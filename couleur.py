"""
Module permettant d'écrire en couleur dans le terminal, de modifier l'intensité des couleurs etc ...
Créé le 02/04/2017
Par Fayçal Bousmaha

Codes SGR complets : https://en.wikipedia.org/wiki/ANSI_escape_code#graphics
"""

class Couleur:
	# Voici les codes couleurs :
	BLACK = 0
	RED = 1
	GREEN = 2
	YELLOW = 3
	BLUE = 4
	PURPULE = 5
	CYAN = 6
	WHITE = 7
	DEFAULT = 9

	# Code clignotage:
	SLOW = 0
	FAST = 1
	NO = 2


	# Voici une fonction permettant soit de changer la couleur du texte, soit celle du background
	def color(couleur, background=False):
		if background:
			print('\033[4{}m'.format(couleur),end='')
		else:
			print('\033[3{}m'.format(couleur),end='')

	# Voici une fonction permettant soit d'augmenter soit de diminuer l'intensité
	def intensite (augmenter =True):
		if augmenter:
			print('\033[1m',end='')
		else:
			print('\033[2m',end='')


	# Voici une fonction qui permet de souligner le texte
	def souligner (souligneur=True):
		if souligneur:
			print('\033[4m',end='')
		else :
			print('\033[24m',end='')


	# Fonction permettant d'incliner le texte
	def incliner(incline = True):
		if (incline):
			print('\033[3m',end='')
		else :
			print('\033[23m',end='')

	



	# Voici une fonction qui remet le style comme il est par défaut
	def defaut():
		print('\033[0m',end='')


	def test():
		Couleur.color(Couleur.BLUE)
		print("Bleu")
		Couleur.color(Couleur.WHITE)
		print("Blanc")
		Couleur.color(Couleur.RED)
		print("Rouge")
		print("\n")
		Couleur.color(Couleur.GREEN)
		print("Hacking")
		Couleur.intensite()
		Couleur.intensite()
		print("Hacking")
		Couleur.intensite(False)
		Couleur.intensite(False)
		print("Hacking")
		Couleur.souligner()
		print("Hacking")
		Couleur.souligner(False)
		print("Hacking")
		Couleur.incliner()
		print("Hacking")
		Couleur.incliner(False)
		print("Hacking")
		Couleur.defaut()
		print("Hacking")
		Couleur.color(Couleur.PURPULE,True)
		print("Sur fond violet")
		Couleur.defaut()
		print("Merci, au revoir")



# Test
Couleur.test()


