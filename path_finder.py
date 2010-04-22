#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from tools import secondes_to_higher, clean_name

def path (start, destination, corresp, delai_correspondance, delai_stations):

    to_do = [[0, clean_name(start), [], '']] 
    done = list()

    while to_do:
        to_do.sort()
        
        station = to_do[0]
        
        cost = station[0]
        name = station[1]
        line = station[3]
        
        path_done = station[2]
        links = corresp[name]

        if clean_name(name) == clean_name(destination):
            print("Le trajet dure %s minutes" % secondes_to_higher(cost))
            return path_done

        for link in links:
            if link[0] not in done:
                next_cost = cost
                if link[1] != line and line:
                    next_cost += delai_correspondance
                next_cost += delai_stations
                    
                next_path = path_done + [link]
                to_do.append([next_cost, link[0], next_path, link[1]])
                
        done.append(name)
        to_do.pop(0)

    return 0
                
                
