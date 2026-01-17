import os
import time
import secrets
import mimetypes
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

# Load environment variables
project_folder = os.path.expanduser('~/mysite')
load_dotenv(os.path.join(project_folder, '.env'))

app = Flask(__name__)

# ==================== CONFIGURATION ====================
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
app.secret_key = os.getenv('APP_SECRET_KEY', secrets.token_hex(32))
AUTH_PASSWORD = '175011'  # Note: Must be string

UPLOAD_FOLDER = os.path.join(project_folder, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Gmail limit is 25MB encoded (approx 19MB actual file size)
MAX_EMAIL_SIZE_MB = 19 
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CLEANUP_MINUTES = 30 

# ==================== HELPER FUNCTIONS ====================

def cleanup_old_files():
    """Deletes files older than CLEANUP_MINUTES"""
    try:
        now = time.time()
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                file_age = (now - os.path.getmtime(filepath)) / 60
                if file_age > CLEANUP_MINUTES:
                    os.remove(filepath)
    except Exception as e:
        print(f"Cleanup error: {e}")

def get_file_count():
    """Returns the number of files currently in the upload folder"""
    try:
        return len([name for name in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, name))])
    except:
        return 0

def send_email(files_info):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"New Upload: {len(files_info)} file(s)"
        
        body = "Files uploaded via Secure FileMailer."
        msg.attach(MIMEText(body, 'plain'))

        for f_info in files_info:
            path = f_info['path']
            filename = f_info['name']
            ctype, encoding = mimetypes.guess_type(path)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)

            with open(path, 'rb') as f:
                part = MIMEBase(maintype, subtype)
                part.set_payload(f.read())
            
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(part)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            
        return True, "Email sent successfully"
    except Exception as e:
        return False, str(e)

# ==================== ROUTES ====================

@app.route('/')
def index():
    cleanup_old_files()
    # Pass temp_files count to the template
    return render_template('index.html', temp_files=get_file_count())

@app.route('/cleanup', methods=['POST'])
def cleanup_route():
    """Manual cleanup route triggered by the button in your HTML"""
    try:
        count = 0
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
                count += 1
        flash(f'Cleaned up {count} temporary files.', 'success')
    except Exception as e:
        flash(f'Error cleaning files: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/send', methods=['POST'])
def send_files():
    if request.form.get('password') != AUTH_PASSWORD:
        flash('Wrong Password! Access Denied.', 'error')
        return redirect(url_for('index'))

    if 'attachments' not in request.files:
        flash('No files part', 'error')
        return redirect(url_for('index'))
        
    files = request.files.getlist('attachments')
    if not files or files[0].filename == '':
        flash('No files selected', 'error')
        return redirect(url_for('index'))

    saved_files = []
    total_size = 0

    try:
        for f in files:
            filename = secure_filename(f.filename)
            unique_name = f"{int(time.time())}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            
            f.save(filepath)
            size = os.path.getsize(filepath)
            total_size += size
            saved_files.append({'path': filepath, 'name': filename})

        # Check total size
        total_size_mb = total_size / (1024 * 1024)
        if total_size_mb > MAX_EMAIL_SIZE_MB:
            for f in saved_files:
                os.remove(f['path'])
            flash(f'Total size {total_size_mb:.1f}MB is too big. Safe Gmail limit is ~{MAX_EMAIL_SIZE_MB}MB.', 'error')
            return redirect(url_for('index'))

        success, message = send_email(saved_files)

        # Auto cleanup after send
        for f in saved_files:
            if os.path.exists(f['path']):
                os.remove(f['path'])

        if success:
            flash(f'Success! {len(saved_files)} files sent.', 'success')
        else:
            flash(f'Error sending email: {message}', 'error')

    except Exception as e:
        flash(f'System Error: {str(e)}', 'error')

    return redirect(url_for('index'))
