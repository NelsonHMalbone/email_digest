import smtplib
import ssl
import config

def send_email_script(message):
    host = 'smtp.gmail.com'
    port = 465

    username = config.username
    api_password = config.app_password

    reciever = 'malbonenelson@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, api_password)
        server.sendmail(username, reciever, message)
