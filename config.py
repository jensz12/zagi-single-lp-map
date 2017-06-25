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
            
def villagerFilter(poi):
    if poi['id'] == 'Villager':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def farmCreeperFilter(poi):
    if poi['id'] == 'CreeperFarm':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def farmIceFilter(poi):
    if poi['id'] == 'IsFarm':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def endGenFilter(poi):
    if poi['id'] == 'EndGenerator':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def endFarmFilter(poi):
    if poi['id'] == 'EndFarm':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
            
def netherZooFilter(poi):
    if poi['id'] == 'NetherZoo':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def farmAreaFilter(poi):
    if poi['id'] == 'FarmArea':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
        
def desertPaladsFilter(poi):
    if poi['id'] == 'DesertPalads':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
        
def spawnFireworkFilter(poi):
    if poi['id'] == 'SpawnFirework':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def mobFarmFilter(poi):
    if poi['id'] == 'mobFarm':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def diskotekFilter(poi):
    if poi['id'] == 'Diskotek':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
        
def peacfullMobFilter(poi):
    if poi['id'] == 'PeacfullMobs':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def farmWitchFilter(poi):
    if poi['id'] == 'FarmWitch':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def flowerUfoFilter(poi):
    if poi['id'] == 'FlowerUfo':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def farmPumpkinFilter(poi):
    if poi['id'] == 'FarmPumpkin':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def dropperAreaFilter(poi):
    if poi['id'] == 'DropperArea':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
            
def farmGuardianFilter(poi):
    if poi['id'] == 'FarmGuardian':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
        
end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

# Define the path to your world here. 'Zagi Single Player' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['Zagi Single Player'] = "/home/jens/zagi/world"

# Define where to put the output.
outputdir = "/var/www/map.zagimc.dk/public_html"

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
                    {'id':'FarmPumpkin',
                    'x':-1793,
                    'y':64,
                    'z':881,
                    'name':'Græskar farm',
                    'description':'Græskar farm'},
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
                    {'id':'Villager',
                    'x':2565,
                    'y':64,
                    'z':2250,
                    'name':'Villager øen',
                    'description':'Villager øen'},
                    {'id':'CreeperFarm',
                    'x':3073,
                    'y':64,
                    'z':2300,
                    'name':'Charged Creeper farm',
                    'description':'Charged Creeper farm. Bygget i episode 68'},
                    {'id':'IsFarm',
                    'x':2671,
                    'y':64,
                    'z':3852,
                    'name':'Is farmen',
                    'description':'Is farmen. Bygget i episode 72'},
                    {'id':'FarmArea',
                    'x':70,
                    'y':64,
                    'z':-381,
                    'name':'Farm området',
                    'description':'Farm område. Indeholder blandt andet en guldfarm.'},
                    {'id':'DesertPalads',
                    'x':-1393,
                    'y':64,
                    'z':-482,
                    'name':'Ørken Palads',
                    'description':'Palads til dropper maps'},
                    {'id':'SpawnFirework',
                    'x':-138,
                    'y':64,
                    'z':146,
                    'name':'Fyrværkeri',
                    'description':'Hytte til fyrværkeri i spawn'},
                    {'id':'MobFarm',
                    'x':52,
                    'y':64,
                    'z':649,
                    'name':'Mob farm',
                    'description':'Mob farm'},
                    {'id':'Diskotek',
                    'x':-367,
                    'y':64,
                    'z':640,
                    'name':'Diskotek',
                    'description':'Diskotek'},
                    {'id':'PeacefullMobs',
                    'x':3000,
                    'y':64,
                    'z':2330,
                    'name':'Peacfull mob farm',
                    'description':'Peacfull mob farm'},
                    {'id':'FarmWitch',
                    'x':1990,
                    'y':64,
                    'z':1454,
                    'name':'Witch farm',
                    'description':'Witch farm'},
                    {'id':'FlowerUfo',
                    'x':2260,
                    'y':64,
                    'z':2825,
                    'name':'Blomster UFO',
                    'description':'Blomster Ufo'},
                    {'id':'DropperArea',
                    'x':-1034,
                    'y':64,
                    'z':-550,
                    'name':'Dropper området',
                    'description':'Dropper maps'},
                    {'id':'FarmGuardian',
                    'x':-3000,
                    'y':64,
                    'z':-1230,
                    'name':'Guardian farm',
                    'description':'Guardian farm'},],
	'markers':[ 
				dict(name="FarmSheep", filterFunction=farmSheepFilter, icon="icons/marker_farm_sheep.png"),
                dict(name="Skib", filterFunction=shipFilter, icon="icons/marker_ship.png"),
                dict(name="Billede", filterFunction=billedeFilter, icon="icons/marker_zagi.png"),
                dict(name="Portaler", filterFunction=portalFilter, icon="icons/marker_portal.png"),
                dict(name="Villager", filterFunction=villagerFilter, icon="icons/marker_villager.png"),
                dict(name="CreeperFarm", filterFunction=farmCreeperFilter, icon="icons/marker_farm_creeper.png"),
                dict(name="IsFarm", filterFunction=farmIceFilter, icon="icons/marker_farm_ice.png"),
                dict(name="FarmArea", filterFunction=farmAreaFilter, icon="icons/marker_farm_area.png"),
                dict(name="DesertPalads", filterFunction=desertPaladsFilter, icon="icons/marker_desert_palads.png"),
                dict(name="SpawnFirework", filterFunction=spawnFireworkFilter, icon="icons/marker_spawn_firework.png"),
                dict(name="MobFarm", filterFunction=mobFarmFilter, icon="icons/marker_farm_mob.png"),
                dict(name="Diskotek", filterFunction=diskotekFilter, icon="icons/marker_diskotek.png"),
                dict(name="PeacfullMobs", filterFunction=peacfullMobFilter, icon="icons/marker_farm_peacfull.png"),
                dict(name="FarmWitch", filterFunction=farmWitchFilter, icon="icons/marker_farm_witch.png"),
                dict(name="FlowerUfo", filterFunction=flowerUfoFilter, icon="icons/marker_flower_ufo.png"),
                dict(name="FarmPumpkin", filterFunction=farmPumpkinFilter, icon="icons/marker_farm_pumpkin.png"),
                dict(name="DropperArea", filterFunction=dropperAreaFilter, icon="icons/marker_dropper_area.png"),
                dict(name="FarmGuardian", filterFunction=farmGuardianFilter, icon="icons/marker_farm_guardian.png"),],
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
                    {'id':'FarmPumpkin',
                    'x':-1793,
                    'y':64,
                    'z':881,
                    'name':'Græskar farm',
                    'description':'Græskar farm'},
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
                    {'id':'Villager',
                    'x':2565,
                    'y':64,
                    'z':2250,
                    'name':'Villager øen',
                    'description':'Villager øen'},
                    {'id':'CreeperFarm',
                    'x':3073,
                    'y':64,
                    'z':2300,
                    'name':'Charged Creeper farm',
                    'description':'Charged Creeper farm. Bygget i episode 68'},
                    {'id':'IsFarm',
                    'x':2671,
                    'y':64,
                    'z':3852,
                    'name':'Is farmen',
                    'description':'Is farmen. Bygget i episode 72'},
                    {'id':'FarmArea',
                    'x':70,
                    'y':64,
                    'z':-381,
                    'name':'Farm området',
                    'description':'Farm område. Indeholder blandt andet en guldfarm.'},
                    {'id':'DesertPalads',
                    'x':-1393,
                    'y':64,
                    'z':-482,
                    'name':'Ørken Palads',
                    'description':'Palads til dropper maps'},
                    {'id':'SpawnFirework',
                    'x':-138,
                    'y':64,
                    'z':146,
                    'name':'Fyrværkeri',
                    'description':'Hytte til fyrværkeri i spawn'},
                    {'id':'MobFarm',
                    'x':52,
                    'y':64,
                    'z':649,
                    'name':'Mob farm',
                    'description':'Mob farm'},
                    {'id':'Diskotek',
                    'x':-367,
                    'y':64,
                    'z':640,
                    'name':'Diskotek',
                    'description':'Diskotek'},
                    {'id':'PeacefullMobs',
                    'x':3000,
                    'y':64,
                    'z':2245,
                    'name':'Peacfull mob farm',
                    'description':'Peacfull mob farm'},
                    {'id':'FarmWitch',
                    'x':1990,
                    'y':64,
                    'z':1454,
                    'name':'Witch farm',
                    'description':'Witch farm'},
                    {'id':'FlowerUfo',
                    'x':2260,
                    'y':64,
                    'z':2825,
                    'name':'Blomster UFO',
                    'description':'Blomster Ufo'},
                    {'id':'DropperArea',
                    'x':-1034,
                    'y':64,
                    'z':-550,
                    'name':'Dropper området',
                    'description':'Dropper maps'},
                    {'id':'FarmGuardian',
                    'x':-3000,
                    'y':64,
                    'z':-1230,
                    'name':'Guardian farm',
                    'description':'Guardian farm'},],
	'markers':[ 
				dict(name="FarmSheep", filterFunction=farmSheepFilter, icon="icons/marker_farm_sheep.png"),
                dict(name="Skib", filterFunction=shipFilter, icon="icons/marker_ship.png"),
                dict(name="Billede", filterFunction=billedeFilter, icon="icons/marker_zagi.png"),
                dict(name="Portaler", filterFunction=portalFilter, icon="icons/marker_portal.png"),
                dict(name="Villager", filterFunction=villagerFilter, icon="icons/marker_villager.png"),
                dict(name="CreeperFarm", filterFunction=farmCreeperFilter, icon="icons/marker_farm_creeper.png"),
                dict(name="IsFarm", filterFunction=farmIceFilter, icon="icons/marker_farm_ice.png"),
                dict(name="FarmArea", filterFunction=farmAreaFilter, icon="icons/marker_farm_area.png"),
                dict(name="DesertPalads", filterFunction=desertPaladsFilter, icon="icons/marker_desert_palads.png"),
                dict(name="SpawnFirework", filterFunction=spawnFireworkFilter, icon="icons/marker_spawn_firework.png"),
                dict(name="MobFarm", filterFunction=mobFarmFilter, icon="icons/marker_farm_mob.png"),
                dict(name="Diskotek", filterFunction=diskotekFilter, icon="icons/marker_diskotek.png"),
                dict(name="PeacfullMobs", filterFunction=peacfullMobFilter, icon="icons/marker_farm_peacfull.png"),
                dict(name="FarmWitch", filterFunction=farmWitchFilter, icon="icons/marker_farm_witch.png"),
                dict(name="FlowerUfo", filterFunction=flowerUfoFilter, icon="icons/marker_flower_ufo.png"),
                dict(name="FarmPumpkin", filterFunction=farmPumpkinFilter, icon="icons/marker_farm_pumpkin.png"),
                dict(name="DropperArea", filterFunction=dropperAreaFilter, icon="icons/marker_dropper_area.png"),
                dict(name="FarmGuardian", filterFunction=farmGuardianFilter, icon="icons/marker_farm_guardian.png"),],
}
# Nether med Smooth Lightning
renders["singlenether"] = {
    "world": "Zagi Single Player",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
    'manualpois':[
                   {'id':'NetherZoo',
                    'x':86,
                    'y':64,
                    'z':-59,
                    'name':'Zoo',
                    'description':'Zoo'},],
	'markers':[ 
				dict(name="NetherZoo", filterFunction=netherZooFilter, icon="icons/marker_zoo.png"),],
}
# End
renders["singleend"] = {
    "world": "Zagi Single Player",
    "title": "End",
    "rendermode": end_smooth_lighting,
    "dimension": "end",
    'manualpois':[
                   {'id':'EndGen',
                    'x':0,
                    'y':64,
                    'z':0,
                    'name':'End generator',
                    'description':'Sand generator'},
                    {'id':'EndFarm',
                    'x':327,
                    'y':64,
                    'z':10,
                    'name':'Enderman farm',
                    'description':'Enderman farm'},],
	'markers':[ 
				dict(name="EndGenerator", filterFunction=endGenFilter, icon="icons/marker_gen_end.png"),
                dict(name="EndFarm", filterFunction=endFarmFilter, icon="icons/marker_farm_end.png"),],
}
