
# from alchemyapi import AlchemyAPI
import json
import pprint


# alchemyapi = AlchemyAPI()

pp = pprint.PrettyPrinter(indent=4)

# ff8f993db5ee0b907a3e41f19bbd57b8b4cbc24a
pp = pprint.PrettyPrinter(indent=4)

b_not_g = []

with open("cg_entities.csv", "r") as file1:
  graph = file1.read().split('\n')

with open("blog_entities.csv", "r") as file2:  
  blog = file2.read().split('\n')

for i in range(0, len(blog)):
  for j in range(1, len(graph)):
    if blog[i] == graph[j]:
      b_not_g.append(blog[i])
    else:
      continue

bNg_set = set(b_not_g)

for x in bNg_set:
  print x



# g_set = set(graph)
# b_set = set(blog)


# #in blog not in graph
# print list(b_set - g_set)




# 
# n = 1
# while n < len(graph):
#   for x in range(0, len(blog)):
#     if blog[x] == graph[x + n]:
#       both.append(blog[x])
#       n+=1

# for i in graph:
#   if i not in blog:
#     print i



# for b in blog:
#   if b in graph:
#     print b
#   else:
#     continue



#for i in range(0, len(blog)):
  # for j in range(0, len(graph)-1):
  # if blog[i] in graph:
  #   print blog[i]
  # else:
  #   continue



#in graph not in blog
#print list(g_set - b_set)

# #return elements of b_set not in g_set
# diff = b_set.difference(g_set)
# # print diff


  # for j in blog:
  #   if i == j or j == i:
  #     print match


    # for j in blog:
  #   if i == j:
  #     print i


  #lis_1=[line for line in file1]        # create a list of lists



# with open("blog_entities.csv", "r") as file2:
#   lis_2 =  [line for line in file2]

#   for i in lis_1:
#     for j in lis_2:
#       if i == j:
#         print i
#       else:
#         print 'not a match'
# #     graph.append(i)


# with open("blog_entities.csv", "r") as file2:
#   lis_2 =  [line for line in file2]

#   for j in lis_2:
#     blog.append(j)

# # for g in graph:
# #   for b in blog:
# both = set(graph).intersection(blog)
# print both

