# -*- coding: utf-8 -*-
#
#	mail_send/lib/mail_smtp.py
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
def mail_smtp_proc(mail,content):

	message = MIMEText (
		content,
		'plain',
		)

	message['Subject'] = mail['subject']
	message['From'] = mail['from']
	message['To'] = mail['to']
	message['Date'] = formatdate()
#
	send_mail_proc(mail,message)
#
# --------------------------------------------------------------------
