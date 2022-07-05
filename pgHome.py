## ###################################################
## Autore: 	Ortu prof. Daniele
## Azienda:	ITTS "C.Grassi" - Torino
## EMAIL:	daniele.ortu@itisgrassi.edu.it

from templatePG import CPG
from oggetti.CTXT import CTXT

class PGHome(CPG):
	def __init__(self):
		super().__init__("pagina Home")

	def getPG(self):
		txtUser=CTXT("txtUsr","","utente");
		txtVecchia=CTXT("txtVecchia","","password vecchia");
		txtVecchia.setTipo("password");
		txtNuova=CTXT("txtNuova","","password nuova");
		txtNuova.setTipo("password");
		txtConferma=CTXT("txtConferma","","password conferma");
		txtConferma.setTipo("password");
		self.corpo="<form action='pgSN' method='POST'>\n"
		#self.corpo+="<INPUT type='text'  name='txtUsr' placeholder='user'><br>"
		self.corpo+="<TABLE style='width:400px'>"
		self.corpo+="<TR>"
		self.corpo+="<TD>"+txtUser.getText()+"</TD>\n"
		self.corpo+="</TR>"
		self.corpo+="<TR>"
		self.corpo+="<TD>"+txtVecchia.getText()+"</TD>"
		self.corpo+="</TR>"
		self.corpo+="<TR>"
		self.corpo+="<TD>"+txtNuova.getText()+"</TD>"
		self.corpo+="</TR>"
		self.corpo+="<TR>"
		self.corpo+="<TD>"+txtConferma.getText()+"</TD>"
		self.corpo+="</TR>"
		self.corpo+="<TR>"
		self.corpo+="<TD><INPUT type='submit' value='aggiorna password'></TD>"
		self.corpo+="</TR>"
		self.corpo+="</TABLE>"
		self.corpo+="</form>"
		
		return self._getPG()
