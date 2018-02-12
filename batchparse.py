from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	neededata = False
	avsim = False

	def handle_starttag(self, tag, attrs):
		if tag == 'td' and self.avsim:
			self.neededata = True
			# print "Encountered a start tag:", tag

	def handle_endtag(self, tag):
		if tag == 'td' and self.avsim:
			self.neededata = False
		if tag == 'tr' and self.avsim:
			print '\n'
		
	# print "Encountered an end tag :", tag

	def handle_data(self, data):
		if data == 'Matches sorted by maximum similarity (':
			print 'Matches sorted by maximum similarity \n'
			self.avsim = True
		if self.neededata:
			if data == '-&gt':
				print '-\>'
			else:
				print data


parser = MyHTMLParser()
f = open('./result/index.html', 'r')
parser.feed(f.read())
