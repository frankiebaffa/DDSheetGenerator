import pickle
import os
import xlwt
import lib
import classes
import db
from lib import settings
from lib import FormatSheet
from lib import PopulateSheet
from db import Database
from classes import CharacterClass
import lib
from lib import settings

def CreateNew():
    bookName = 'test'
    classlist = settings.classlist
    racelist = settings.racelist

    player = input('Who is playing the character?  ')
    characterName = input('What is the name of your character?  ')

    classcheck = False
    while classcheck == False:
        y = 0
        for i in range(len(classlist)):
            print('{} - {}'.format(y, classlist[i]))
            y += 1
        classaction = input('Pick a class for your character by number:  ')
        try:
            classaction = int(classaction)
            characterClass = classlist[classaction]
            classcheck = True
            print('')
        except:
            print('Please pick a listed number.')
            print('')

    racecheck = False
    while racecheck == False:
        y = 0
        for i in range(len(racelist)):
            print('{} - {}'.format(y, racelist[i]))
            y += 1
        raceaction = input('Pick a race for your character by number:  ')
        try:
            raceaction = int(raceaction)
            race = racelist[raceaction]
            racecheck = True
            print('')
        except:
            print('Please pick a listed number.')
            print('')

    character = CharacterClass.Character(characterName, characterClass, player,
        race, classlist, racelist)

    file = 'Characters/' + character.name
    object = open(file, 'wb')
    pickle.dump(character, object)
    object.close()
