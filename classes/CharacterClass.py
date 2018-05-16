import pickle
import lib
from lib import settings

class Character:
    def __init__(self, name, characterclass, player, race, classlist, racelist):
        self.name = name
        self.characterclass = PrimaryClass(characterclass, race, classlist, racelist)
        self.player = player
        self.ability = Ability()
        self.inventory = []
        self.weaponry = []

    def AddItem(name, quantity):
        self.inventory.append(Item(name, quantity))

    def AddWeapon(slot, name, damage, critical, range, type, notes):
        self.weaponry.append(Weaponry(name, damage, critical, range, type, notes))

class PrimaryClass:
    def __init__(self, classname, race, classlist, racelist):

        for i in range(len(racelist)):
            if race == racelist[i]:
                self.race = race

        for i in range(len(classlist)):
            if classname == classlist[i]:
                self.classname = classname

        self.level = 1
        self.skillpoints = 0
        self.skills = Skills()

class Ability:
    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def __iter__(self):
        return self

class Weaponry:
    def __init__(self, name, damage, critical, range, type, notes):
        self.name = name
        self.damage = damage
        self.critical = critical
        self.range = range
        self.type = type
        self.notes = notes
    def __iter__(self):
        return self

class Skills:
    def __init__(self):
        self.Appraise = 0
        self.Balance = 0
        self.Bluff = 0
        self.Climb = 0
        self.Concentrate = 0
        self.Craft1 = {'': 0}
        self.Craft2 = {'': 0}
        self.Craft3 = {'': 0}
        self.DecipherScript = 0
        self.Diplomacy = 0
        self.DisableDevice = 0
        self.Disguise = 0
        self.EscapeArtist = 0
        self.Forgery = 0
        self.GatherInfo = 0
        self.HandleAnimal = 0
        self.Heal = 0
        self.Hide = 0
        self.Intimidate = 0
        self.Jump = 0
        self.Knowledge1 = {'': 0}
        self.Knowledge2 = {'': 0}
        self.Knowledge3 = {'': 0}
        self.Knowledge4 = {'': 0}
        self.Knowledge5 = {'': 0}
        self.Listen = 0
        self.MoveSilently = 0
        self.OpenLock = 0
        self.Perform1 = {'': 0}
        self.Perform2 = {'': 0}
        self.Perform3 = {'': 0}
        self.Profession1 = {'': 0}
        self.Profession2 = {'': 0}
        self.Ride = 0
        self.Search = 0
        self.SenseMotive = 0
        self.SleightOfHand = 0
        self.Spellcraft = 0
        self.Spot = 0
        self.Survival = 0
        self.Swim = 0
        self.Tumble = 0
        self.UseMagicDevice = 0
        self.UseRope = 0
        self.Custom1 = {'': 0}
        self.Custom2 = {'': 0}

    def __iter__(self):
        return self
