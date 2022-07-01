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
	def __body(self):
		 r="<body>"
		 r+=self.corpo
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
