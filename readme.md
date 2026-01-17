# 📧 FileMailer - Secure File Email Service

<div align="center">

![FileMailer Banner](https://img.shields.io/badge/FileMailer-Secure%20Transfer-red?style=for-the-badge&logo=gmail)

**A beautiful, secure Flask web application for instant file sharing via email**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-yaminiverma.pythonanywhere.com-blue?style=for-the-badge&logo=python)](https://yaminiverma.pythonanywhere.com/)
[![GitHub](https://img.shields.io/badge/GitHub-lovnishverma%2Ffilemailer-black?style=for-the-badge&logo=github)](https://github.com/lovnishverma/filemailer)

[![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

[Live Demo](https://yaminiverma.pythonanywhere.com/) • [Report Bug](https://github.com/lovnishverma/filemailer/issues) • [Request Feature](https://github.com/lovnishverma/filemailer/issues)

</div>

---

## 🎬 Live Demo

**Try it now:** [https://yaminiverma.pythonanywhere.com/](https://yaminiverma.pythonanywhere.com/)

> **Note:** The live demo requires an access password for security. Contact the repository owner for demo access.

---

## ✨ Features

### 🎨 **Beautiful Modern UI**
- Animated gradient background with smooth transitions
- Responsive design that works on all devices
- Drag-and-drop file upload interface
- Real-time file preview with icons
- Elegant flash message notifications

### 🔒 **Security & Privacy**
- Password-protected uploads
- Secure file handling with werkzeug
- Automatic file cleanup after sending
- Session security with secret keys
- Environment variable configuration

### 📁 **Smart File Management**
- Upload up to **100 files** simultaneously
- Support for **all file types** (PDF, images, documents, etc.)
- Real-time size calculation and validation
- Gmail 25MB limit enforcement
- Individual file icons and size display

### 🗑️ **Auto-Cleanup System**
- Immediate file deletion after email sent
- Background cleanup every 5 minutes
- Removes files older than 30 minutes
- Manual cleanup option available
- Zero file retention for privacy

### 📧 **Email Features**
- Direct Gmail SMTP integration
- Detailed email with file list and sizes
- Professional email formatting
- Attachment support up to 25MB (Gmail limit)
- Instant delivery confirmation

### 💡 **User Experience**
- Live file count and total size display
- Color-coded warnings (yellow/red for size limits)
- Loading states with spinner animations
- File type-specific icons
- Auto-dismissing notifications

---

## 📸 Screenshots

### Upload Interface

<img width="615" height="908" alt="image" src="https://github.com/user-attachments/assets/418202e7-8496-4d53-a2ec-0d5eddb767cf" />

Note: Yamini Verma is my Sister she is using it that's why her name is in the copyright section.

![sent](https://github.com/user-attachments/assets/b55fff4b-d864-4286-96e2-59cc3adc688b)

---

<img width="1510" height="581" alt="image" src="https://github.com/user-attachments/assets/24ffec70-81ea-4d6e-b001-d940fd1d2b40" />
 
---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Gmail account with App Password
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lovnishverma/filemailer.git
   cd filemailer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your credentials:
   ```env
   EMAIL_ADDRESS=your-gmail@gmail.com
   EMAIL_PASSWORD=your-app-password-here
   RECIPIENT_EMAIL=where-to-send@email.com
   APP_SECRET_KEY=your-secret-key-123
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open browser**
   ```
   http://localhost:5000
   ```

---

## 📧 Gmail App Password Setup

### Step-by-Step Guide

1. **Enable 2-Step Verification**
   - Go to https://myaccount.google.com/security
   - Enable "2-Step Verification"

2. **Generate App Password**
   - Visit https://myaccount.google.com/apppasswords
   - Select app: **Mail**
   - Select device: **Other** → Enter "FileMailer"
   - Click **Generate**

3. **Copy the password**
   ```
   Format: xxxx xxxx xxxx xxxx (16 characters)
   ```

4. **Update .env file**
   ```env
   EMAIL_PASSWORD=abcd efgh ijkl mnop
   ```

> ⚠️ **Important:** Use App Password, NOT your regular Gmail password!

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `EMAIL_ADDRESS` | Your Gmail address (sender) | `youremail@gmail.com` | ✅ Yes |
| `EMAIL_PASSWORD` | Gmail App Password (16 chars) | `abcd efgh ijkl mnop` | ✅ Yes |
| `RECIPIENT_EMAIL` | Where to send files | `recipient@email.com` | ✅ Yes |
| `APP_SECRET_KEY` | Flask session security key | `random-secret-key-123` | ✅ Yes |

### Application Limits

| Setting | Default Value | Description |
|---------|---------------|-------------|
| Max Files | 100 | Maximum files per upload |
| Max Upload Size | 500 MB | Flask upload limit |
| Gmail Limit | 25 MB | Total attachment size (enforced) |
| Cleanup Interval | 5 minutes | Background cleanup frequency |
| File Retention | 30 minutes | Delete files older than this |

### Customization

Edit `app.py` to customize:

```python
# File Upload Settings
MAX_FILES = 100  # Change maximum file count
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # Change size limit

# Auto-cleanup settings
CLEANUP_AFTER_SEND = True  # Delete after sending
AUTO_CLEANUP_ENABLED = True  # Enable background cleanup
CLEANUP_OLDER_THAN_MINUTES = 30  # File retention time
```

---

## 🎯 Usage Guide

### Basic Upload Flow

1. **Visit the application**
   - Open http://localhost:5000 (or live demo)

2. **Select files**
   - Click upload area OR drag and drop
   - Up to 100 files, max 25MB total

3. **Review files**
   - Check file list with individual sizes
   - Watch for size warnings (yellow/red)

4. **Enter password**
   - Type access password (default: `Change in app.py code`)

5. **Send**
   - Click "Send Files Now"
   - Wait for confirmation
   - Check recipient email!

### Advanced Features

#### Manual Cleanup
If temporary files exist, a cleanup button appears:
```
🗑️ Clean 3 temporary file(s)
```

#### Size Warnings
- **Green** (< 20MB): ✅ Safe to send
- **Yellow** (20-25MB): ⚠️ Close to limit
- **Red** (> 25MB): ❌ Too large, blocked

#### File Type Icons
Files display with appropriate icons:
- 📄 PDF files
- 📘 Word documents
- 📗 Excel spreadsheets
- 📙 PowerPoint presentations
- 🖼️ Images (JPG, PNG, GIF)
- 📦 Archives (ZIP, RAR)

---

## 🌐 Deployment

### Local Network Access

Share on your local network:

1. **Find your IP address**
   ```bash
   # Windows
   ipconfig
   
   # macOS/Linux
   ifconfig
   ```

2. **Run the app**
   ```bash
   python app.py
   ```

3. **Access from other devices**
   ```
   http://YOUR-IP-ADDRESS:5000
   ```

### PythonAnywhere Deployment

Deploy for free on PythonAnywhere:

1. **Create account**
   - Sign up at https://www.pythonanywhere.com
   - Choose free tier

2. **Upload files**
   - Upload `app.py`, `templates/`, and `requirements.txt`
   - Create `uploads/` folder

3. **Configure web app**
   - Go to Web tab
   - Create new Flask app
   - Point to your `app.py`

4. **Set environment variables**
   - Edit `app.py` or use PythonAnywhere environment settings
   - Add all credentials from `.env`

5. **Install requirements**
   ```bash
   pip install --user -r requirements.txt
   ```

6. **Reload and test**
   - Click "Reload" button
   - Visit your-username.pythonanywhere.com

### Production Recommendations

For production deployment:

```python
# app.py - Production settings
if __name__ == '__main__':
    app.run(
        debug=False,        # Disable debug mode
        host='0.0.0.0',     # Allow external connections
        port=5000,
        threaded=True       # Handle multiple requests
    )
```

Additional steps:
- ✅ Use strong `APP_SECRET_KEY`
- ✅ Set `debug=False`
- ✅ Use environment variables (not hardcoded)
- ✅ Implement rate limiting
- ✅ Add HTTPS/SSL
- ✅ Use production WSGI server (Gunicorn)
- ✅ Set up logging
- ✅ Add monitoring

---

## 🐛 Troubleshooting

### Email Not Sending

#### Problem: "Authentication failed"

**Solutions:**
1. ✅ Use **App Password**, not regular Gmail password
2. ✅ Enable 2-Step Verification first
3. ✅ Verify no extra spaces in `EMAIL_PASSWORD`
4. ✅ Generate new App Password
5. ✅ Check Gmail security: https://myaccount.google.com/notifications

#### Problem: "Connection timeout"

**Solutions:**
1. ✅ Check internet connection
2. ✅ Verify firewall allows port 587
3. ✅ Try different network (corporate networks may block SMTP)
4. ✅ Check Gmail status: https://www.google.com/appsstatus

### File Upload Issues

#### Problem: "Invalid Password"

**Solutions:**

1. ✅ **Ensure Variable Type Consistency:** Since you are defining `AUTH_PASSWORD` directly in your Python code (and not using a `.env` file), the value **must be a string** (enclosed in quotes, e.g., `'123456'`). Defining it as an integer (e.g., `123456`) will cause authentication to fail because data received from the HTML form is always read as a string.
2. ✅ **Check for Whitespace:** Verify that there are no accidental spaces inside the quotes (e.g., `' 123456 '`) or trailing typos.
3. ✅ **Reload Server:** You must reload the web application (click the green "Reload" button on the Web tab) for any changes to the variable in `flask_app.py` to take effect.

#### Problem: "Files too large for Gmail"

**Solutions:**
1. ✅ Total size exceeds 25MB (Gmail hard limit)
2. ✅ Upload fewer files
3. ✅ Compress files with ZIP/RAR
4. ✅ Use cloud storage for large files
5. ✅ Split into multiple emails

#### Problem: "413 Request Entity Too Large"

**Solutions:**
1. ✅ Total upload exceeds 500MB
2. ✅ Reduce file count or size
3. ✅ Check `MAX_CONTENT_LENGTH` in `app.py`

### Interface Issues

#### Problem: "Template not found"

**Solutions:**
1. ✅ Ensure `templates/` folder exists
2. ✅ Verify `index.html` is inside `templates/`
3. ✅ Check file name case (case-sensitive on Linux)

#### Problem: "Styling broken"

**Solutions:**
1. ✅ Check internet (Tailwind CSS loads from CDN)
2. ✅ Clear browser cache (Ctrl+F5)
3. ✅ Try different browser

---

## 📊 Project Structure

```
filemailer/
│
├── app.py                          # Main Flask application
│   ├── Configuration               # Email, security, file settings
│   ├── Helper Functions            # File handling, cleanup, email
│   ├── Background Tasks            # Auto-cleanup thread
│   ├── Routes                      # /, /send, /cleanup
│   └── Error Handlers              # 413, 500 errors
│
├── templates/
│   └── index.html                  # Frontend interface
│       ├── Navigation              # Header with branding
│       ├── Flash Messages          # Animated notifications
│       ├── Upload Area             # Drag-and-drop zone
│       ├── File Preview            # Live file list
│       ├── Password Field          # Access control
│       └── JavaScript              # File validation, UI
│
├── uploads/                        # Temporary file storage (auto-created)
│
├── .env                            # Environment variables (create this)
├── .env.example                    # Configuration template
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

---

## 🔐 Security Features

### Built-in Security

1. **Password Protection**
   - Required for all uploads
   - Server-side validation
   - Environment variable storage

2. **Secure File Handling**
   - `secure_filename()` prevents directory traversal
   - Timestamp-based unique naming
   - Automatic cleanup (no file retention)

3. **Session Security**
   - Flask secret key for sessions
   - CSRF protection ready
   - Secure cookie handling

4. **Data Privacy**
   - Files deleted immediately after send
   - Background cleanup for orphaned files
   - No database or logging of file contents

### Best Practices

✅ **DO:**
- Use strong, unique `APP_SECRET_KEY`
- Change `AUTH_PASSWORD` from default
- Keep `.env` file secure (never commit)
- Use HTTPS in production
- Rotate App Passwords regularly

❌ **DON'T:**
- Share your `.env` file
- Use regular Gmail password (use App Password)
- Commit credentials to Git
- Run with `debug=True` in production

---

## ❓ FAQ

### General Questions

**Q: Can I use this with other email providers?**

A: Yes! Update SMTP settings in `app.py`:
```python
# For Outlook/Hotmail
server = smtplib.SMTP('smtp-mail.outlook.com', 587)

# For Yahoo
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
```

**Q: How do I send to multiple recipients?**

A: Modify `RECIPIENT_EMAIL` in `.env`:
```env
RECIPIENT_EMAIL=email1@example.com,email2@example.com
```

**Q: Can I change the upload password?**

A: Yes! Edit `.env`:
```env
AUTH_PASSWORD=your-new-password
```
Then restart the app.

**Q: Why 25MB limit when Flask allows 500MB?**

A: Gmail has a strict 25MB limit for email attachments. The app enforces this to prevent send failures.

**Q: Are uploaded files stored permanently?**

A: No! Files are deleted:
- Immediately after sending
- After 30 minutes if unsent
- Via manual cleanup button
- By background cleanup task

### Technical Questions

**Q: How do I generate a secure APP_SECRET_KEY?**

A: Run this command:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Q: Can I customize the email template?**

A: Yes! Edit the `body` variable in `send_email_with_attachments()` function in `app.py`.

**Q: How do I disable auto-cleanup?**

A: Edit `app.py`:
```python
CLEANUP_AFTER_SEND = False
AUTO_CLEANUP_ENABLED = False
```

**Q: Can I add file type restrictions?**

A: Yes! Add validation in `save_uploaded_files()`:
```python
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork the repository**
   ```bash
   git clone https://github.com/lovnishverma/filemailer.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Test thoroughly

4. **Commit changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```

5. **Push to branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open Pull Request**
   - Describe your changes
   - Link any related issues
   - Wait for review

### Contribution Ideas

- [ ] Multi-language support (i18n)
- [ ] Database for tracking sent emails
- [ ] User authentication system
- [ ] File compression before sending
- [ ] Cloud storage integration (Google Drive, Dropbox)
- [ ] Email scheduling/delayed send
- [ ] Upload progress bar
- [ ] File preview before sending
- [ ] Dark mode toggle
- [ ] Mobile app (React Native/Flutter)
- [ ] REST API for programmatic access
- [ ] Webhook notifications
- [ ] Email templates
- [ ] Multiple recipient groups
- [ ] File encryption

### Code of Conduct

- Be respectful and inclusive
- Follow the project's coding standards
- Test your changes before submitting
- Document new features
- Help review others' PRs

---

## 📜 License

This project is licensed under the MIT License.

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

---

## 🙏 Acknowledgments

### Technologies Used

- **[Flask](https://flask.palletsprojects.com/)** - Python web framework
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Font Awesome](https://fontawesome.com/)** - Icon library
- **[Google Fonts (Inter)](https://fonts.google.com/)** - Typography
- **[Gmail SMTP](https://support.google.com/mail/answer/7126229)** - Email delivery
- **[Werkzeug](https://werkzeug.palletsprojects.com/)** - WSGI utilities
- **[PythonAnywhere](https://www.pythonanywhere.com/)** - Hosting platform

### Inspiration

- Modern web design principles
- User privacy and security best practices
- Simple, effective file sharing solutions

---

## 📞 Support & Contact

### Get Help

- 🐛 **Report Bugs:** [GitHub Issues](https://github.com/lovnishverma/filemailer/issues)
- 💡 **Request Features:** [GitHub Issues](https://github.com/lovnishverma/filemailer/issues)
- 📧 **Email:** [Create an issue for support](https://github.com/lovnishverma/filemailer/issues)

### Resources

- **Flask Documentation:** https://flask.palletsprojects.com/
- **Gmail SMTP Guide:** https://support.google.com/mail/answer/7126229
- **PythonAnywhere Docs:** https://help.pythonanywhere.com/

---

## 📈 Roadmap

### Version 1.0 ✅
- [x] Basic file upload and email
- [x] Gmail SMTP integration
- [x] Password protection
- [x] Auto-cleanup system
- [x] Modern UI/UX
- [x] Flash messages
- [x] File preview

### Version 2.0 🚧
- [ ] User authentication
- [ ] Upload history
- [ ] Email templates
- [ ] Multiple recipients
- [ ] File compression
- [ ] Cloud storage integration

### Version 3.0 📋
- [ ] REST API
- [ ] Mobile app
- [ ] Scheduled sending
- [ ] File encryption
- [ ] Admin dashboard
- [ ] Analytics

---

## 📊 Stats

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/lovnishverma/filemailer?style=social)
![GitHub forks](https://img.shields.io/github/forks/lovnishverma/filemailer?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/lovnishverma/filemailer?style=social)

</div>

---

<div align="center">

**Made with ❤️ by [Lovnish Verma](https://github.com/lovnishverma)**

**Last Updated:** January 2026 | **Version:** 1.0.0

⭐ **Star this repo** if you find it helpful!

[🔗 Live Demo](https://yaminiverma.pythonanywhere.com/) • [📁 GitHub](https://github.com/lovnishverma/filemailer) • [🐛 Issues](https://github.com/lovnishverma/filemailer/issues)

</div>
