# -*- coding: utf-8 -*-
#
#	mail_yahoo.py
#
#						Dec/28/2018
# --------------------------------------------------------------------
import	sys
import	email
from email.mime.text import MIMEText
from email.utils import formatdate
# --------------------------------------------------------------------
from mail_send.lib.send_mail import send_mail_proc
# --------------------------------------------------------------------
def mail_yahoo_proc(mail_from,mail_to,subject,content):
	mail = {}
	mail['server'] = 'smtp.mail.yahoo.co.jp'
	mail['port'] = 587
	mail['usr'] = mail_from
	mail['password'] = 'esp789yy'
	mail['from'] = mail_from
	mail['to'] = mail_to

	message = MIMEText (
		content,
		'plain',
		)

	message['Subject'] = subject
	message['From'] = mail_from
	message['To'] = mail_to
	message['Date'] = formatdate()
#
	send_mail_proc(mail,message)
#
# --------------------------------------------------------------------
