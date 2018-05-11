import uuid

class Character:
    def __init__(self, name, characterclass, player, race, classlist, racelist):
        self.id = uuid.uuid4()
        self.name = name
        self.characterclass = PrimaryClass(self.id, characterclass, race, classlist, racelist)
        self.player = player

    def AddItem(name):
        id = self.id
        Item(id, name)

    def AddWeapon(name, damage, critical, range, type, notes):
        id = self.id
        Weaponry(id, name, damage, critical, range, type, notes)

class PrimaryClass:
    def __init__(self, id, classname, race, classlist, racelist):
        self.id = id

        for i in range(len(racelist)):
            if race == racelist[i]:
                self.race = race

        for i in range(len(classlist)):
            if classname == classlist[i]:
                self.classname = classname

        self.level = 1
        self.skillpoints = 0
        self.skills = Skills(self.id)

class Item:
    def __init__(self, playerid, name):
        self.id = uuid.uuid4()
        self.playerid = playerid
        self.name = name

class Weaponry:
    def __init__(self, playerid, name, damage, critical, range, type, notes):
        self.id = uuid.uuid4()
        self.playerid = playerid
        self.name = name
        self.damage = damage
        self.critical = critical
        self.range = range
        self.type = type
        self.notes = notes

class Skills:
    def __init__(self, id):
        self.playerid = id
        self.Appraise = 0
        self.Balance = 0
        self.Bluff = 0
        self.Climb = 0
        self.Concentrate = 0
        self.Craft1 = {'':0}
        self.Craft2 = {'':0}
        self.Craft3 = {'':0}
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
        self.Knowledge1 = {'':0}
        self.Knowledge2 = {'':0}
        self.Knowledge3 = {'':0}
        self.Knowledge4 = {'':0}
        self.Knowledge5 = {'':0}
        self.Listen = 0
        self.MoveSilently = 0
        self.OpenLock = 0
        self.Perform1 = {'':0}
        self.Perform2 = {'':0}
        self.Perform3 = {'':0}
        self.Profession1 = {'':0}
        self.Profession2 = {'':0}
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
        self.Custom1 = {'':0}
        self.Custom2 = {'':0}
