from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	neededata = False

	def handle_starttag(self, tag, attrs):
		if tag == 'td' or tag == 'th':
			self.neededata = True
			# print "Encountered a start tag:", tag


	def handle_data(self, data):
		if self.neededata and data != '-':
			print data
			self.neededata = False

parser = MyHTMLParser()
f = open('./result/match0-top.html', 'r')
parser.feed(f.read())
