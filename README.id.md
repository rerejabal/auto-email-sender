```markdown
# Auto Email Sender

Sebuah alat sederhana untuk mengirim email otomatis - jadwalkan dan kirim ke banyak penerima dengan mudah.

---

## ✨ Fitur
- Penjadwalan email harian otomatis
- Mendukung banyak penerima
- Subjek & isi email dari file teks
- Bisa melampirkan banyak file
- Dukungan zona waktu
  
---

## 📦 Kebutuhan
- Python 3.8+ (pastikan sudah terpasang)
- pip (pengelola paket Python)
- Akun email yang mendukung SMTP (Gmail, Outlook, Yahoo, dll.)
- Library yang dibutuhkan:
  - schedule  
  - art  
  - python-dotenv  
  - pytz  
  - rich  

---

## 📁 Struktur Folder
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
 │   ├─ File Anda 1
 │   ├─ File Anda 2
 │   └─ ...

---

## ⚙️ Persiapan
> Klik kanan pada lokasi folder yang diinginkan, lalu pilih **Open in Terminal / PowerShell / Command Prompt**.

### 1. Clone repository ini di Terminal / PowerShell / Command Prompt:
git clone https://github.com/rerejabal/auto-email-sender.git
cd auto-email-sender

### 2. Instal dependensi:
pip install -r requirements.txt

### 3. Siapkan file Anda:
Ubah file `.env` dengan kredensial email Anda:

⚠️ Gmail memerlukan App Password (bukan password biasa).  
Buat melalui Google Account → Security → App passwords.  
Jika tidak ada, cari: *App Password*.  
Contoh App Password: kjgwxutxzhkyqjkw

EMAIL_SENDER=youremail@gmail.com  
EMAIL_PASSWORD=yourapppassword  

`email_subject.txt` → subjek email  
Contoh:
Lamaran Kerja

`email_body.txt` → isi email  
Contoh:
Kepada: HR Department  
PT. Chang Shin Reksa Jaya  

Dengan hormat,  

Nama saya Thomas Alpha Edisound, dan saya ingin melamar pekerjaan di PT. Chang Shin Reksa Jaya.  
Saya yakin dapat berkontribusi dalam mendukung visi dan misi perusahaan. Bersama ini saya lampirkan dokumen lamaran untuk dipertimbangkan.  

Saya sangat berharap mendapat kesempatan untuk berdiskusi lebih lanjut mengenai kualifikasi saya dan dapat berkontribusi di perusahaan Bapak/Ibu.  

Terima kasih atas perhatian Bapak/Ibu.  

Hormat saya,  
Thomas Alpha Edisound  

`email_config.txt` → konfigurasi (penerima, waktu, zona waktu, lampiran)  
`attachments` → tempat file lampiran  

Contoh email_config.txt:
RECEIVERS=contoh1@gmail.com,contoh2@gmail.com,contoh3@gmail.com  
SEND_TIME=07:00  
TIMEZONE=Asia/Jakarta  
ATTACHMENTS=CV.pdf,song.mp3,video_pribadi.mp4  

---

## ▶️ Cara Menjalankan
Jika semua sudah dikonfigurasi dengan benar, jalankan bot dengan:
python bot_email.py

Jika ingin lebih mudah, cukup jalankan file `auto_start.bat` yang sudah tersedia.

---

## 🔄 Update Script
Perbarui script jika tersedia versi baru:
git pull
```
