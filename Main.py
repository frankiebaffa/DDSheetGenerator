import os
import xlwt
import lib
import classes
import methods
from methods import Create
from methods import View
from methods import Edit
from lib import settings
from lib import FormatSheet
from lib import PopulateSheet
from classes import CharacterClass
import pickle

if not os.path.exists('Excel/'):
    os.makedirs('Excel/')
if not os.path.exists('Characters/'):
    os.makedirs('Characters/')

settings.init()

def LoadCharacter():
    characterName = input("Which character do you want to load?")
    object = open('Characters/' + characterName, 'rb')
    character = pickle.load(object)
    print('{} {}'.format(character.name, character.characterclass.race))


progrun = True
while progrun == True:
    action = 0
    actioncheck = False
    while actioncheck == False:
        print('Would you like to:')
        print('1 - Create a new character?')
        print('2 - Edit a character?')
        print('3 - View your characters?')
        print('4 - View character details?')
        print('5 - Delete a character?')
        print('6 - Generate a sheet for an existing character?')
        print('7 - Generate a blank sheet?')
        print('8 - Exit?')
        print('')
        try:
            action = int(input('Pick one by number:  '))
        except:
            print('')
            print('Please pick one by its number.')
            print('')

        if action == 1 or action == 2 or action == 3 or action == 4 or action == 5 or action == 6 or action == 7 or action == 8:
            actioncheck = True
        else:
            print('')
            print('Please pick one by its number.')
            print('')

    if action == 1:
        methods.Create.CreateNew()
    elif action == 2:
        character = methods.Edit.pickCharacter()
        methods.Edit.editCharacterMenu(character)
    elif action == 3:
        methods.View.viewCharacters()
    elif action == 4:
        character = methods.Edit.pickCharacter()
        methods.View.viewDetails(character)
    #elif action == 5:
        # delete logic here
    elif action == 6:
        Database.pickCharacter(settings.book, settings.sheet)
    elif action == 7:
        FormatSheet.initFormat(settings.book, settings.sheet)
        PopulateSheet.initSheet(settings.book, settings.sheet)
        settings.book.save('Excel/BlankSheet.xls')
    elif action == 8:
        print('')
        print('Exiting...')
        progrun = False
