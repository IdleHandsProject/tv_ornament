import SocketServer 
from BaseHTTPServer import BaseHTTPRequestHandler 
from pytube import YouTube
import os

url = 'https://www.youtube.com/watch?v='
videourl = 'https://www.youtube.com/watch?v=t7kxPYzigCQ'

def play_video(video):
    
	print video
	yt = YouTube(video).streams.filter(subtype='mp4', res='360p').first()
	filename = yt.default_filename
	print filename
	newfilename = filename.replace(" ", "")
	newfilename.replace("/", "")
	newfilename.replace("'", "")
	checkfile = newfilename
	print checkfile
	if (os.path.isfile(checkfile) == False):
		yt.download()
		os.rename(filename,checkfile)
	os.system('SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl  -framedrop -volume 10 ' + checkfile)

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if (self.path == '/favicon.ico'):
			print 'Favicon'
		elif (self.path[0] == '/'):
			print self.path
			newurl = url + self.path[1:]
			# Insert your code here
			play_video(newurl)

		self.send_response(200) 

		
httpd = SocketServer.TCPServer(("", 80), MyHandler)
httpd.serve_forever()
