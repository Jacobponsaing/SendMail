import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP(host='smtp.live.com', port=587)

server.ehlo()

# not save
# server.login('mail@mail.com', 'password')

with open('password.txt', 'r') as f:
    password = f.read()

server.starttls()
server.login('****@hotmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Jacob'
msg['To'] = '****@gmail.com'
msg['Subject'] = 'Test python file'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'python_image.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('****@hotmail.com', "****@gmail.com", text)
