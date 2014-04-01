import requests
import ssl, socket, time
import smtplib

found = False
num = 0

def hunt():
 	global num
	num = input('Enter the episode to watch for: ')
	episode = 'Archer Season 5 Episode ' + str(num)

	global parser
	global found
	homeURL = 'http://www.free-tv-video-online.me/internet/archer/season_5.html'

	while found is False:
		try:
			r = requests.get(homeURL)
		except (requests.exceptions.ConnectionError, requests.exceptions.InvalidSchema, requests.exceptions.Timeout, ssl.SSLError, socket.timeout):
			pass
		
		if r.text.find(episode) is not -1:
			print r.text.find(episode)
			print episode
			found = True
		else:
			print "30 second sleep"
			time.sleep(30)

def mail():
	if found is True:
		server = smtplib.SMTP( "smtp.gmail.com", 587 )
		server.starttls()
		server.login( 'email', 'pwd' )
		server.sendmail( 'from', 'to', 'There is a link up for Archer, Episode ' + str(num) )


if __name__ == "__main__":
    hunt()
    mail()
