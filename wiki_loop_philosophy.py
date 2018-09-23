import requests
import re
import time
import sys
from bs4 import BeautifulSoup

utf = 'utf-8'

#regexList
insideParentheses = r'\(.*?\)'
getATag = r'<a.*?</a>'
getWikiLink = r'/wiki/(.*?)"'


def getContent(url):
	r"""
	Return the first link on a certain wikipedia link

	1. get the request from url parameter
	2. find the main body of the article
	3. remove some irrelevant classes and ids
	"""

	html = requests.get(url).text
	soup = BeautifulSoup(html, features='html5lib')
	
	content = soup.find(id='mw-content-text')

	irrelevantClasses = ['ambox', 'dablink', 'geography', 'infobox', 'metadata',
			'thumb', 'toc', 'right', 'vcard', 'vertical-navbox', 'nowraplinks',
			'collapsible', 'collapsed', 'toccolours', 'biota', 'infobox_v2', 
			'navbox-inner', 'NavHead', 'NavContent', 'mw-empty-elt', 'quotebox']
	irrelevantIDs = ['coordinates']

	for c in content.find_all(class_=irrelevantClasses): 
		c.replace_with('')

	for c in content.find_all(id=irrelevantIDs):
		c.replace_with('')

	return content

def findFirstLink(tag):
	r"""
	Find the first link of a BeautifulSoup HTML tag object
	Requirements are:
	1. from the main page article, not in a box
	2. blue (red is for non-existing articles)
	3. not in parentheses, not italic, and not a footnote
	"""

	#remove all irrelevant tags and classes
	irrelevantTags = ['i', 'sup', 'img', 'b', 'strong', 'small', '[title="Help:Pronunciation respelling key"]']
	for t in tag.find_all(irrelevantTags):
		t.replace_with('')

	irrelevantClasses = ['new', 'nowrap', 'extiw', 'IPA', 
			'unicode', 'external']
	for t in tag.find_all(class_=irrelevantClasses):
		t.replace_with('')

	#remove all <a> tags inside of parentheses
	tagText = str(tag)
	textInParentheses = re.findall(insideParentheses, tagText)
	for t in textInParentheses:
		aTags = re.findall(getATag, t)

		#removing all of these a tags 
		for a in aTags: 
			tagText = tagText.replace(a, '')

	allWikiLinks = re.findall(getWikiLink, tagText)

	if len(allWikiLinks) == 0:
		return None 

	return allWikiLinks[0]

def createWikipediaLink(topic):
	return 'https://en.wikipedia.org/wiki/%s' % topic

#add some exceptions
class MaxLoopError(BaseException):
	#maximum number of loop has been reached
	pass

class InfiniteLoopError(BaseException):
	#infinite loop between 2 articles has been triggered
	pass

class NoLinkError(BaseException):
	#no legitimate link was found in the url
	pass


if __name__ == '__main__':
	#try getting starting topic from argv
	#if none stated then use random one
	try:
		url = sys.argv[1]
	except:
		url = createWikipediaLink('Special:Random')

	#set a history to indicate a loop
	history=[]

	#set max loop with default value 100
	try:
		maxLoop = int(sys.argv[2])
	except:
		maxLoop = 100

	curLoop = 0

	r"""
	loop until one of this conditions is fulfilled:
	1. next url is the philosophy page
	2. max loop number has been reached
	3. next url is already in the history
	4. there isn't any link found in the main article
	"""
	while url != 'https://en.wikipedia.org/wiki/Philosophy':
		time.sleep(.500)
		if curLoop >= maxLoop:
			raise MaxLoopError('Max loop: {}'.format(maxLoop))
		curLoop += 1

		content = getContent(url)
		mainContent = content.find_all(['p', 'ul'])

		for cnt in mainContent:
			firstLink = findFirstLink(cnt)

			if not firstLink is None:
				#print(firstLink)
				sys.stdout.write('%s\n' % firstLink)
				sys.stdout.flush()
				url = createWikipediaLink(firstLink)
				if url in history:
					raise InfiniteLoopError('URL has been already visited before')
				history.append(url)
				break

		if firstLink is None:
			raise NoLinkError('No new link found')

	print("Philosophy page has been reached!")