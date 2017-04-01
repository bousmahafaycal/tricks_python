"""
Module utilisant cgitb permettant d'obtenir une trace détaillée des erreurs
Créé le 02/04/2017
Par Fayçal Bousmaha
"""
import cgitb # La librairie qui va être utilisée
cgitb.enable(format='text') # Fonction permettant d'activer le mode de trace étendu


def division(a,b):
	print(str(a)+" divisé par "+str(b)+" donne : "+str(a/b))

division(10,0)