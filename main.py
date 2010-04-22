#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from parser import get_data, get_corresp
from path_finder import *
from show_result import *
from tools import clean_name

def main(start, destination, file, delai_correspondance, delai_stations):
    """The Main Controller of the program, the functions are called here"""

    #Opening the file
    data = get_data(file)
    if not data:
        print('Fichier de description introuvable !')
        exit()

    #Building the linking map for each stations
    corresp = get_corresp(data, start, destination)
    
    if not corresp:
        return'Format du fichier de description invalide !'
    inexistant = 0
    if clean_name(start) not in corresp:
        inexistant = start
    elif clean_name(destination) not in corresp:
        inexistant = destination
    if inexistant:
        return 'Station "%s" introuvable dans ce fichier de description' % inexistant
       

    #Finding the shortest path
    path_done = path(start, destination, corresp, delai_correspondance, delai_stations)

    #Show results
    return display(path_done)


if __name__ == '__main__':
    """Interactive mode with the user"""
    
    import sys
    import appendix

    #Help
    if '-h' in sys.argv:
        print(appendix.help())
        exit()
    
    #Copyright
    if '-v' in sys.argv:
        print(appendix.copyright())
        exit()
        
    #Station de départ
    if '-x' in sys.argv:
        start = sys.argv[sys.argv.index('-x') + 1]
    else:
        start = input('Station de départ : \t')

    #Station d'arrivée
    if '-y' in sys.argv:
        destination = sys.argv[sys.argv.index('-y') + 1]
    else:
        destination = input('Station d\'arrivée : \t')

    #Temps pour aller d'une station à l'autre
    if '-d' in sys.argv:
        delai_stations = sys.argv[sys.argv.index('-d') + 1]
    else:
        delai_stations = input('Temps entre stations : \t')

    #Durée des correspondances
    if '-c' in sys.argv:
        delai_correspondance = sys.argv[sys.argv.index('-c') + 1]
    else:
        delai_correspondance = input('Durée des correspondances : \t')

    #Fichier listant les stations par ligne
    if '-f' in sys.argv:
        file = sys.argv[sys.argv.index('-f') + 1]
    else:
        print('Spécifiez un nom de fichier !')
        file = input('Fichier listant les stations :\t')
        

    #Lancement du programme
    print(main(start, destination, file, int(delai_correspondance), int(delai_stations)))
