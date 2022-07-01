## ###################################################
## Autore: 	Ortu prof. Daniele
## Azienda:	ITTS "C.Grassi" - Torino
## EMAIL:	daniele.ortu@itisgrassi.edu.it

from templatePG import CPG

class PGHome(CPG):
	def __init__(self):
		super().__init__("pagina Home")

	def getPG(self):
		self.corpo="<form action='pgSN' method='POST'>"
		self.corpo+="<INPUT type='text'  name='txtUsr' placeholder='user'><br>"
		self.corpo+="<INPUT type='password'  name='txtVecchia' placeholder='password vecchia'><br>"
		self.corpo+="<INPUT type='passwor' name='txtNuova' placeholder='password nuova'><br>"
		self.corpo+="<INPUT type='password' name='txtConferma' placeholder='password confema'><br>"
		self.corpo+="<INPUT type='submit' value='aggiorna password'><br>"
		self.corpo+="</form>"
		
		return self._getPG()
