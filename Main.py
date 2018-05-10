import os
import xlwt
import lib
from lib.settings import *
from lib.FormatSpreadSheet import *
from lib.PopulateSheet import *

if not os.path.exists('Excel/'):
    os.makedirs('Excel/')

lib.settings.init()

#bookName = input("Name Your Sheet...  ")
bookName = 'test.xls'

initFormat(lib.settings.book, lib.settings.sheet)

initSheet(lib.settings.book, lib.settings.sheet)

lib.settings.book.save('Excel/' + bookName)# + '.xls')
