import classes
from classes import CharacterClass
import pickle
import os
import lib
from lib import settings

def pickCharacter():
    characterFiles = []

    for (dirpath, dirnames, filenames) in os.walk('Characters/'):
        characterFiles.extend(filenames)

    print('')
    for item in range(len(characterFiles)):
        file = 'Characters/' + characterFiles[item]
        object = open(file, 'rb')
        character = pickle.load(object)
        print('{} - {} - {} - {} - {}'.format(item, character.name,
            character.characterclass.race, character.characterclass.classname,
            character.characterclass.level))
        object.close()
    print('')

    characterPick = 0
    file = ''
    checkPick = False
    while checkPick == False:
        try:
            characterPick = int(input('Pick character by number  '))
            file = 'Characters/' + characterFiles[characterPick]
            object = open(file, 'rb')
            character = pickle.load(object)
            checkPick = True
            object.close()
            return character
        except:
            print('')
            print('Please enter the corresponding number.')
            print('')

def editCharacterMenu(character):
    editRun = True
    while editRun == True:
        action = 0
        actioncheck = False
        while actioncheck == False:
            print('Would you like to:')
            print('1 - Change character ability scores?')
            print('2 - Change skill ranks?')
            print('3 - Add/Remove item?')
            print('4 - Add weaponry?')
            print('5 - Exit?')
            print('')
            try:
                action = int(input('Pick one by number:  '))
            except:
                print('')
                print('Please pick one by its number.')
                print('')

            if action == 1 or action == 2 or action == 3 or action == 4 or action == 5:
                actioncheck = True
            else:
                print('')
                print('Please pick one by its number.')
                print('')
        if action == 1:
            Scores(character)
        elif action == 2:
            EditSkills(character)
        elif action == 3:
            AddInventory(character)
        #elif action == 4:

        elif action == 5:
            editRun = False
            print()

def Scores(character):
    ab = character.ability
    ab.strength = int(input('Enter strength:  '))
    ab.dexterity = int(input('Enter dexterity '))
    ab.constitution = int(input('Enter constitution  '))
    ab.intelligence = int(input('Enter intelligence  '))
    ab.wisdom = int(input('Enter wisdom  '))
    ab.charisma  = int(input('Enter charisma  '))

    file = 'Characters/' + character.name
    os.remove(file)
    object = open(file, 'wb')
    pickle.dump(character, object)
    object.close()

def AddInventory(character):
    file = 'Characters/' + character.name
    name = input('Name of item?')

    # Add exception handling
    quantity = int(input('How many?'))

    itemdup = 0
    item = None
    for i in range(len(character.inventory)):
        if name.replace(" ", "").lower() == character.inventory[i].name.replace(" ", "").lower():
            itemdup += 1
            item = character.inventory[i]
    if itemdup > 0:
        item.quantity += quantity
    else:
        character.inventory.append(classes.CharacterClass.Item(name, quantity))
    os.remove(file)
    object = open(file, 'wb')
    pickle.dump(character, object)
    object.close()

def EditSkills(character):
    allSkills = character.characterclass.skills.__dict__.keys()
    allSkillsList = list(allSkills)

    skill = input('Enter the skill you wish to change:  ')

    skillCheck = False
    while skillCheck == False:
        for attr in range(len(allSkillsList)):
            if skill.replace(" ", "").lower() == allSkillsList[attr].lower():
                print('')
                print('{}'.format(allSkillsList[attr]))
                print('')
                skillPick = allSkillsList[attr]
                skillCheck = True
                break

    skillGrab = getattr(character.characterclass.skills, skillPick)
    if isinstance(skillGrab, int):
        skillValue = int(input('Enter the total ranks in skill:  '))
        setattr(character.characterclass.skills, skillPick, skillValue)
        print()
        print('{} - {}'.format(skillPick, skillGrab))
        print()
    elif isinstance(skillGrab, dict):
        k, v = next(iter(skillGrab.items()))
        print('{} is set as {}'.format(skillPick, skillGrab))
        del skillGrab[k]
        skillKey = input('Enter the type of {}:  '.format(skillPick[:-1]))
        skillValue = int(input('Enter the total ranks in skill:  '))
        skillGrab[skillKey] = skillValue
        print()
        print('{} - {}'.format(skillPick, skillGrab))
        print()

    file = 'Characters/' + character.name
    os.remove(file)
    object = open(file, 'wb')
    pickle.dump(character, object)
    object.close()
