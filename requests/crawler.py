import requests
from HTMLParser import HTMLParser
import time
import ssl, socket

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
        	if 'href' in attr and 'javascript:show' not in attr[1]:
        		if not any(attr[1] in s for s in checkedArray):
        			if 'http' not in attr[1]:
        				urlArray.append(homeURL+attr[1])
        			else:
        				urlArray.append(attr[1])
        #print "Encountered a start tag:", tag
    #def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
    def handle_data(self, data):
        if "Droessler" in data:
        	print data

urlArray = []
checkedArray = []

pagecount = 0
uwecPageCount = 0
parser = MyHTMLParser()

homeURL = 'http://www.uwec.edu/'
urlArray.append(homeURL)

totalTime=0


while len(urlArray) > 0 and pagecount < 1000:
	#print urlArray[0]
	if 'uwec.edu' in urlArray[0]:
		uwecPageCount+=1

	start = time.time()
	try:
		r = requests.get(urlArray[0], timeout=0.5)
	except (requests.exceptions.ConnectionError, requests.exceptions.InvalidSchema, requests.exceptions.Timeout, ssl.SSLError, socket.timeout):
		pass
	end = time.time()

	totalTime+=(end - start)
	pagecount+=1

	checkedArray.append(urlArray[0])
	urlArray.pop(0)
	
	try:
		parser.feed(r.text)
	except HTMLParser.HTMLParseError:
		pass


print uwecPageCount
print pagecount
print ("Average time: " + str(totalTime / pagecount))
print checkedArray
