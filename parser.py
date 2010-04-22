#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from re import *
from tools import clean_name

def get_data(path, coding='utf-8'):
    """Extracting data from the file"""
    try:
        file = open(path, encoding=coding)
    except:
        return 0
    else:
        return file.readlines()

def get_corresp(data, start, destination):

    #The dict in which we store the corresps map
    corresp = {}

    """Fetching the file for building a corresp dict looking like:
    corresp = {"La Défense":['Neuilly',"ligne 3",'Argenteuil'], 
    ... ['CCial','ligne 3', 'Bercy'], ['Nanterre', 'ligne 4', 'Saint-Denis']}"""
    
    
    
    while data:
        #If the current line of text is a metro line
        if findall('\[(.+)\]',data[0]):
            line_name = findall('\[(.+)\]',data[0])[0]
            data.pop(0)
            
            stations = []#We store the ordered stations of the line in a list
            
            #Get the stations
            #While we stay on the same metro line
            while not findall('\[(.+)\]',data[0]):
                station = findall(r'\b.+',data[0])[0]
                
                if clean_name(station) == clean_name(start):
                    station = clean_name(station)
                elif clean_name(station) == clean_name(destination):
                    station = clean_name(station)
                    
                stations.append(station)
                data.pop(0)

                #If there's nothing else to examine
                if not data:
                    break

            #Infos about the line        
            first_station = stations[0]
            last_station = stations[-1]

            #Creation of the corresp table for this line
            for d, station in enumerate(stations):
                linked_with = list()
                if d < (len(stations) - 1):
                    linked_with.append([stations[d + 1], line_name, last_station])
                if d > 0:
                    linked_with.append([stations[d - 1], line_name, first_station])

                if station not in corresp:
                    corresp[station] = linked_with
                else:
                    corresp[station].extend(linked_with)
                    
        else:
            data.pop(0)
                     
    
    return corresp


if __name__ == '__main__':
    print(get_lines('stations.txt'))
            
    
    
    
    
