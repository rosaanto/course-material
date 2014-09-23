# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
    }
#print(station.keys())
#print(station.item())
#for key in station.keys():
#   print "key: %s , value: %s" % (key, station[key])
#print(station)
#for i in station:
#    print(i)
#print(len(station))
#print(station[key])
for key, value in station.iteritems():
    print(key, value)
