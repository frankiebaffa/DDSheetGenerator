import pathlib
import urllib.parse
import sqlite3

dbPath = 'db/DungeonPy.db'

def _path_to_uri(dbPath):
    path = pathlib.Path(dbPath)
    if path.is_absolute():
        return path.as_uri()
    return 'file:' + urllib.parse.quote(path.as_posix(), safe=':/')

def dbInit():
    try:
        conn = sqlite3.connect(_path_to_uri(dbPath) + '?mode=rw', uri=True)
    except sqlite3.OperationalError:
        conn = sqlite3.connect('db/DungeonPy.db')
        c = conn.cursor()
        ex = c.execute
        ex('''CREATE TABLE characters
            (ID text, Player text, Name text, Race text)''')
        conn.commit()
        ex('''CREATE TABLE class
            (PlayerID text, Name text, Level real, SkillPoints real)''')
        conn.commit()
        ex('''CREATE TABLE weaponry
            (ID text, PlayerID text, Name text, Damage text, Critical text,
            Range text, Type text, Notes text)''')
        conn.commit()
        ex('''CREATE TABLE items
            (ID text, PlayerID text, Name text)''')
        conn.commit()
        ex('''CREATE TABLE skills
            (PlayerID text, Appraise real, Balance real, Bluff real, Climb real,
            Concentrate real, Craft1Type text, Craft1 real, Craft2Type text,
            Craft2 real, Craft3Type text, Craft3 real, DecipherScript real,
            Diplomacy real, DisableDevice real, Disguise real,
            EscapeArtist real, Forgery real, GatherInfo real,
            HandleAnimal real, Heal real, Hide real, Intimidate real,
            Jump real, Knowledge1Type text, Knowledge1 real, Knowledge2Type text,
            Knowledge2 real, Knowledge3Type text, Knowledge3 real,
            Knowledge4Type text, Knowledge4 real, Knowledge5Type text,
            Knowledge5 real, Listen real, MoveSilently real, OpenLock real,
            Perform1Type text, Perform1 real, Perform2Type text, Perform2 real,
            Perform3Type text, Perform3 real, Profession1Type text,
            Profession1 real, Profession2Type text, Profession2 real,
            Ride real, Search real, SenseMotive real, SleightOfHand real,
            Spellcraft real, Spot real, Survival real, Swim real, Tumble real,
            UseMagicDevice real, UseRope real, Custom1Type text, Custom1 real,
            Custom2Type text, Custom2 real)''')
        conn.commit()

def dbAddNew(character):
    conn = sqlite3.connect('db/DungeonPy.db')
    c = conn.cursor()
    ex = c.execute

    charvalues = (str(character.id), character.player, character.name, character.characterclass.race)
    ex('INSERT INTO characters VALUES (?, ?, ?, ?)', charvalues)
    conn.commit()

def viewCharacters():
    conn = sqlite3.connect('db/DungeonPy.db')
    c = conn.cursor()
    ex = c.execute
    print('')
    for row in ex('SELECT Name, Race FROM characters ORDER BY Name'):
        print('{}'.format(row))
    print('')

def pickCharacter(book, sheet):
    conn = sqlite3.connect('db/DungeonPy.db')
    c = conn.cursor()
    ex = c.execute

    print('')
    y = 0
    for row in ex('SELECT Name, Race FROM characters ORDER BY Name'):
        print('{} - {}'.format(y, row))
        y += 1
    print('')

def dbClose():
    conn = sqlite3.connect('db/DungeonPy.db')
    conn.close()
