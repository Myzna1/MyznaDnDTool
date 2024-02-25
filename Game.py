#Imports
import array
import random

#Global Variables
Worldname = "Faerun"
Charactersheet = []
Characterinventory = []

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
    HumanRaces.append(Human)
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
def racesetup():
    HumanRaces.append(Human)
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











#Character Creation
def character_creation():
    Playername = input("What is the name of our hero?\n")
    Charactersheet.append(Playername)
    Playersex = input("Are you a male or a female?\n")
    Charactersheet.append(Playersex)
    Playerclass = input("Are you a Rogue, Fighter or Wizard?\n")
    Charactersheet.append(Playerclass)
    print(Playername + ", Welcome to Dungeons of Dragons.\n")

#Print Character Info 
def charactersheetprint():
    print("Your name is: " + Charactersheet[0])
    print("Your sex is: " + Charactersheet[1])
    print("Your class is: " + Charactersheet[2])



#Rolls 6 stat numbers 
def rollstats():
    stat1 = random.randrange(3,18)
    while(stat1 < 8):
        stat1 = random.randrange(3,18)
    print(stat1)
    stat2 = random.randrange(3,18)
    while(stat2 < 8):
        stat2 = random.randrange(3,18)
    print(stat2)
    stat3 = random.randrange(3,18)
    while(stat3 < 8):
        stat3 = random.randrange(3,18)
    print(stat3)
    stat4 = random.randrange(3,18)
    while(stat4 < 8):
        stat4 = random.randrange(3,18)
    print(stat4)
    stat5 = random.randrange(3,18)
    while(stat5 < 8):
        stat5 = random.randrange(3,18)
    print(stat5)
    stat6 = random.randrange(3,18)
    while(stat6 < 8):
        stat6 = random.randrange(3,18)
    print(stat6)
#Run
#rollstats()
#racesetup()
#character_creation()
#charactersheetprint()