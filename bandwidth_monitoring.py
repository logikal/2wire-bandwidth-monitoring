#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import re
import sys

mech = Browser()
url = "http://192.168.1.254/xslt?PAGE=C_1_0"

try:
        page = mech.open(url)
except:
        print "Network NOT OK: Unable to reach 2wire gateway. Check the 'url' variable in the script|"
        sys.exit(2)

html = page.read()

soup = BeautifulSoup(html)

# From django's strip_html function:
# https://code.djangoproject.com/browser/django/trunk/django/utils/html.py
def strip_tags(value):
        return re.sub(r'<[^>]*?>', '', value)

transmit_bytes = strip_tags(str(soup.find(text='Transmit').findNext('td')))
receive_bytes =  strip_tags(str(soup.find(text='Receive').findNext('td')))

print "Network OK | transmit_bytes=" + transmit_bytes + "B receive_bytes=" + receive_bytes + "B"