## ###################################################
## Autore: 	Ortu prof. Daniele
## Azienda:	ITTS "C.Grassi" - Torino
## EMAIL:	daniele.ortu@itisgrassi.edu.it

import os
from templatePG import CPG

class PGAggiorna(CPG):
	def __init__(self,usr,vecchia,nuova,conferma):
		super().__init__("pagina Home")
		self.usr=usr
		self.vecchia=vecchia
		self.nuova=nuova
		self.conferma=conferma

	def _controlloParametri(self):
		if self.vecchia=="" or \
			  self.usr=="" or \
			  self.nuova=="" or \
			  self.conferma=="":
			return False
		if self.nuova!=self.conferma:
			return False
		
		return True
	
	def getPG(self):
		if not self._controlloParametri():
			self.corpo= "parametri inseriti errati" 
		else:
			r=os.system('echo "'+self.vecchia+'" | smbclient -L localhost -U '+self.usr)
			if r!=0:
				self.corpo="utente e password non coincidenti o non esistenti"
			else:
				#r=os.system('smbpasswd -x '+self.usr)
				#print('echo -e "'+self.nuova+'\n'+self.conferma+'" | sudo smbpasswd -as '+self.usr)
				#r=os.system('echo -e "'+self.nuova+'\n'+self.nuova+'" | sudo smbpasswd -a '+self.usr)
				#istr=b"echo -e 'mmTah99e\nmmTah99e' | sudo smbpasswd -a "+bytes(self.usr,"utf-8")
				istr="./script.sh "+self.nuova+" "+self.conferma+" "+self.usr
				r=os.system(istr)
				print(istr)
#				if self.nuova==self.conferma:
#					self.corpo="PASSWORD AGGIORNATA"
#				else:
				if r==0:
					self.corpo="PASSWORD AGGIORNATA"
				else:
					self.corpo="PASSWORD NON AGGIORNATA"
		return self._getPG()
