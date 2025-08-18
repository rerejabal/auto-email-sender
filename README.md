
#### *Read this in other languages:*  
[![English](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/United-States.png)](README.md)
[![Bahasa Indonesia](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Indonesia.png)](README.id.md)
--------
<img width="1084" height="555" alt="Screenshot 2025-08-18 142912" src="https://github.com/user-attachments/assets/397631c3-e43f-402b-aab7-cbf0b27331b7" />


# Auto Email Sender

A simple tool for automated email sending - schedule and send to multiple recipients effortlessly.

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
  - rich 

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
 ├─ auto_start.bat
 ├─ banner_utils.py
 ├─ attachments/
 │   ├─ Your file to send 1
 │   ├─ Your file to send 2
 │   └─ ...
```
---
## ⚙️ Setup
> Right-click the desired folder location, then select Open in Terminal or PowerShell or even Command Prompt if available.

### 1. Clone this repository on Terminal or PowerShell or Command Prompt:

```
git clone https://github.com/rerejabal/auto-email-sender.git
cd auto-email-sender
```
### 2. Install dependency:
```
pip install -r requirements.txt
```
### 3. Prepare your files:
Modify the `.env` file with your email credentials:


> ⚠️ Gmail requires an App Password (not your normal password).
Create one via Google Account → Security → App passwords.
If its not there, search: App Password.
Example of App Password: kjgwxutxzhkyqjkw
```
EMAIL_SENDER=youremail@gmail.com
EMAIL_PASSWORD=yourapppassword
```
`email_subject.txt` → subject of the email

For example:
```
Job Application
```
`email_body.txt` → body of the email

For example:
```
To: HR Department
PT. Chang Shin Reksa Jaya

Dear Sir/Madam,

My name is Thomas Alpha Edisound, and I would like to apply for a position at PT. Chang Shin Reksa Jaya.
I am confident that I can contribute to supporting the company’s vision and mission. Enclosed are my application documents for your consideration.

I sincerely hope for the opportunity to further discuss my qualifications and to contribute to your esteemed company.

Thank you very much for your attention.

Sincerely,
Thomas Alpha Edisound
```
`email_config.txt` → configuration (recipients, time, timezone, attachments)
`attachments` → place your attachments file

Example email_config.txt:
```
RECEIVERS=example1@gmail.com,example2@gmail.com,example3@gmail.com
SEND_TIME=07:00
TIMEZONE=Asia/Jakarta
ATTACHMENTS=CV.pdf,song.mp3,your naked video.mp4
```

---
## ▶️ Usage
Once everything is configured properly, start the bot with:
```
python bot_email.py
```
If you prefer a simpler way to run, you can run the `auto_start.bat` file provided in the repository.

## 🔄 Update the Script
Update your Script when its availabe:
```
git pull
```
