from alchemyapi import AlchemyAPI
import json
import pprint


alchemyapi = AlchemyAPI()


# ff8f993db5ee0b907a3e41f19bbd57b8b4cbc24a
pp = pprint.PrettyPrinter(indent=4)

    
myText = ""
with open("cg_partial.csv", "r") as file:
  data = file.read()
  myText = data.split()
  print type(myText)
  print myText

  for i,x in enumerate(lis):              #print the list items 
    print 



    # #print "line{0} = {1}".format(i,x)
    # #print "{1}".format(i,x)
    # names = x.split(',', 2)[0]
    # entities.append(x)
#categorize entities in Civic Graph based on their descriptions (data = 'text')
  for i in range(0, len(lis)):
    categ_result = alchemyapi.category('text', entities[i]);
    pp.pprint(categ_result)
    i += 1

categ_result = alchemyapi.category('text', "http://techpresident.com/news/25496/first-post-data-driven");
pp.pprint(categ_result['category'])






