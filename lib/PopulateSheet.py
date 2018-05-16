#import settings
import xlwt

def initSheet(book, sheet):
    write = sheet.write
    boldon = "font: bold on"
    boldcenteron = "font: bold on; align: horiz center"
    bold = xlwt.easyxf(boldon)
    boldcenterbigon = "font: bold on, height 220; align: horiz center"
    boldcenterbig = xlwt.easyxf(boldcenterbigon)
    boldcenter = xlwt.easyxf(boldcenteron)
    centeron = "align: horiz center"
    center = xlwt.easyxf(centeron)
    fonton = "font: name Arial, height 200"
    font = xlwt.easyxf(fonton)

    for i in range(65):
        for j in range(43):
            write(i, j, style=font)


    write(0, 26, "Feats", style=bold)
    write(0, 29, "Notes", style=bold)
    write(0, 36, "Spells", style=bold)
    write(1, 1, "Character", style=bold)
    write(1, 7, "Player", style=bold)
    write(1, 19, "Campaign", style=bold)
    write(1, 36, "Domains / Specialities, Schools", style=bold)
    write(2, 13, "Dungeons and Dragons 3.5", style=boldcenterbig)
    write(3, 36, "Level", style=bold)
    write(3, 37, "Spell", style=boldcenter)
    write(4, 1, "Class", style=bold)
    write(4, 3, "Level", style=bold)
    write(4, 4, "Race", style=bold)
    write(4, 7, "Align", style=bold)
    write(4, 8, "Deity", style=bold)
    write(4, 13, "Character Records", style=center)
    write(4, 19, "Experience Points", style=bold)
    write(6, 19, "Gear", style = boldcenter)
    write(7, 1, "Size", style = bold)
    write(7, 2, "Age", style = bold)
    write(7, 3, "Gender", style = bold)
    write(7, 4, "Height", style = bold)
    write(7, 5, "Eyes", style = bold)
    write(7, 6, "Hair", style = bold)
    write(7, 7, "Skin", style = bold)
    write(7, 19, "Armor / Protect", style = bold)
    write(7, 21, "Type", style = bold)
    write(7, 22, "AC Bon", style = bold)
    write(7, 23, "Mx Dex", style = bold)
    write(9, 1, "Ability", style = bold)
    write(9, 2, "Score", style = bold)
    write(9, 3, "Mod", style = bold)
    write(9, 4, "T.Score", style = bold)
    write(9, 5, "T.Mod", style = bold)

    write(9, 7, "HP Mx", style = bold)
    healths = ['HP Mx', 'HP', 'Touch', 'FF']
    y = 0
    for i in range(9, 13):
        write(i, 7, '{}'.format(healths[y]), style = bold)
        y += 1

    write(9, 10, "Speed", style = bold)
    write(9, 11, "Init", style = bold)
    write(9, 19, "Check", style = bold)
    write(9, 20, "Spell", style = bold)
    write(9, 21, "Speed", style = bold)
    write(9, 22, "Weight", style = bold)
    write(9, 23, "Special Prop.", style = bold)

    abilities = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    y = 0
    for i in range(10, 16):
        write(i, 1, "{}".format(abilities[y]), style = bold)
        y += 1

    write(13, 19, "Shield / Protect", style = bold)
    write(13, 21, "AC Bon.", style = bold)
    write(13, 22, "Weight", style = bold)
    write(13, 23, "Check", style = bold)

    write(14, 7, "AC", style = bold)

    armorClass = ['AC', 'Total', 'Base', 'Armor', 'Shield',
        'Dex', 'Size', 'Nat', 'Deflect', 'Misc', 'Reduct']
    y = 0
    for i in range(7, 18):
        write(14, i, "{}".format(armorClass[y]), style = bold)
        y += 1

    write(15, 19, "Spell", style = bold)
    write(15, 20, "Special Properties", style = bold)
    write(15, 26, "Special Abilities", style = bold)
    write(15, 29, "Notes", style = bold)

    throws = ['Saving Throws', 'Total', 'Base', 'Mod', 'Magic',
        'Misc', 'Temp', 'Class', 'Skill Name', 'Ability', 'Skill',
        'Mod', 'Ranks', 'Skill']
    y = 0
    for i in range(1, 18):
        if i != 2 and i < 9:
            write(17, i, '{}'.format(throws[y]), style = bold)
            y += 1
        elif i > 8 and i != 9 and i < 12:
            write(17, i, '{}'.format(throws[y]), style = bold)
            y += 1
        elif i > 12:
            write(17, i, '{}'.format(throws[y]), style = bold)
            y += 1

    saves = ['Fortitude', 'Reflex', 'Will']
    y = 0
    for i in range(18, 21):
        write(i, 1, '{}'.format(saves[y]), style = bold)
        y += 1

    skills = ['Appraise', 'Balance', 'Bluff', 'Climb', 'Concentrate',
        'Craft 1', 'Craft 2', 'Craft 3', 'Decipher Script', 'Diplomacy',
        'Disable Device', 'Disguise', 'Escape Artist', 'Forgery',
        'Gather Info', 'Handle Animal', 'Heal', 'Hide', 'Intimidate',
        'Jump', 'Knowledge 1', 'Knowledge 2', 'Knowledge 3', 'Knowledge 4',
        'Knowledge 5', 'Listen', 'Move Silently', 'Open Lock', 'Perform 1',
        'Perform 2', 'Perform 3', 'Profession 1', 'Profession 2', 'Ride',
        'Search', 'Sense Motive', 'Sleight of Hand', 'Spellcraft', 'Spot',
        'Survival', 'Swim', 'Tumble', 'Use Magic Dev.', 'Use Rope',
        'Custom 1', 'Custom 2']
    y = 0
    for i in range(18, 64):
        write(i, 11, '{}'.format(skills[y]), style = bold)
        y += 1

    # This should be able to be compacted into a single code block
    protectives = ['Protective Item', 'AC Bon.', 'Weight', 'Check']
    y = 0
    for i in range(19, 24):
        if i < 20 or i > 20:
            write(19, i, '{}'.format(protectives[y]), style = bold)
            y += 1

    y = 0
    for i in range(19, 24):
        if i < 20 or i > 20:
            write(23, i, '{}'.format(protectives[y]), style = bold)
            y += 1

    write(22, 1, "Base Attack Bonus", style = bold)

    write(24, 1, "Grapple", style = bold)

    grapples = ['Total', 'BAB', 'STR', 'Size', 'Misc']
    y = 0
    for i in range(3, 8):
        write(25, i, '{}'.format(grapples[y]), style = bold)
        y += 1

    write(27, 19, 'Other Possessions', style = boldcenter)

    items = ['Item', 'Quant.', 'Pg.', 'Wt']
    y = 0
    for i in range(19, 25):
        if i < 20 or i > 21:
            write(28, i, '{}'.format(items[y]), style = bold)
            y += 1

    write(41, 26, "Languages", style = bold)
    write(41, 29, "Notes", style = bold)

    #49, 30
    dayspells = ['Level', 'Known', 'SaveDC', 'Per Day', 'Bonus']
    y = 0
    for i in range(30, 35):
        write(49, i, '{}'.format(dayspells[y]), style = bold)
        y += 1

    y = 0
    for i in range(50, 60):
        write(i, 30, '{}'.format(y), style = bold)
        y += 1

    write(50, 26, 'Money', style = boldcenter)

    monies = ['Copper', 'Silver', 'Gold', 'Platinum']
    y = 0
    for i in range(51, 55):
        write(i, 26, '{}'.format(monies[y]), style = bold)
        y += 1

    #61, 30
    spellsaves = ['Spell Save', 'Arcane Failure %', 'Cond. Mods']
    y = 0
    for i in range(61, 64):
        write(i, 30, '{}'.format(spellsaves[y]), style = bold)
        y += 1

    # weapon boxes
    for i in range(28, 59, 6):
        write(i, 1, "Attack", style = bold)
        write(i, 3, "Attack Bonus", style = bold)
        write(i, 5, "Damage", style = bold)
        write(i, 7, "Critical", style = bold)
        write(i+2, 1, "Range", style = bold)
        write(i+2, 2, "Type", style = bold)
        write(i+2, 3, "Notes", style = bold)

    # spell levels
    x = 0
    for i in range(4, 59, 6):
        write(i, 36, "{}".format(x), style=bold)
        x += 1

def fillSheet(book, sheet):

    write = sheet.write
    boldon = "font: bold on"
    boldcenteron = "font: bold on; align: horiz center"
    bold = xlwt.easyxf(boldon)
    boldcenterbigon = "font: bold on, height 220; align: horiz center"
    boldcenterbig = xlwt.easyxf(boldcenterbigon)
    boldcenter = xlwt.easyxf(boldcenteron)
    centeron = "align: horiz center"
    center = xlwt.easyxf(centeron)
    fonton = "font: name Arial, height 200"
    font = xlwt.easyxf(fonton)
