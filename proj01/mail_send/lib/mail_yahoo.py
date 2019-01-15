# -*- coding: utf-8 -*-
#
#	lib/mail_yahoo.py
#
#						Jan/15/2019
# --------------------------------------------------------------------
import	sys
import	email
from email.mime.text import MIMEText
from email.utils import formatdate
# --------------------------------------------------------------------
from mail_send.lib.send_mail import send_mail_proc
# --------------------------------------------------------------------
def mail_yahoo_proc(server,mail_from,password,mail_to,subject,content):
	mail = {}
	mail['server'] = server
	mail['port'] = 587
	mail['usr'] = mail_from
	mail['password'] = password
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
