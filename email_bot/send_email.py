import smtplib
from email.message import EmailMessage
from pathlib import Path

SENDER_EMAIL = "your@gmail.com"
APP_PASSWORD = "abcd efgh ijkl mnop"  #hated this one at first but all ok now
PDF_FILE = "attachment.pdf"
EMAILS_FILE = "emails.txt"
MESSAGE_FILE = "message.txt"

with open(EMAILS_FILE, "r", encoding="utf-8") as f:
    recipients = [line.strip() for line in f if line.strip()]

with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()
    subject = lines[0].strip()
    body = "".join(lines[1:]).strip()

pdf_path = Path(PDF_FILE)
with open(pdf_path, "rb") as f:
    pdf_data = f.read()

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(SENDER_EMAIL, APP_PASSWORD)

    for email in recipients:
        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg["Subject"] = subject
        msg.set_content(body)

        msg.add_attachment(
            pdf_data,
            maintype="application",
            subtype="pdf",
            filename=pdf_path.name
        )

        server.send_message(msg)
        print(f"pookie sent to {email}")

print("all done gang")