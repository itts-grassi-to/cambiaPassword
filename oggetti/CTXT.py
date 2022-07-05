## ###################################################
## Autore: 	Ortu prof. Daniele
## Azienda:	ITTS "C.Grassi" - Torino
## EMAIL:	daniele.ortu@itisgrassi.edu.it

class CTXT():
	
	def __init__(self,nome,valore,placeholder):
		self.__nome=nome
		self.__valore=valore
		self.__tipo="Text"
		self.__placeholder=placeholder
	def getNome(self):
		return self.nome
	def getValore(self):
		return self.valore
	def __getPH(self):
		if self.__placeholder!="":
			return "placeholder='"+self.__placeholder+"'"
		return ""
	def getFont(self):
		return "font:  25px Arial, Helvetica, sans-serif;"
	def getColor(self):
		 return "color: #000000;"
	def getBackground(self):
		return "background: transparent;"
		 #return "background: #FFFFFF;"
	def getBordi(self):
		return " \
				  border-top: 0px solid #000000; \
				  border-left: 0px solid #000000; \
				  border-bottom: 1px solid #f98012; \
				  border-right: 0px solid #f98012; \
			   "  
	def getPadding(self):
		return " \
				  padding-top: 5px; \
				  padding-left: 5px; \
				  padding-bottom: 5px; \
				  padding-right: 5px; \
			   "
	def getLarghezza(self):
		return "width: 100%;";
	def getStile(self):
		return "style='"+self.getFont()+self.getColor()+self.getBackground()+ \
				self.getBordi()+self.getPadding()+self.getLarghezza()+"'"

	def setTipo(self,tp):
		self.__tipo=tp		   

	def getText(self):
		return "<INPUT type='"+self.__tipo+"' name='"+self.__nome+"' id='"+self.__nome+ \
				"' "+self.getStile()+" value='"+self.__valore+"' "+self.__getPH()+">"

#if __name__ == "__main__": 
	
#	pg=CPG()
#	print(pg.getPG())
