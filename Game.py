#Imports
import array
import random
import requests
from pprint import pprint
#Global Variables
Worldname = "Faerun"

Characterinventory = []

#CharacterSheet
class CharacterSheet:
    name = ""
    race = ""
    gender = ""
    characterclass = ""
    background = ""
    alignment = ""
    stats = []

    def __init__(self, name, race, gender, characterclass, background, alignment, stats):
        self.name = name
        self.race = race
        self.gender = gender
        self.characterclass = characterclass
        self.background = background
        self.alignment = alignment
        self.stats = stats
#Race
        

#RacesConfig
AvailableRaces = []

HumanRaces = []
Human = ["Human", "+1 to All Ability Scores", "Extra Language", "Size: Medium", "Base speed: 30ft"]
HumanV = ["Human(V)", "+1 to 2 Ability Scores", "+1 Skill Proficiency", "+1 Feat", "Base speed: 30ft"]

ElfRaces = []
HighElf = ["HighElf", "+2 Dexterity", "+1 Intelligence", "Darkvision: 60ft", "Percpetion Proficiency", "Longsword, Shortsword, Shortbow and Longbow proficency", "Fey Ancestry", "+1 Wizard Cantrip(INT)", "Elvish + 1 Extra Language", "Size: Medium", "Base speed: 30ft"]
WoodElf = ["WoodElf", "+2 Dexterity", "+1 Wisdom", "Darkvision: 60ft", "Percpetion Proficiency", "Longsword, Shortsword, Shortbow and Longbow proficency", "Fey Ancestry", "Mask of the Wild(Hide)", "Elvish", "Size: Medium", "Base speed: 35ft"]

DwarfRaces = []
HillDwarf = ["HillDwarf", "+2 Constitution", "+1 Wisdom", "Darkvision: 60ft", "Dwarven Resilience", "Dwarven Toughness", "Battleaxe, Handaxe, LightHammer and Warhammer proficiency", "Smith's tools, Brewer's Supplies or Mason's tools proficiency", "Stonecunning", "Dwarfish", "Size: Medium", "Base speed: 25ft", ]
MountainDwarf = ["MountainDwarf", "+2 Constitution", "+2 Strength" "Darkvision: 60ft", "Dwarven Resilience", "Battleaxe, Handaxe, LightHammer and Warhammer proficiency", "Light and Medium armour proficiency", "Smith's tools, Brewer's Supplies or Mason's tools proficiency", "Stonecunning", "Dwarfish", "Size: Medium", "Base speed: 25ft", ]

#Create races
def racesetup():
    HumanRaces.extend(Human)
    HumanRaces.append(HumanV)
    ElfRaces.append(HighElf)
    ElfRaces.append(WoodElf)
    DwarfRaces.append(HillDwarf)
    DwarfRaces.append(MountainDwarf)
    AvailableRaces.append(HumanRaces)
    AvailableRaces.append(ElfRaces)
    AvailableRaces.append(DwarfRaces)
    for race in AvailableRaces:
        print(race)
        print("\n")

#ClasesConfig
AvailableClasses = []

Rogue = []
Wizard = []
Fighter = []

#Create classes
##def racesetup():
  #  HumanRaces.append(Human)
   ##ElfRaces.append(HighElf)
    #ElfRaces.append(WoodElf)
    #DwarfRaces.append(HillDwarf)
   # DwarfRaces.append(MountainDwarf)
    #AvailableRaces.append(HumanRaces)
    #AvailableRaces.append(ElfRaces)
    #AvailableRaces.append(DwarfRaces)
    #for race in AvailableRaces:
     #   print(race)
      #  print("\n")

#Character Creation
def character_creation():
    Playername = input("What is the name of our hero?\n")
    Playerrace = input("Are you a Human, Elf or Dwarf\n")
    Playergender = input("Are you a male or a female?\n")
    Playerclass = input("Are you a Rogue, Fighter or Wizard?\n")
    Playerbackground = input("Are you a noble, sage or folk Hero?\n")
    Playeralignment = input("Are you good, bad or neutral?\n")
    Playerstats = input("give me stat numbers?\n")
    player = CharacterSheet(name=Playername, race=Playerrace, gender=Playergender, characterclass=Playerclass, background=Playerbackground, alignment=Playeralignment, stats=Playerstats)
    print(Playername + ", Welcome to Dungeons of Dragons.\n")
    pprint(vars(player))

#Print Character Info 
def charactersheetprint():
    print("Your name is: " + Charactersheet[0])
    print("Your sex is: " + Charactersheet[1])
    print("Your class is: " + Charactersheet[2])



#Rolls 6 stat numbers 
def rollstats():
    randomstat = []
    stat1 = random.randrange(3,18)
    while(stat1 < 8):
        stat1 = random.randrange(3,18)
    randomstat.append(stat1)
    stat2 = random.randrange(3,18)
    while(stat2 < 8):
        stat2 = random.randrange(3,18)
    randomstat.append(stat2)
    stat3 = random.randrange(3,18)
    while(stat3 < 8):
        stat3 = random.randrange(3,18)
    randomstat.append(stat3)
    stat4 = random.randrange(3,18)
    while(stat4 < 8):
        stat4 = random.randrange(3,18)
    randomstat.append(stat4)
    stat5 = random.randrange(3,18)
    while(stat5 < 8):
        stat5 = random.randrange(3,18)
    randomstat.append(stat5)
    stat6 = random.randrange(3,18)
    while(stat6 < 8):
        stat6 = random.randrange(3,18)
    randomstat.append(stat6)
    print("The Stat numbers rolled are:")
    for stat in randomstat:
        print(stat, end=' ')


def api():
  

    reqinput = input("What type of knowledge do you seek adventurer: ")
    response = requests.get("https://www.dnd5eapi.co/api/spells/" + reqinput)
    charquery = response.json()
    print(charquery)
    #prints the status code 
    print(response.status_code)
    if response.status_code == 404:
        reqinput = input("Sorry hero, that spell doesn't exist... try again: ")
        response = requests.get("https://www.dnd5eapi.co/api/spells/" + reqinput)
        charquery = response.json()
        print(charquery)

def api2():
    initialresponse = requests.get("https://www.dnd5eapi.co/api/")
    print(initialresponse.json())
    
    reqinput = input("What type of knowledge do you seek adventurer: ")
    reqinput = reqinput + "/"
    response = requests.get("https://www.dnd5eapi.co/api/" + reqinput)
    reqinput2 = input("What exact knowledge of " + reqinput + " do you seek adventurer: ")
    response = requests.get("https://www.dnd5eapi.co/api/" + reqinput + reqinput2)
    charquery = response.json()
    print(charquery)
    #prints the status code 
    print(response.status_code)
    if response.status_code == 404:
        reqinput = input("Sorry hero, that "+ reqinput +" doesn't exist... try again: ")
        response = requests.get("https://www.dnd5eapi.co/api/" + reqinput + reqinput2)
        charquery = response.json()
        print(charquery)
#Run
api2()
#rollstats()
#racesetup()
#character_creation()
#charactersheetprint()
