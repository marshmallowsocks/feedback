import os
import random
import mechanize

def login(login,passwd):
	
	html = br.open('http://202.129.209.5:7766/liteqbmsce')
	br.form = list(br.forms())[0]

	br['login'] = login
	br['password'] = passwd
	
	br.submit()
	
def getAgreeScreen():
	
	br.form = list(br.forms())[0]	
	
	br.submit()

def getPasswdChangeScreen(usn,email,passwd):

	br.form = list(br.forms())[0]

	br['oldpass'] = usn
	br['newpass1'] = passwd	
	br['newpass2'] = passwd
	br['email1'] = email
	br['email2'] = email

	response = br.submit()

	print response.geturl()

def getFeedbackScreen():
	
	linkArr = [ link for link in br.links()	]

	linkArr = linkArr[2:]

	for link in linkArr:
		
		link.url = 'http://202.129.209.5:7766/liteqbmsce/' + link.url		

		print link.url		

		request = br.click_link(link)
		response = br.follow_link(link)

		submitFeedback() #works!

def submitFeedback():

	br.form = list(br.forms())[0]
		
	for control in br.form.controls:
		 if control.type == 'radio':
			control.value = [random.choice('353555')]

	br.submit()	

def main():
	
		print "Welcome to automatic feedback generator! This program requires that you enter your USN, email address, and a new password for your account, and then it automatically submits feedback for you. Why waste 5 minutes lying when you can get a program to do it for you? ;) "		

		usn = raw_input('Enter you usn:')
		email = raw_input('Enter your email id:')
		passwd = raw_input('Enter the password to change it to:')		
		
		login(usn,usn) #Works!
		getAgreeScreen() #Works!		
		getPasswdChangeScreen(usn,email,passwd) #Works!		
		getFeedbackScreen() #works!
	

if __name__ == '__main__':
		
	br = mechanize.Browser()
	os.environ['http_proxy'] = ''	
	
	main()

