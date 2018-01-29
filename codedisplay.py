from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	neededata = False

	def handle_starttag(self, tag, attrs):
		if tag == 'font':
			self.neededata = True
			print 'Encountered code similarity: '
			# print "Encountered a start tag:", tag

	def handle_endtag(self, tag):
		if tag == 'font':
			self.neededata = False
	# print "Encountered an end tag :", tag

	def handle_data(self, data):
		if self.neededata:
			print data


parser = MyHTMLParser()
f = open('./result/match0-0.html', 'r')
parser.feed(f.read())
