# -*- coding: utf-8 -*-
#
#	send_mail.py
#
#						May/20/2017
# --------------------------------------------------------------------
import	sys
import	socket
import	smtplib
import	email
from email.mime.text import MIMEText
from email.utils import formatdate
# --------------------------------------------------------------------
# [6]:
def send_mail_proc (mail,message):
	if (mail['port'] == 465):
		try:
			send_ssl (mail,message)
		except Exception as ee:
			sys.stderr.write ("*** error *** send_ssl ***\n")
			sys.stderr.write (str (ee) + "\n")
	elif (0 <= mail['server'].find ('plala.or.jp')):
		try:
			send_plain (mail,message)
		except Exception as ee:
			sys.stderr.write ("*** error *** send_plain ***\n")
			sys.stderr.write (str (ee) + "\n")
	else:
		send_mail_proc_s2 (mail,message)
#
# --------------------------------------------------------------------
# [6-2]:
def send_ssl (mail,message):
	ss = smtplib.SMTP_SSL (mail['server'],mail['port'])
	ss.ehlo ()
#	ss.starttls ()
	ss.ehlo ()
	ss.login (mail['usr'],mail['password'])
	ss.sendmail (
		mail['from'],
		[mail['to']],
		message.as_string (),
		)
	ss.close ()
#
# --------------------------------------------------------------------
# [6-4]:
def send_starttls (mail,message):
	ss = smtplib.SMTP (mail['server'],mail['port'])
	ss.ehlo ()
	ss.starttls ()
	ss.ehlo ()
	ss.login (mail['usr'],mail['password'])
	ss.sendmail (
		mail['from'],
		[mail['to']],
		message.as_string (),
		)
	ss.close ()
#
# --------------------------------------------------------------------
# [6-2]:
def send_mail_proc_s2 (mail,message):
	try:
		send_starttls (mail,message)
	except Exception as ee:
		sys.stderr.write ("*** error *** send_starttls ***\n")
		sys.stderr.write (str (ee) + "\n")
		try:
			send_plain (mail,message)
		except Exception as ee:
			sys.stderr.write ("*** error *** send_plain ***\n")
			sys.stderr.write (str (ee) + "\n")
			sys.stderr.write ("*** error *** send_plain ***\n")
			try:
				send_simple (mail,message)
			except Exception as ee:
				sys.stderr.write ("*** error *** send_simple ***\n")
				sys.stderr.write (str (ee) + "\n")
#
# --------------------------------------------------------------------
# [6-6]:
def send_plain (mail,message):
	sys.stderr.write ("*** send_plain *** start ***\n")
	ss = smtplib.SMTP (mail['server'],mail['port'])
	ss.ehlo ()
#	ss.starttls ()
#	ss.ehlo ()
	sys.stderr.write ("*** send_plain *** bbb ***\n")
	ss.login (mail['usr'],mail['password'])
	sys.stderr.write ("*** send_plain *** ccc ***\n")
	ss.sendmail (
		mail['from'],
		[mail['to']],
		message.as_string (),
		)
	ss.close ()
#
# --------------------------------------------------------------------
# [6-8]:
def send_simple (mail,message):
	sys.stderr.write ("*** send_simple *** start ***\n")
	ss = smtplib.SMTP (mail['server'],mail['port'])
#
	ss.sendmail (
		mail['from'],
		[mail['to']],
		message.as_string (),
		)

	ss.close ()
#
	sys.stderr.write ("*** send_simple *** end ***\n")
# --------------------------------------------------------------------
