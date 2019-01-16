# --------------------------------------------------------------------
#
#	mail_send/views.py
#
#					Jan/15/2019
# --------------------------------------------------------------------
import	sys
import	os

from datetime import datetime
#
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#
from mail_send.lib.mail_smtp import mail_smtp_proc 

# ------------------------------------------------------------------
def index(request):
	message = ""
	message += 'mail_send からのメッセージです。<br />'
	message += str(request.user.id) + '&nbsp;&nbsp;'
	message += request.user.username + '<p />'
	dd = {
		'hour': datetime.now().hour,
		'minute': datetime.now().minute,
		'message': message,
	}
	return render(request, 'mail_send/mail_send.html', dd)
#
# ------------------------------------------------------------------
@csrf_exempt 
def mail_main_proc(request):
	sys.stderr.write("*** mail_main_proc *** start ***\n")
#
	if (request.method == 'POST'):
		flags = None
#
		mail = {}
		mail['server'] = os.environ.get('server')
		mail['port'] = 587
		mail['usr'] = os.environ.get('mail_from')
		mail['password'] = os.environ.get('password')
		mail['from'] = os.environ.get('mail_from')
		mail['to'] = request.POST['mail_to']
		mail['subject'] = request.POST['subject']
		str_message = request.POST['str_message']
		str_message += "*** message ***\n"
		str_message += "mail_from: " + mail['from'] + "\n"
		str_message += "mail_to: " + mail['to'] + "\n"
		str_message += "*** message ***\n"
#
		sys.stderr.write("*** mail_from: " + mail['from'] + "\n")
		sys.stderr.write("mail_to:" + mail['to'] + "\n")
		mail_smtp_proc(mail,str_message)
#
	sys.stderr.write("*** mail_main_proc *** end ***\n")
#
	str_out = "Success"
#
	return HttpResponse(str_out)
# --------------------------------------------------------------------
