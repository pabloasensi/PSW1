from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	neededata = False
	counter = 0

	def handle_starttag(self, tag, attrs):
		if tag == 'th':
			self.counter += 1
			# print "Encountered a start tag:", tag


	def handle_data(self, data):
		if self.counter == 2:
			print data
			print " <->"
		if self.counter == 3:
			print data

parser = MyHTMLParser()
f = open('./result/match0-top.html', 'r')
print '\n'
parser.feed(f.read())
