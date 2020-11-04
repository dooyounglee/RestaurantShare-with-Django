from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def sendEmail(request):
	checked_res_list = request.POST.getlist('checks')
	inputReceiver = request.POST['inputReceiver']
	inputTitle = request.POST['inputTitle']
	inputContent = request.POST['inputContent']
	
	restaurants = []
	for checked_res_id in checked_res_list:
		restaurants.append(Restaurant.objects.get(id = checked_res_id))
	content = {'inputContent': inputContent, 'restaurants':restaurants}
	msg_html = render_to_string('sendEmail/email_format.html', content)
	msg = EmailMessage(subject = inputTitle, body=msg_html, from_email="gostbaducking0@gmail.com",bcc=inputReceiver.split(','))
	msg.content_subtype = 'html'
	msg.send()
	
	"""mail_html = "<html><body>1</body></html>"
	
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login("gostbaducking0@gmail.com","skfktkfkd220@@)")
	
	msg = MIMEMultipart('alternative')
	msg['Subject'] = inputTitle
	msg['From'] = 'gostbaducking0@gmail.com'
	msg['To'] = inputReceiver
	mail_html = MIMEText(mail_html,'html')
	msg.attach(mail_html)
	server.sendmail(msg['From'],msg['To'].split(','),msg.as_string())
	server.quit()"""
	return HttpResponseRedirect(reverse('index'))