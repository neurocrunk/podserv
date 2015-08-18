# Simple Point of Presence Server/App

Why would I want to use your hacky code?! :

 * It's pretty - Bootstrap ftw
 * Memory usage sits @ around 10-15MB 
 * Extensible - Use the Autoindex extension to prettily present a directory of your choice
 
 * Survives a DoS - Thoroughly tested with with :arrow_down:, a stopwatch, and Wireshark 
 
```python
import urllib2

while True:
	urllib2.urlopen("http://localhost:4545/foo/bar").read()

```


Results after 30 minutes? Not too shabby considering the request count. 

![Image of DoS](https://i.imgur.com/wAEBYMe.png)


Okay, let's get down to it. :v: :v: :v: :v:




***Grab deps (don't worry, there's only a few :) )***

```bash

$ pip install -r requirements.txt

```

***Using it***

Use your favorite text editor to change line 8:

```python

'/Users/[your username here]/POD_Server/web'

```

to reflect your username/path you cloned the project to

```bash

$ python framework_server.py thermometer-wsgi

```

It should then ask you for a port number, and then serve a hardcoded "web" directory located in the project's root. 


## Some thoughts for usage

***Serving PWD***

* Append `import os` to the `flask_app.py` file in the project's root dir
* Change `'/Users/jack/POD_Server/web'` to `os.path.curdir`


* Alternatively, change that same line to point to a directory of your choice to serve it (no need for `import os` if you're hardcoding a path
