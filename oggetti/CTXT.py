## ###################################################
## Autore: 	Ortu prof. Daniele
## Azienda:	ITTS "C.Grassi" - Torino
## EMAIL:	daniele.ortu@itisgrassi.edu.it

class CTXT():
	
	def __init__(self,nome,valore,placeholder):
		self.__nome=nome
		self.__valore=valore
		self.__tipo=""
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
		return "font: bold 28px Arial, Helvetica, sans-serif;"
	def getColor(self):
		 return "color: #000000;"
	def getBackground(self):
		 return "background: #FFFFFF;"
	def getBordi(self):
		return " \
				  border-top: 0px solid #000000; \
				  border-left: 0px solid #000000; \
				  border-bottom: 1px solid #000000; \
				  border-right: 0px solid #000000; \
			   "  
	def getPadding(self):
		return " \
				  padding-top: 1px; \
				  padding-left: 1px; \
				  padding-bottom: 1px; \
				  padding-right: 1px; \
			   "  
	def getStile(self):
		return "style='"+self.getFont()+self.getColor()+self.getBackground()+self.getBordi()+self.getPadding()+"'"
	def getText(self):
		return "<INPUT type='"+self.__tipo+"' name='"+self.__nome+"' id='"+self.__nome+ \
				"' "+self.getStile()+" value='"+self.__valore+"' "+self.__getPH()+">"

#if __name__ == "__main__": 
	
#	pg=CPG()
#	print(pg.getPG())
