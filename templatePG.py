## ###################################################
## Autore: 	Ortu prof. Daniele
## Azienda:	ITTS "C.Grassi" - Torino
## EMAIL:	daniele.ortu@itisgrassi.edu.it

class CPG():
	
	def __init__(self,titolo):
		self.__titolo=titolo
		self._corpo=""
		
	def __head(self):
		r="<head>"
		r+="<title>"+self.__titolo+"</title>"
		r+="</head>"
		return r
	def __menu(self):
		r="  <div style='background-color:#aaa; height:40px;width:100%;'>"
		r+="	  <div><b>Main Menu</b></div>"
		r+="  </div>"
		return ""
	def __getBunner(self):
		return "\n<img src='/img/bunner.png' alt='bunner'>"
	def __body(self):
		r="<body>"
		r+="<div style='width:100%'>"
		r+="  <div style='background-color:#b5dcb3; width:100%'>"
		r+=" <h1>CAMBIA PASSWORD</h1>"
		r+="  </div>"
		r+=self.__menu()
		r+="  <div style='background-color:#ecf0f1; height:500px;width:100%;float:left;padding-top:20px'>"
		r+="  <center>"
		r+=self.corpo
		r+="  </center>"
		r+="  </div>"
		r+="  <div style='background-color:#b5dcb3;clear:both'>"
		r+="  <center>"
		r+="	 No copyright  daniele.ortu@itisgrassi.edu.it"
		r+="  </center>"
		r+="  </div>"
		r+="</div>"
		r+="</body>"
		return r
	def _getPG(self):
		 r="<html>"		 
		 r+=self.__head()+self.__body()
		 r+="<html>"
		 return r

#if __name__ == "__main__": 
	
#	pg=CPG()
#	print(pg.getPG())
