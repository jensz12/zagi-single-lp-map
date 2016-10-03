# -*- coding: utf-8 -*-

def farmSheepFilter(poi):
    if poi['id'] == 'FarmSheep':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
def shipFilter(poi):
    if poi['id'] == 'Skib':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def billedeFilter(poi):
    if poi['id'] == 'Billede':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def portalFilter(poi):
    if poi['id'] == 'Portaler':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

# Define the path to your world here. 'Zagi Single Player' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['Zagi Single Player'] = "C:/Users/Jens/Downloads/world"

# Define where to put the output.
outputdir = "C:/zagi/world"

# Dag med Smooth Lightning
renders["singleoverworld"] = {
    "world": "Zagi Single Player",
    "title": "Dag",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    'manualpois':[
                   {'id':'FarmSheep',
                    'x':335,
                    'y':64,
                    'z':-1169,
                    'name':'Fårefarmen',
                    'description':'Fårefarmen, bygget i episode 88 & 107'},
                    {'id':'Skib',
                    'x':-553,
                    'y':64,
                    'z':1853,
                    'name':'Piratskibet',
                    'description':'Piratskibet, bygget i episode 89'},
                    {'id':'Billede',
                    'x':5869,
                    'y':64,
                    'z':-910,
                    'name':'Billedet af Zagi',
                    'description':'Billedet af Zagi, påbegyndt i episode 90, færdigjort i episode ??'},
                    {'id':'Portaler',
                    'x':2920,
                    'y':64,
                    'z':2300,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':2762,
                    'y':64,
                    'z':3856,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':10,
                    'y':64,
                    'z':671,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':-1793,
                    'y':64,
                    'z':881,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':-3270,
                    'y':64,
                    'z':795,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':-2906,
                    'y':64,
                    'z':-1335,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    ],
	'markers':[ 
				dict(name="FarmSheep", filterFunction=farmSheepFilter, icon="icons/marker_farm_sheep.png"),
                dict(name="Skib", filterFunction=shipFilter, icon="icons/marker_ship.png"),
                dict(name="Billede", filterFunction=billedeFilter, icon="icons/marker_zagi.png"),
                dict(name="Portaler", filterFunction=portalFilter, icon="icons/marker_portal.png"),],
}
# Overworld caves
renders["singlecave"] = {
    "world": "Zagi Single Player",
    "title": "Cave",
    "rendermode": cave,
    "dimension": "overworld",
                        }
# Overworld nat
renders["singlenight"] = {
    "world": "Zagi Single Player",
    "title": "Nat",
    "rendermode": smooth_night,
    "dimension": "overworld",
    'manualpois':[
                   {'id':'FarmSheep',
                    'x':335,
                    'y':64,
                    'z':-1169,
                    'name':'Fårefarmen',
                    'description':'Fårefarmen, bygget i episode 88 & 107'},
                    {'id':'Skib',
                    'x':-553,
                    'y':64,
                    'z':1853,
                    'name':'Piratskibet',
                    'description':'Piratskibet, bygget i episode 89'},
                    {'id':'Billede',
                    'x':5869,
                    'y':64,
                    'z':-910,
                    'name':'Billedet af Zagi',
                    'description':'Billedet af Zagi, påbegyndt i episode 90, færdigjort i episode ??'},
                    {'id':'Portaler',
                    'x':2920,
                    'y':64,
                    'z':2300,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':2762,
                    'y':64,
                    'z':3856,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':10,
                    'y':64,
                    'z':671,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':-1793,
                    'y':64,
                    'z':881,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':-3270,
                    'y':64,
                    'z':795,
                    'name':'Portal',
                    'description':'Portal til Nether'},
                    {'id':'Portaler',
                    'x':-2906,
                    'y':64,
                    'z':-1335,
                    'name':'Portal',
                    'description':'Portal til Nether'},],
	'markers':[ 
				dict(name="FarmSheep", filterFunction=farmSheepFilter, icon="icons/marker_farm_sheep.png"),
                dict(name="Skib", filterFunction=shipFilter, icon="icons/marker_ship.png"),
                dict(name="Billede", filterFunction=billedeFilter, icon="icons/marker_zagi.png"),
                dict(name="Portaler", filterFunction=portalFilter, icon="icons/marker_portal.png"),],
}
# Nether med Smooth Lightning
renders["singlenether"] = {
    "world": "Zagi Single Player",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
# End
renders["singleend"] = {
    "world": "Zagi Single Player",
    "title": "End",
    "rendermode": end_smooth_lighting,
    "dimension": "end",
}
