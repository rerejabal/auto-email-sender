import smtplib
import schedule
import time
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from art import text2art
from dotenv import load_dotenv
import os
import pytz
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.panel import Panel

console = Console()

# Load .env
load_dotenv()
pengirim_email = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")

# Fungsi baca subject & body
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

# Fungsi baca config
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

# Fungsi kirim email
def kirim_email():
    subject, body = load_email_content()
    receivers, _, _, attachments = load_config()

    msg = MIMEMultipart()
    msg["From"] = pengirim_email
    msg["To"] = ", ".join(receivers)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Folder lampiran
    attachments_folder = os.path.join(os.getcwd(), "attachments")

    # Tambahkan lampiran
    for file in attachments:
        lokasi_file = os.path.join(attachments_folder, file)
        if os.path.exists(lokasi_file):
            try:
                with open(lokasi_file, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={file}")
                    msg.attach(part)
            except Exception as e:
                console.print(f"[red]Gagal melampirkan {file}: {e}[/red]")
        else:
            console.print(f"[yellow]⚠️ File {file} tidak ditemukan di folder attachments![/yellow]")

    # Kirim email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(pengirim_email, password)
        server.sendmail(pengirim_email, receivers, msg.as_string())
        server.quit()
        console.print(f"[green][{datetime.now()}] ✅ Email successfully sent to {', '.join(receivers)}[/green]")
    except Exception as e:
        console.print(f"[red]Gagal mengirim email: {e}[/red]")

# Baca config
receivers, send_time, timezone, attachments = load_config()

# Setup timezone & target
local_tz = pytz.timezone(timezone)
now = datetime.now(local_tz)
send_hour, send_minute = map(int, send_time.split(":"))
target = now.replace(hour=send_hour, minute=send_minute, second=0, microsecond=0)
if now > target:
    target = target + timedelta(days=1)

schedule.every().day.at(send_time).do(kirim_email)

# Banner
banner = text2art("MYSTIC  BOT  SCRIPT", font="small")
console.print(Panel(banner, title="📧 Auto Email Sender", style="bold magenta"))
console.print(f"[cyan]by rerejabal[/cyan]\n")
console.print(f"[yellow]Email will be automatically sent at: {send_time} ({timezone}).[/yellow]\n")

# Loop dengan progress bar countdown
while True:
    now = datetime.now(local_tz)
    if now > target:
        target = target + timedelta(days=1)

    selisih = target - now
    total_detik = selisih.seconds
    jam, sisa = divmod(total_detik, 3600)
    menit, detik = divmod(sisa, 60)

    with Progress(
        TextColumn("⏳ [progress.description]{task.description}"),
        BarColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(f"Countdown {jam:02d}:{menit:02d}:{detik:02d}", total=total_detik)
        while total_detik > 0:
            time.sleep(1)
            total_detik -= 1
            progress.update(task, advance=1)
            if total_detik == 0:
                break

    schedule.run_pending()
