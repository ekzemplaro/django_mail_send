# --------------------------------------------------------------------
import	sys
import	os

from datetime import datetime
#
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#
from mail_send.lib.mail_yahoo import mail_yahoo_proc 

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
		server = os.environ.get('server')
		mail_from = os.environ.get('mail_from')
		password = os.environ.get('password')
		mail_to = request.POST['mail_to']
		subject = request.POST['subject']
		str_message = request.POST['str_message']
		str_message += "*** message ***\n"
		str_message += "mail_from: " + mail_from + "\n"
		str_message += "mail_to: " + mail_to + "\n"
		str_message += "*** message ***\n"
#
		sys.stderr.write("*** mail_from: " + mail_from + "\n")
		sys.stderr.write("mail_to:" + mail_to + "\n")
		mail_yahoo_proc(server,mail_from,password,mail_to,subject,str_message)
#
	sys.stderr.write("*** mail_main_proc *** end ***\n")
#
	str_out = "Success"
#
	return HttpResponse(str_out)
# --------------------------------------------------------------------
