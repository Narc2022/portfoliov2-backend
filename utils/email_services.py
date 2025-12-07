import smtplib
from email.mime.text import MIMEText


def send_reset_email(to_email:str, reset_link:str):
    msg = MIMEText(f"Click the following link to reset your password: {reset_link}")
    msg['subject'] = 'Password Reset Request'
    msg['from'] = 'noreply@example.com'
    msg['to'] = to_email
    
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login("your_email@gmail,com","your_password")
        server.send_message(msg)