import xlwt

def init():
    global book
    book = xlwt.Workbook(encoding = "utf-8")

    global sheet
    sheet = book.add_sheet("Sheet 1", cell_overwrite_ok=True)

    global classlist
    classlist = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
        'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']

    global racelist
    racelist = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc',
        'Halfling']

    global skillList

    skillList = ['Appraise', 'Balance', 'Bluff', 'Climb', 'Concentrate', 'Craft1Type', 'Craft1',
        'Craft2Type', 'Craft2', 'Craft3Type', 'Craft3', 'DecipherScript', 'Diplomacy', 'DisableDevice',
        'Disguise', 'EscapeArtist', 'Forgery', 'GatherInfo', 'HandleAnimal', 'Heal', 'Hide',
        'Intimidate', 'Jump', 'Knowledge1Type', 'Knowledge1', 'Knowledge2Type', 'Knowledge2',
        'Knowledge3Type', 'Knowledge3', 'Knowledge4Type', 'Knowledge4', 'Knowledge5Type',
        'Knowledge5', 'Listen', 'MoveSilently', 'OpenLock', 'Perform1Type', 'Perform1',
        'Perform2Type', 'Perform2', 'Perform3Type', 'Perform3', 'Profession1Type', 'Profession1',
        'Profession2Type', 'Profession2', 'Ride', 'Search', 'SenseMotive', 'SleightOfHand',
        'Spellcraft', 'Spot', 'Survival', 'Swim', 'Tumble', 'UseMagicDevice', 'UseRope', 'Custom1type',
        'Custom1', 'Custom2Type', 'Custom2']
