import os
import xlwt
import lib
import classes
import db
import methods
from methods import Create
from lib import settings
from lib import FormatSheet
from lib import PopulateSheet
from db import Database
from classes import CharacterClass

if not os.path.exists('Excel/'):
    os.makedirs('Excel/')

settings.init()
Database.dbInit()

progrun = True
while progrun == True:
    action = 0
    actioncheck = False
    while actioncheck == False:
        print('Would you like to:')
        print('1 - Create a new character?')
        print('2 - View your characters?')
        print('3 - Delete a character?')
        print('4 - Generate a sheet for an existing character?')
        print('5 - Generate a blank sheet?')
        print('6 - Exit?')
        print('')
        try:
            action = int(input('Pick one by number:  '))
        except:
            print('')
            print('Please pick one by its number.')
            print('')

        if action == 1 or action == 2 or action == 3 or action == 4 or action == 5 or action == 6:
            actioncheck = True
        else:
            print('')
            print('Please pick one by its number.')
            print('')

    if action == 1:
        methods.Create.CreateNew()
    elif action == 2:
        Database.viewCharacters()
    #elif action == 3:
        # delete logic here
    elif action == 4:
        Database.pickCharacter(settings.book, settings.sheet)
    elif action == 5:
        FormatSheet.initFormat(settings.book, settings.sheet)
        PopulateSheet.initSheet(settings.book, settings.sheet)
        settings.book.save('Excel/BlankSheet.xls')
    elif action == 6:
        print('')
        print('Exiting...')
        Database.dbClose()
        progrun = False
