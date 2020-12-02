import smtplib
from os import getenv

port = 465
server = 'saturn.kreativmedia.ch'
password = getenv('MAIL_PASSWORD')
login = getenv('MAIL_LOGIN')

def send(address):
    with smtplib.SMTP(server, port) as s:
        s.login(login, password)
        s.sendmail(login, address, 'You real?')
        s.close()
