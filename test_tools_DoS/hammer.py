import urllib2

print """\
           _
         ./ |   
         /  /   
       /'  /   
      /   /   
     /    \     
    |      `
    |        |                                ___________________
    |        |___________________...-------'''- - -  =- - =  - = `.
   /|        |                   \-  =  = -  -= - =  - =-   =  - =|
  ( |        |                    |= -= - = - = - = - =--= = - = =|
   \|        |___________________/- = - -= =_- =_-=_- -=_=-=_=_= -|
    |        |                   ```-------...___________________.'
    |________|      
      \    /                                       
      |    |                              
    ,-'    `-,       
    |        |       
    `--------'

"""
print 'Please enter in the port that the server is being run on:'
input_port = int(raw_input())
print 'Please enter in the page you would like to hammer: \n e.g. /files'
input_path = raw_input()
num = 0 
while True:
	num = num +1
	urllib2.urlopen("http://localhost:" + str(input_port) + input_path).read()
	print "GET Requests: \n", num

