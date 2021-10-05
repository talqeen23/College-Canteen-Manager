from pitho import app
from flask_mail import Mail,Message
mail=Mail(app)
app.config['MIAL_SERVER']="smtp.gmail.com"
app.config['MAIL_PORT']="587"
app.config['MAIL_USERNAME']="talqeen987@gmail"
app.config['MAIL_PASSWORD']="8561028556"
app.config['MAIL_USED_TLS']=True
app.config['MAIL_USE_SSL']=False
def mailer(subject,message,reciever):
	msg=Message(subject,sender="talqeen987@gmail.com",recipients=[reciever])
	msg.body=message
	mail.send(msg)
	return True
	