import pickle
import os
import lib
from lib import settings

def viewCharacters():
    characterFiles = []
    characters = []

    for (dirpath, dirnames, filenames) in os.walk('Characters/'):
        characterFiles.extend(filenames)

    print('')
    for item in range(len(characterFiles)):
        file = 'Characters/' + characterFiles[item]
        object = open(file, 'rb')
        character = pickle.load(object)
        print('{} - {} - {} - {}'.format(character.name,
            character.characterclass.race, character.characterclass.classname,
            character.characterclass.level))
        object.close()
    print('')

def viewDetails(character):
    ab = character.ability
    #inventory[] = character.inventory
    print('')
    print('{} - {} - {} - {}'.format(character.name, character.characterclass.race,
        character.characterclass.classname, character.characterclass.level))
    print()
    print('Abilities:')
    print('Strength - {}'.format(ab.strength))
    print('Dexterity - {}'.format(ab.dexterity))
    print('Constitution - {}'.format(ab.constitution))
    print('Intelligence - {}'.format(ab.intelligence))
    print('Wisdom - {}'.format(ab.wisdom))
    print('Charisma - {}'.format(ab.charisma))
    print()

    print('Inventory:')
    for item in range(len(character.inventory)):
        print('{} - {}'.format(character.inventory[item].quantity, character.inventory[item].name))
    print()

    print('Skills:')
    allSkillKeys = list(character.characterclass.skills.__dict__.keys())
    allSkillValues = list(character.characterclass.skills.__dict__.values())

    for attr in range(len(character.characterclass.skills.__dict__.keys())):
        print('{} - {}'.format(allSkillKeys[attr], allSkillValues[attr]))
    print()
