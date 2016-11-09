# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
 
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup
import re

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)						#requests Beautiful Soup output of html code of webpage
soup = BeautifulSoup(r.text, "html.parser")		#assigns to variable soup

text=soup('p')
l=[]
for x in text:
	s=re.findall('.*student.*',str(x))
	for a in s:
		l.append(a)
print (l)
