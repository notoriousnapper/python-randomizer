#!/usr/bin/python
import webbrowser
import random
import sys
import pyfiglet

# Return random list item
def get_random_list_item(l):
  max_len = len(l)
  return l[random.randrange(0, max_len)]


# Code Begins
ascii_banner = pyfiglet.figlet_format("Hello Jesse!!")
ascii_banner_heading = pyfiglet.figlet_format("==========")
print ascii_banner + ascii_banner_heading

#random.seed(a=None, version=2) #Anything like a string
if len(sys.argv) < 2 :
  print 'Require one more argument for filepath'
else: 
  file_name = sys.argv[1]

  # Using readlines() 
  file = open(file_name, 'r') 
  lines = file.readlines() 

  list_item = get_random_list_item(lines)
  banner = pyfiglet.figlet_format(list_item)
  print banner
  
  # TODO: random chance of things happening function
  #print(random.randrange(100)) # print a random number from 0 to 99
  #num = random.randrange(100)
  #if (num > 50):
  #  webbrowser.open('http://net-informations.com', new=2)

