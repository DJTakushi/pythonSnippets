#naming convention:  major + polite + +/-	
#assume plain & current

class verb:
	def __init__(self,name,type,deviation):
		self.__name__ = name
		self.type = type
		self.deviation = deviation
		self.length = len(self.__name__)
		self.stem = self.__name__[0:self.length-2]
		if(self.type=="ru"):
			self.fStem=self.stem
		else:
			if(self.__name__[self.length-2:self.length-0] == "su"):
				self.fStem = self.__name__[0:self.length-2]+"shi"
			elif(self.__name__[self.length-2:self.length-0] == "ru"):
				self.fStem = self.__name__[0:self.length-2]+"ri"
			elif(self.__name__[self.length-2:self.length-0] == "ku"):
				self.fStem = self.__name__[0:self.length-2]+"ki"				
			elif(self.__name__[self.length-2:self.length-0] == "gu"):
				self.fStem = self.__name__[0:self.length-2]+"gi"			
			elif(self.__name__[self.length-2:self.length-0] == "gu"):
				self.fStem = self.__name__[0:self.length-2]+"gi"					
			elif(self.__name__[self.length-1:self.length-0] == "u"):
				self.fStem = self.__name__[0:self.length-1]+"i"					
			else:
				self.fStem = "bacon"
		print("plain = ",self.__name__, ", fStem = ",self.fStem)
			
		
			
	def __str__(self):
		return(self.__name__)
	def rfStem(self):
		return(self.__name__)
		#return(self.fStem)

	def polite(self):
		return(self.stem + "masu")
	def negative(self):
		return(self.stem + "nai")
	def politeNegative(self):
		return(self.stem + "masen")


	def past(self):
		return(self.stem + "ta")		
	def pastPolite(self):
		return(self.stem + "mashita")
	def pastNegative(self):
		return(self.stem + "nakatta")
	def pastPoliteNegative(self):
		return(self.stem + "masendeshita")

		
	def te(self):
		return(self.stem + "te")		
	def teNegative(self):
		return(self.stem + "nakute")		
		
	def potential(self):
		return(self.stem + "rareru")	
	def potentialNegative(self):
		return(self.stem + "rarenai")			
		
	def passive(self):
		return(self.stem + "rareru")
	def passiveNegative(self):
		return(self.stem + "rarenai")
		
	def causitive(self):
		return(self.stem + "saseru")
	def causitiveNegative(self):
		return(self.stem + "sasenai")

	def causitivePassive(self):
		return(self.stem + "saserareru")
	def causitivePassiveNegative(self):
		return(self.stem + "saserarenai")		
		
taberu = verb("taberu","ru",0)
#print("Regular =                  ",taberu)
#print("negative =                 ",taberu.negative())
#print("polite =                   ",taberu.polite())
#print("politeNegative =           ",taberu.politeNegative())
#print("past =                     ",taberu.past())
#print("pastPolite =               ",taberu.pastPolite())
#print("pastNegative =             ",taberu.pastNegative())
#print("pastPoliteNegative =       ",taberu.pastPoliteNegative())
#print("te =                       ",taberu.te())
#print("teNegative =               ",taberu.teNegative())
#print("potential =                ",taberu.potential())
#print("potentialNegative =        ",taberu.potentialNegative())
#print("passive =                  ",taberu.passive())
#print("passiveNegative =          ",taberu.passiveNegative())
#print("causitive =                ",taberu.causitive())
#print("causitiveNegative =        ",taberu.causitiveNegative())
#print("causitivePassive =         ",taberu.causitivePassive())
#print("causitivePassiveNegative = ",taberu.causitivePassiveNegative())

hanasu = verb("hanasu","u",0)
#print("regular = ", hanasu)
#print("fStem = ",hanasu.fStem)

iu = verb("iu","u",0)