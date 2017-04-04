"""
Exemple de récupération des arguments avec argparse
Créé le 05/04/2017
Par Fayçal Bousmaha
"""

import sys
import argparse

def syntax():
	print("Syntax: recuperer_arguments fillename [-v|--verbose] [--output=filename]")
	print("		filename : fichier en entrée")
	print("		-v | --verbose : mode verbeux")
	print("		--output=filename : fichier en sortie")
	exit(1)

def cmd_line(args):
	arguments = { 'input':None, 'verbose':False, 'output':'default.txt'}
	parser = argparse.ArgumentParser(description='Récuperer les arguments de la ligne de commande')
	parser.add_argument('-v','--verbose', dest='verbose', default=False, action='store_true', help='mode verbeux')
	parser.add_argument('input', action='store', help='fichier en entrée')
	parser.add_argument('--output', dest='output', default='default.txt', help='fichier en sortie')
	return parser.parse_args()

if __name__ == '__main__':
	args = cmd_line(sys.argv)
	print(args)