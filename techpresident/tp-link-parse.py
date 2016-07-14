import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re


#get contents of Tech President's archives
base_url = "http://techpresident.com/blog"

r = rq.get(base_url)
soup = bsoup(r.text, "lxml")

page_count_links = soup.find_all("a",href=re.compile(r".*javascript:goToPage.*"))
try: # Make sure there are more than one page, otherwise, set to 1.
    num_pages = int(page_count_links[-1].get_text())
except IndexError:
    num_pages = 357 #1411 pages #1071 / 3 = 357

url_list = ["{}?page={}".format(base_url, str(page + 1054)) for page in range(1, num_pages + 1)]
#340 + 357 = 697
#697 + 357 = 1054

#url_list.remove("http://techpresident.com/blog?page=1") <- actual page - don't remove
# url_list.insert(0, "http://techpresident.com/blog")

article_links = []
# loop through p. 341 ~ 1411 and grab partial article links
for url in url_list:
  html_doc = urllib2.urlopen(url).read()
  soup = BeautifulSoup(html_doc, "lxml")
  contents = soup.findAll('div', attrs={"class": " technewsfeat-wrapper boxshadow"})
  
  #grab inner html with partial links
  for c in contents: #10 article links per page
    # c = str(c)
    piece = c.find('h4')
    piece = str(piece)

    #grab partial links
    start = piece.find("/") #index of this
    end = piece.find('">')
    #inner = piece[start:end]

    #construct full links
    full_link = "http://techpresident.com" + piece[start:end]
    
    article_links.append(full_link)

# print article_links

#write article urls to textfile
with open("techpres_links.txt", "w") as outfile:
  for x in article_links:
    outfile.write(x + '\n')


#bad code - delete
# base_url = "http://techpresident.com/topics/"
# r = rq.get(base_url)
# soup = bsoup(r.text, "lxml")

# topics = ['revolution', 'obama-2012', 'malcolm-gladwell',
#           'hacktivism', 'facebook', 'online-organizing',
#           'wegov', 'backchannel', 'civic-hacking'] 

# morelinks = ['http://techpresident.com/techpresident-topics/debates-20',
#               'http://techpresident.com/techpresident-topics/hip-or-hype',
#               'http://techpresident.com/techpresident-topics/grassrootsiness',
#               'http://techpresident.com/techpresident-topics/email-watch',
#               'http://techpresident.com/techpresident-topics/blogging',
#               'http://techpresident.com/techpresident-topics/occupywallst',
#               'http://techpresident.com/techpresident-topics/gop-2012',
#               'http://techpresident.com/techpresident-topics/design']

# links = []
# for t in topics:
#   url = base_url + t
#   links.append(url)

# for m in morelinks:
#   links.append(m)

# i = 0
# for l in links:
#   html_doc = urllib2.urlopen(l).read()

#   fname = 'topicpage_' + str(i)
#   i += 1

#   with open(fname, "w") as html_file:
#     html_file.write(html_doc)



# contents = soup.findAll('div', attrs={"id": "topic-background"})
# print contents
