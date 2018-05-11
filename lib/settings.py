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
