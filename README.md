# Auto Email Sender

A simple tool for automated email sending — schedule and send to multiple recipients effortlessly.

---

## ✨ Features
- Auto daily email scheduling
- Support multiple recipients
- Custom subject & body from text file
- Attach multiple files
- Timezone support
  
---

## 📦 Requirements
- Python 3.8+ (make sure it's installed)
- pip (Python package manager)
- SMTP-compatible email account (Gmail, Outlook, Yahoo, etc.)
- Required libraries:
  - schedule  
  - art  
  - python-dotenv  
  - pytz  

---

## 📁 Folder Structure
```
auto-email-sender/
 ├─ bot_email.py
 ├─ .env
 ├─ email_subject.txt
 ├─ email_body.txt
 ├─ email_config.txt
 ├─ requirements.txt
 ├─ timezone_list.txt
 ├─ attachments/
 │   ├─ Your file to send 1
 │   ├─ Your file to send 2
 │   └─ ...
```
---
## ⚙️ Setup

Clone this repository:
```
git clone https://github.com/rerejabal/auto-email-sender.git
cd auto-email-sender
```
Activate the virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
Install dependency:
```
pip install -r requirements.txt
```
Change .env file with your email credentials:

⚠️ Gmail requires an App Password (not your normal password).
Create one via:
Google Account → Security → App passwords.
If its not there, search: App Password.
```
EMAIL_SENDER=youremail@gmail.com
EMAIL_PASSWORD=yourapppassword
```
### Prepare your files:
- email_subject.txt → subject of the email

For example:
```
Job Application
```
- email_body.txt → body of the email

For example:
```
To: HR Department
PT. Chang Shin Reksa Jaya

Dear Sir/Madam,

My name is Salma Nurhulaida, and I would like to apply for a position at PT. Chang Shin Reksa Jaya.
I am confident that I can contribute to supporting the company’s vision and mission. Enclosed are my application documents for your consideration.

I sincerely hope for the opportunity to further discuss my qualifications and to contribute to your esteemed company.

Thank you very much for your attention.

Sincerely,
Salma Nurhulaida
```
- email_config.txt → configuration (recipients, time, timezone, attachments)
- attachments → place your attachments file

Example email_config.txt:
```
RECEIVERS=example1@gmail.com,example2@gmail.com,example3@gmail.com
SEND_TIME=07:20
TIMEZONE=Asia/Jakarta
ATTACHMENTS=CV.pdf,song.mp3,your naked video.mp4
```

---
## 🚀 Run the Script
Once everything is configured properly, start the bot with:
```
python bot_email.py
```
And if you prefer a simpler way, you can use auto_start.bat file (already provided).
