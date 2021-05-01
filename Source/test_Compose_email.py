import smtplib, ssl
from email.message import EmailMessage

message = "Please enter your email body here."


def test_send_email():
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "This is a automated mail generated using automation scripts"
    msg["From"] = "*******@gmail.com"             #Enter your email id
    msg["To"] = "******@outlook.com"       #Enter to address

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], "SS_automation")
        smtp.send_message(msg)
        smtp.quit()