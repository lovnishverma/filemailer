# FileMailer - Secure File Email Service

A lightweight Flask web application that allows users to upload and email multiple files instantly through Gmail's SMTP server. Perfect for quick file sharing without the need for cloud storage services.

![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=flat&logo=flask)
![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- ✨ **Modern UI** - Beautiful gradient animated interface with Tailwind CSS
- 📧 **Email Integration** - Direct Gmail SMTP integration for instant delivery
- 📁 **Bulk Upload** - Upload up to 100 files simultaneously
- 📊 **Real-time Feedback** - Live file count, size calculation, and warnings
- 🔒 **Gmail Limit Protection** - Automatic validation against Gmail's 25MB attachment limit
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- ⚡ **Fast Processing** - Efficient file handling and email delivery
- 🎯 **User-Friendly** - Simple drag-and-drop interface with visual feedback

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [File Limits](#-file-limits)
- [Gmail Setup](#-gmail-setup)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

## 🎬 Demo

1. Visit the application URL
2. Click or drag files to upload area
3. See live preview with file names and sizes
4. Submit to send via email
5. Receive confirmation message

## 🔧 Prerequisites

- **Python 3.7+** installed on your system
- **Gmail account** with 2-Step Verification enabled
- **Gmail App Password** (see [Gmail Setup](#-gmail-setup))
- **pip** package manager

## 📥 Installation

### Step 1: Clone or Download

```bash
# Clone the repository (if using Git)
git clone https://github.com/yourusername/filemailer.git
cd filemailer

# OR download and extract the ZIP file
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install flask
```

That's it! Flask is the only dependency needed.

## ⚙️ Configuration

### Edit app.py

Open `app.py` and update the configuration section:

```python
# ----------------- CONFIGURATION -----------------
EMAIL_ADDRESS = "your-email@gmail.com"        # Your Gmail address
EMAIL_PASSWORD = "your app password here"      # Gmail App Password (16 chars)
RECIPIENT_EMAIL = "recipient@email.com"        # Where to send files

# Optional: Adjust limits
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max upload
MAX_FILES = 100  # Maximum number of files
# -------------------------------------------------
```

### Important Configuration Notes:

- **EMAIL_PASSWORD**: Must be a Gmail App Password (NOT your regular Gmail password)
- **MAX_CONTENT_LENGTH**: Flask upload limit (default: 500MB)
- **MAX_FILES**: Maximum files per upload (default: 100)
- Gmail has a hard limit of 25MB total attachments - the app enforces this

## 📧 Gmail Setup

### Generate Gmail App Password

1. **Enable 2-Step Verification**
   - Go to https://myaccount.google.com/security
   - Find "2-Step Verification" and turn it on
   - Complete the setup process

2. **Create App Password**
   - Visit https://myaccount.google.com/apppasswords
   - Select app: **Mail**
   - Select device: **Other (Custom name)** → Type "FileMailer"
   - Click **Generate**
   - Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)

3. **Update app.py**
   ```python
   EMAIL_PASSWORD = "abcd efgh ijkl mnop"  # Your generated password
   ```

### Why App Password?

- Gmail doesn't allow regular passwords for SMTP access
- App Passwords are more secure and app-specific
- They can be revoked without changing your main password

## 🚀 Usage

### Starting the Application

```bash
# Make sure you're in the project directory
# and virtual environment is activated

python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
```

### Using the Web Interface

1. **Open Browser**
   - Navigate to: `http://localhost:5000`
   - Or use your computer's IP for network access

2. **Upload Files**
   - Click the upload area or drag files
   - Select up to 100 files (any file type)
   - See real-time file list and size calculation

3. **Submit**
   - Click "Send Files Now"
   - Wait for confirmation message
   - Check recipient email inbox

### Success Response

After successful upload, you'll see:
```
Success! Files mailed via Gmail.
Sent 5 file(s) totaling 12.34MB
```

## 📊 File Limits

| Limit Type | Value | Notes |
|------------|-------|-------|
| **Max Files** | 100 files | Per single upload |
| **Max Upload Size** | 500 MB | Total Flask limit |
| **Gmail Attachment Limit** | 25 MB | **Enforced by app** |
| **File Types** | Any | No restrictions |

### Gmail Limit Handling

The app automatically checks total file size:

- **Under 20MB**: ✅ Green light - sends normally
- **20-25MB**: ⚠️ Warning shown - sends with caution
- **Over 25MB**: ❌ Rejected with helpful message:
  ```
  Warning: Files too large for Gmail
  Total size: 28.5MB
  Gmail has a 25MB limit for attachments.
  ```

## 🌐 Deployment

### Local Network Access

To access from other devices on your network:

1. Find your computer's IP address:
   ```bash
   # Windows
   ipconfig
   
   # macOS/Linux
   ifconfig
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Access from other devices:
   ```
   http://YOUR-IP-ADDRESS:5000
   ```

### PythonAnywhere Deployment

Perfect for hosting this app for free!

1. **Create Account**
   - Sign up at https://www.pythonanywhere.com
   - Choose free tier

2. **Upload Files**
   - Upload `app.py` and `templates/index.html`
   - Create `templates` folder if needed

3. **Configure Web App**
   - Go to Web tab
   - Create new web app (Flask)
   - Set Python version (3.7+)
   - Point to your `app.py`

4. **Update Settings**
   - Edit `app.py` with your Gmail credentials
   - Set `debug=False` for production

5. **Reload**
   - Click "Reload" button
   - Access via your PythonAnywhere URL

### Production Considerations

For production deployment:

```python
# app.py - Production settings
if __name__ == '__main__':
    app.run(
        debug=False,           # Disable debug mode
        host='0.0.0.0',        # Allow external connections
        port=5000,             # Standard port
        threaded=True          # Handle multiple requests
    )
```

Additional recommendations:
- Use environment variables for credentials
- Implement rate limiting
- Add user authentication
- Set up HTTPS/SSL
- Use production WSGI server (Gunicorn, uWSGI)
- Add logging for monitoring
- Implement error tracking

## 🐛 Troubleshooting

### Email Not Sending

**Problem**: "Authentication failed" or "Login failed"

**Solutions**:
1. ✅ Verify you're using **App Password**, not regular password
2. ✅ Check 2-Step Verification is enabled
3. ✅ Ensure no extra spaces in EMAIL_PASSWORD
4. ✅ Try generating a new App Password
5. ✅ Check Gmail security alerts: https://myaccount.google.com/notifications

**Problem**: "Connection refused" or "Timeout"

**Solutions**:
1. ✅ Check internet connection
2. ✅ Verify firewall isn't blocking port 587
3. ✅ Try different network (sometimes corporate networks block SMTP)
4. ✅ Check if Gmail is down: https://www.google.com/appsstatus

### File Upload Issues

**Problem**: "413 Request Entity Too Large"

**Solutions**:
1. ✅ Total upload exceeds 500MB - reduce file count/size
2. ✅ Check `MAX_CONTENT_LENGTH` in app.py
3. ✅ Consider compressing files first

**Problem**: "Files too large for Gmail" error

**Solutions**:
1. ✅ Total size exceeds 25MB (Gmail limit)
2. ✅ Upload fewer files
3. ✅ Compress files with ZIP/RAR
4. ✅ Use cloud storage (Google Drive, Dropbox) instead
5. ✅ Split into multiple emails

**Problem**: Files not appearing in upload area

**Solutions**:
1. ✅ Check browser console for JavaScript errors
2. ✅ Try different browser (Chrome, Firefox recommended)
3. ✅ Clear browser cache
4. ✅ Check file permissions

### Interface Issues

**Problem**: Styling broken or missing

**Solutions**:
1. ✅ Check internet connection (Tailwind CSS loads from CDN)
2. ✅ Verify `templates/index.html` is in correct location
3. ✅ Clear browser cache (Ctrl+F5)

**Problem**: "Template not found" error

**Solutions**:
1. ✅ Ensure `templates/` folder exists
2. ✅ Verify `index.html` is inside `templates/`
3. ✅ Check file name is exactly `index.html` (case-sensitive on Linux)

## ❓ FAQ

**Q: Can I use this with other email providers?**

A: Yes! Update the SMTP settings in app.py:
```python
# For Outlook/Hotmail
server = smtplib.SMTP('smtp-mail.outlook.com', 587)

# For Yahoo
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
```

**Q: How do I send to multiple recipients?**

A: Modify app.py:
```python
RECIPIENT_EMAIL = "email1@example.com,email2@example.com"
# Or use a list
RECIPIENT_EMAIL = ["email1@example.com", "email2@example.com"]
```

**Q: Can I add password protection?**

A: Yes! Add authentication to the route:
```python
@app.route('/send', methods=['POST'])
def send_email():
    password = request.form.get('password')
    if password != 'YOUR_SECRET_PASSWORD':
        return "Unauthorized", 401
    # ... rest of code
```

**Q: How do I customize the email subject/body?**

A: Edit these lines in app.py:
```python
msg['Subject'] = f"Custom Subject: {len(files)} file(s)"
body = "Your custom email message here"
```

**Q: Can I save uploaded files instead of deleting them?**

A: Yes! Remove the cleanup code and save files:
```python
# Save files to disk
for fd in file_data:
    with open(f"saved_files/{fd['name']}", 'wb') as f:
        f.write(fd['content'])
```

**Q: Is this secure?**

A: Considerations:
- ✅ Gmail App Password is secure
- ⚠️ Files are transmitted over HTTPS (if deployed properly)
- ⚠️ No encryption on uploaded files (they're emailed as-is)
- ⚠️ Add authentication for production use
- ⚠️ Use environment variables for credentials

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] User authentication system
- [ ] Multiple email provider support
- [ ] File preview before sending
- [ ] Upload progress bar
- [ ] Email templates
- [ ] Scheduled sending
- [ ] File compression
- [ ] Cloud storage integration (Google Drive, Dropbox)
- [ ] Database for tracking sent emails
- [ ] Rate limiting

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2026 Yamini Verma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📞 Support

If you encounter issues:

1. **Check Troubleshooting Section** above
2. **Review Gmail SMTP Guide**: https://support.google.com/mail/answer/7126229
3. **Flask Documentation**: https://flask.palletsprojects.com/
4. **Open an Issue**: Create a detailed bug report with:
   - Error message
   - Steps to reproduce
   - Python version
   - Operating system

## 🙏 Acknowledgments

- **Flask** - Web framework
- **Tailwind CSS** - Styling
- **Font Awesome** - Icons
- **Gmail SMTP** - Email delivery
- **Inter Font** - Typography

## 📊 Project Structure

```
filemailer/
│
├── app.py                     # Main Flask application
│   ├── Configuration          # Email settings, file limits
│   ├── Routes                 # / (index), /send (upload handler)
│   ├── Email Handler          # SMTP connection and sending
│   └── Error Handlers         # 413 file too large
│
├── templates/
│   └── index.html            # Frontend interface
│       ├── Navigation        # Header with branding
│       ├── Upload Area       # Drag-and-drop zone
│       ├── File Preview      # Live file list with sizes
│       ├── Warnings          # Gmail limit alerts
│       └── JavaScript        # File validation and UI updates
│
├── README.md                 # This file
├── requirements.txt          # Python dependencies (optional)
└── .gitignore               # Git ignore rules (optional)
```

## 🔐 Security Best Practices

1. **Never commit credentials** to version control
2. **Use environment variables** in production
3. **Enable HTTPS** for production deployment
4. **Implement rate limiting** to prevent abuse
5. **Add CSRF protection** for forms
6. **Validate file types** if restricting uploads
7. **Scan uploaded files** for malware in production
8. **Use strong App Passwords** and rotate regularly

## 📈 Future Roadmap

- [ ] Dark mode toggle
- [ ] Multiple language support
- [ ] Email scheduling
- [ ] File encryption before sending
- [ ] Upload history with search
- [ ] Bulk email to multiple recipients
- [ ] Integration with cloud storage APIs
- [ ] Mobile app (React Native/Flutter)
- [ ] REST API for programmatic access
- [ ] Webhook notifications

---

**Made with ❤️ by Lovnish Verma**

**Last Updated**: January 2026

**Version**: 2.0.0 (Enhanced Limits Edition)

For questions or feedback, please open an issue or contact the maintainer.

---

⭐ **Star this repo** if you find it helpful!