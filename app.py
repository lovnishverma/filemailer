import os
import time
import secrets
from datetime import datetime, timedelta
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading

app = Flask(__name__)

# ==================== CONFIGURATION ====================
# Email Settings
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'yamini.verma1600@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'mbvy nmtv mygd fhgj')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'yamini.verma1600@gmail.com')

# Security Settings
app.secret_key = os.getenv('APP_SECRET_KEY', secrets.token_hex(32))
AUTH_PASSWORD = os.getenv('AUTH_PASSWORD')

# File Upload Settings
UPLOAD_FOLDER = 'uploads'
MAX_FILES = 100
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Auto-cleanup settings
CLEANUP_AFTER_SEND = True  # Delete files immediately after sending
AUTO_CLEANUP_ENABLED = True  # Enable automatic cleanup of old files
CLEANUP_OLDER_THAN_MINUTES = 30  # Delete files older than 30 minutes

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==================== HELPER FUNCTIONS ====================

def get_file_age_minutes(filepath):
    """Get the age of a file in minutes"""
    if not os.path.exists(filepath):
        return 0
    file_time = os.path.getmtime(filepath)
    current_time = time.time()
    age_seconds = current_time - file_time
    return age_seconds / 60

def cleanup_old_files():
    """Remove files older than specified time from uploads folder"""
    if not AUTO_CLEANUP_ENABLED:
        return
    
    try:
        deleted_count = 0
        total_size = 0
        
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            
            # Skip if it's a directory
            if os.path.isdir(filepath):
                continue
            
            # Check file age
            age_minutes = get_file_age_minutes(filepath)
            
            if age_minutes > CLEANUP_OLDER_THAN_MINUTES:
                file_size = os.path.getsize(filepath)
                os.remove(filepath)
                deleted_count += 1
                total_size += file_size
        
        if deleted_count > 0:
            total_size_mb = total_size / (1024 * 1024)
            print(f"[CLEANUP] Deleted {deleted_count} old file(s), freed {total_size_mb:.2f}MB")
    
    except Exception as e:
        print(f"[CLEANUP ERROR] {str(e)}")

def cleanup_specific_files(file_paths):
    """Delete specific files from the system"""
    deleted = 0
    for filepath in file_paths:
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                deleted += 1
        except Exception as e:
            print(f"[DELETE ERROR] Could not delete {filepath}: {str(e)}")
    
    if deleted > 0:
        print(f"[CLEANUP] Deleted {deleted} file(s) after email send")

def save_uploaded_files(files):
    """Save uploaded files to disk and return file information"""
    saved_files = []
    total_size = 0
    
    for f in files:
        if f and f.filename:
            # Secure the filename
            filename = secure_filename(f.filename)
            
            # Add timestamp to avoid conflicts
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            name, ext = os.path.splitext(filename)
            unique_filename = f"{name}_{timestamp}{ext}"
            
            filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
            
            # Save file
            f.save(filepath)
            
            # Get file info
            file_size = os.path.getsize(filepath)
            total_size += file_size
            
            saved_files.append({
                'name': filename,  # Original name for email
                'filepath': filepath,
                'size': file_size
            })
    
    return saved_files, total_size

def format_bytes(bytes_size):
    """Format bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} TB"

def send_email_with_attachments(file_list, total_size):
    """Send email with file attachments"""
    try:
        total_size_mb = total_size / (1024 * 1024)
        
        # Setup email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"📧 FileMailer: {len(file_list)} file(s) - {format_bytes(total_size)}"
        
        # Email body
        body = f"""Hello,

You have received {len(file_list)} file(s) via FileMailer.

Upload Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Total Files: {len(file_list)}
• Total Size: {format_bytes(total_size)}
• Sent At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Files Included:
"""
        for idx, file_info in enumerate(file_list, 1):
            file_size_str = format_bytes(file_info['size'])
            body += f"{idx}. {file_info['name']} ({file_size_str})\n"
        
        body += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Powered by FileMailer
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach files
        for file_info in file_list:
            with open(file_info['filepath'], 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {file_info["name"]}'
            )
            msg.attach(part)
        
        # Send via Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, text)
        server.quit()
        
        return True, "Email sent successfully!"
    
    except Exception as e:
        return False, f"Error sending email: {str(e)}"

# ==================== BACKGROUND CLEANUP TASK ====================

def background_cleanup_task():
    """Background task that runs periodic cleanup"""
    while True:
        time.sleep(300)  # Run every 5 minutes
        cleanup_old_files()

# Start background cleanup thread
if AUTO_CLEANUP_ENABLED:
    cleanup_thread = threading.Thread(target=background_cleanup_task, daemon=True)
    cleanup_thread.start()
    print("[STARTUP] Background cleanup task started")

# ==================== ROUTES ====================

@app.route('/')
def index():
    # Run cleanup check on page load
    cleanup_old_files()
    
    # Get upload folder stats
    file_count = len([f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))])
    
    return render_template('index.html', temp_files=file_count)

@app.route('/send', methods=['POST'])
def send_email_route():
    # Check password first
    password = request.form.get('password', '')
    
    if password != AUTH_PASSWORD:
        flash('🔒 Invalid password! Please enter the correct access password.', 'error')
        return redirect(url_for('index'))
    
    # Check if files are present
    if 'attachments' not in request.files:
        flash('No files selected. Please choose files to upload.', 'error')
        return redirect(url_for('index'))
    
    files = request.files.getlist('attachments')
    
    # Validate files
    if not files or files[0].filename == '':
        flash('No files selected. Please choose files to upload.', 'error')
        return redirect(url_for('index'))
    
    # Check file count
    if len(files) > MAX_FILES:
        flash(f'Maximum {MAX_FILES} files allowed. You tried to upload {len(files)} files.', 'error')
        return redirect(url_for('index'))
    
    try:
        # Save files to disk
        saved_files, total_size = save_uploaded_files(files)
        
        if not saved_files:
            flash('No valid files to send.', 'error')
            return redirect(url_for('index'))
        
        # Check Gmail size limit
        total_size_mb = total_size / (1024 * 1024)
        if total_size_mb > 25:
            # Cleanup files before returning error
            file_paths = [f['filepath'] for f in saved_files]
            cleanup_specific_files(file_paths)
            
            flash(f'Files too large for Gmail! Total size: {total_size_mb:.2f}MB. Gmail limit is 25MB. Please compress files or upload fewer files.', 'error')
            return redirect(url_for('index'))
        
        # Send email
        success, message = send_email_with_attachments(saved_files, total_size)
        
        # Cleanup files after sending
        if CLEANUP_AFTER_SEND:
            file_paths = [f['filepath'] for f in saved_files]
            cleanup_specific_files(file_paths)
        
        if success:
            flash(f'✅ Success! Sent {len(saved_files)} file(s) totaling {format_bytes(total_size)} to {RECIPIENT_EMAIL}', 'success')
        else:
            flash(f'❌ Error: {message}', 'error')
    
    except Exception as e:
        flash(f'❌ Error processing files: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/cleanup', methods=['POST'])
def manual_cleanup():
    """Manual cleanup endpoint"""
    cleanup_old_files()
    flash('🗑️ Cleanup completed!', 'success')
    return redirect(url_for('index'))

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    flash('⚠️ Upload too large! Maximum size is 500MB. Gmail limit is 25MB for attachments.', 'error')
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(e):
    """Handle internal server errors"""
    flash(f'❌ Server error: {str(e)}', 'error')
    return redirect(url_for('index'))

# ==================== STARTUP ====================

if __name__ == '__main__':
    print("=" * 50)
    print("FileMailer Starting...")
    print(f"Email: {EMAIL_ADDRESS}")
    print(f"Recipient: {RECIPIENT_EMAIL}")
    print(f"Auth Password: {'*' * len(AUTH_PASSWORD)} (Protected)")
    print(f"Max Files: {MAX_FILES}")
    print(f"Max Size: 500MB")
    print(f"Upload Folder: {UPLOAD_FOLDER}")
    print(f"Auto Cleanup: {AUTO_CLEANUP_ENABLED}")
    print(f"Cleanup After Send: {CLEANUP_AFTER_SEND}")
    print(f"Cleanup Old Files (>{CLEANUP_OLDER_THAN_MINUTES} min): {AUTO_CLEANUP_ENABLED}")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
