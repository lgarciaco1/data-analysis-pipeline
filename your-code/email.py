import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import email
import email.mime.application
 
 
#html to include in the body section
html = """
 
Dear, 
 
This is my final report.
 
 
Best Regards,"""
 
# Creating message.
msg = MIMEMultipart('alternative')
msg['Subject'] = "My Final ppt report"
msg['From'] = "lcobaleda1@gmail.com"
msg['To'] = "deliaclarramirez@gmail.com"
 
# The MIME types for text/html
HTML_Contents = MIMEText(html, 'html')
 
# Adding pptx file attachment
filename='Proyecto.pdf'
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
 
# Attachment and HTML to body message.
msg.attach(attach)
msg.attach(HTML_Contents)
 
 
# Your SMTP server information
s_information = smtplib.SMTP()
#You can also use SSL
#smtplib.SMTP_SSL([host[, port[, local_hostname[, keyfile[, certfile[, timeout]]]]]])
s_information.connect('localhost')
#s_information.login('UserName','Your Password')
s_information.sendmail(msg['From'], msg['To'], msg.as_string())
s_information.quit()


