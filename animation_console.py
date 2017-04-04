"""
Module permettant d'afficher une barre de progression 
Créé le 04/04/2017
Par Fayçal Bousmaha
"""


import time

class ProgressBar:
	def __init__ (self, msg = "Work in progress"):
		self.current = 0
		self.msg = msg

	def add (self,increment): 
		# Ajoute l'increment au pourcentage actuel
		self.current += increment
		if self.current > 100:
			self.current = 100


	def show (self):
		# Affiche la barre avec le pourcentage actuel
		text = "{} : [{}%]".format(self.msg,self.current)
		if self.isFinished():
			print(text)
		else:
			text += "\r"
			print(text,end='')

	def isFinished(self):
		# Renvoie True si la progression a atteint 100%, False sinon
		return self.current == 100

if __name__ == "__main__":
	prog = ProgressBar()
	while not prog.isFinished():
		prog.show()
		time.sleep(0.5)
		prog.add(5)