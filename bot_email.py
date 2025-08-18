import smtplib
import schedule
import time
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
import pytz
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console

# import banner
from banner_utils import show_banner

console = Console()

# Load .env
load_dotenv()
sender_email = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")

# --- Email helper functions ---
def load_email_content():
    subject, body = "No Subject", "No Body"
    try:
        with open("email_subject.txt", "r", encoding="utf-8") as f:
            subject = f.read().strip()
    except: pass
    try:
        with open("email_body.txt", "r", encoding="utf-8") as f:
            body = f.read()
    except: pass
    return subject, body

def load_config():
    receivers, send_time, timezone, attachments = [], "07:20", "Asia/Jakarta", []
    try:
        with open("email_config.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "#" in line:
                    line = line.split("#")[0].strip()
                if line.startswith("RECEIVERS="):
                    receivers = [r.strip() for r in line.split("=")[1].split(",") if r.strip()]
                elif line.startswith("SEND_TIME="):
                    send_time = line.split("=")[1].strip()
                elif line.startswith("TIMEZONE="):
                    timezone = line.split("=")[1].strip()
                elif line.startswith("ATTACHMENTS="):
                    attachments = [a.strip() for a in line.split("=")[1].split(",") if a.strip()]
    except: pass
    return receivers, send_time, timezone, attachments

def send_email():
    subject, body = load_email_content()
    receivers, _, _, attachments = load_config()

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = ", ".join(receivers)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    attachments_folder = os.path.join(os.getcwd(), "attachments")
    for file in attachments:
        file_path = os.path.join(attachments_folder, file)
        if os.path.exists(file_path):
            try:
                with open(file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={file}")
                    msg.attach(part)
            except Exception as e:
                console.print(f"[red]Failed to attach {file}: {e}[/red]")
        else:
            console.print(f"[yellow]⚠️ File {file} not found in attachments folder![/yellow]")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receivers, msg.as_string())
        server.quit()
        console.print(f"[green][{datetime.now()}] ✅ Email sent to {', '.join(receivers)}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to send email: {e}[/red]")

# --- Setup ---
receivers, send_time, timezone, attachments = load_config()
local_tz = pytz.timezone(timezone)
now = datetime.now(local_tz)
send_hour, send_minute = map(int, send_time.split(":"))
target = now.replace(hour=send_hour, minute=send_minute, second=0, microsecond=0)
if now > target:
    target = target + timedelta(days=1)

schedule.every().day.at(send_time).do(send_email)

# --- Banner (pakai banner_utils) ---
show_banner(send_time, timezone, title="📧 Auto Email Sender")

# --- Countdown loop ---
while True:
    now = datetime.now(local_tz)
    if now > target:
        target = target + timedelta(days=1)

    delta = target - now
    total_seconds = delta.seconds
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    with Progress(
        TextColumn("⏳ Countdown:"),
        BarColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(f"{hours:02d}:{minutes:02d}:{seconds:02d}", total=total_seconds)
        while total_seconds > 0:
            time.sleep(1)
            total_seconds -= 1
            progress.update(task, advance=1)
            if total_seconds == 0:
                break

    schedule.run_pending()
