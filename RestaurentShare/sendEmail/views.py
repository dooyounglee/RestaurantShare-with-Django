from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def sendEmail(request):
	checked_res_list = request.POST['checks']
	inputReceiver = request.POST['inputReceiver']
	inputTitle = request.POST['inputTitle']
	inputContent = request.POST['inputContent']
	
	mail_html = "<html><body>1</body></html>"
	
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login("gostbaducking0@gmail.com","비밀")
	
	msg = MIMEMultipart('alternative')
	msg['Subject'] = inputTitle
	msg['From'] = 'gostbaducking0@gmail.com'
	msg['To'] = inputReceiver
	mail_html = MIMEText(mail_html,'html')
	msg.attach(mail_html)
	server.sendmail(msg['From'],msg['To'].split(','),msg.as_string())
	server.quit()
	return HttpResponseRedirect(reverse('index'))