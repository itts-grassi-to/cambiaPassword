## ###################################################
## Autore: 	Ortu prof. Daniele
## Azienda:	ITTS "C.Grassi" - Torino
## EMAIL:	daniele.ortu@itisgrassi.edu.it

from pgHome import PGHome
from pgAggiorna import PGAggiorna

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
#import urlparse
#from urllib.parse import urlparse, parse_qs
#from html.parser import HTMLParser
import ast

#hostName = "localhost"
hostName = "192.168.1.77"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def pgDefault(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p> PAGINA "+self.path+" NON GESTITA</p>","utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
	  
    def pgHome(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        pg=PGHome();

        self.wfile.write(bytes(pg.getPG(), "utf-8"))
    def pgAggiorna(self,usr,vecchia,nuova,conferma):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        pg=PGAggiorna(usr,vecchia,nuova,conferma);

        self.wfile.write(bytes(pg.getPG(), "utf-8"))
		
    def do_GET(self):
        if self.path=="/":
          self.pgHome()
        else:
          self.pgDefault()
    def do_POST(self):
        if self.path=="/pgSN":
          #self.log_message( "Command: %s \nPath: %s \nHeaders: %r"
          #            % ( self.command, self.path, self.headers.items() ) )
          print("******************************************************************")
         
          length= int( self.headers['content-length'] )
          field_data = str(self.rfile.read(length))
          #fields = urlparse.parse_qs(field_data)
          dicPar=self.getDicParam(field_data)
          self.pgAggiorna(
            dicPar['txtUsr'],
            dicPar['txtVecchia'],
            dicPar['txtNuova'],
            dicPar['txtConferma']
          )
        else:
          self.pgDefault()

    def getDicParam(self,s):
        s="{'"+s[2:len(s)-1]+"'}"
        s=s.replace("=","':'")
        s=s.replace("&","','")
        return ast.literal_eval(s)
        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
