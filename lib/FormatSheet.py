#import settings
import xlwt

def initFormat(book, sheet):
    merge = sheet.merge
    # size all columns 1000
    for i in range(43):
        #width = 500 + i * 500
        sheet.col(i).width = 1500

    # merge (toprow, bottomrow, leftcolumn, rightcolumn)
    #   (0, 0) : (0, 63
    merge(0, 65, 0, 0)

    #   (1, 0) : (5, 0), (1, 1) : (5, 1), (1, 2) : (5, 2)
    for i in range(3):
        merge(i, i, 1, 5)
    #   (6, 0) : (6, 4)
    merge(0, 4, 6, 6)
    #   (7, 0) : (11, 0), (7, 1) : (11, 1), (7, 2) : (11, 2)
    for i in range(3):
        merge(i, i, 7, 11)
    #   (12, 0) : (12, 12)
    merge(0, 12, 12, 12)
    #   (13, 0) : (17, 1)
    merge(0, 1, 13, 17)
    #   (18, 0) : (18, 63)
    merge(0, 63, 18, 18)

    #   (13, 2) : (17, 3)
    merge(2, 3, 13, 17)
    #   (1, 3) : (2, 3)
    merge(3, 3, 1, 2)
    #   (4, 3) : (5, 3)
    merge(3, 3, 4, 5)
    #   (8, 3) : (10, 3)
    merge(3, 3, 8, 10)

    merge(3, 4, 11, 11)

    #   (1, 4) : (2, 4)
    merge(4, 4, 1, 2)
    #   (4, 4) : (5, 4)
    merge(4, 4, 4, 5)
    #   (8, 4) : (10, 4)
    merge(4, 4, 8, 10)
    #   (13, 4) : (17, 4)
    merge(4, 4, 13, 17)

    #   (1, 5) : (7, 5)
    merge(5, 5, 1, 7)
    #   (8, 5) : (11, 7)
    merge(5, 7, 8, 11)
    #   (13, 5) : (17, 12)
    merge(5, 12, 13, 17)

    #   (1, 8) : (11, 8)
    merge(8, 8, 1, 11)

    merge(9, 12, 9, 9)

    merge(11, 12, 10, 10)

    merge(11, 12, 11, 11)

    #   (6, 9) : (6, 15)
    merge(9, 15, 6, 6)

    #   (1, 10) : (11, 10)
    #merge(10, 10, 1, 11)

    #   (7, 13) : (17, 13)
    merge(13, 13, 7, 17)

    #   (7, 14) : (7, 15)
    merge(14, 15, 7, 7)

    #   (1, 16) : (17, 16)
    merge(16, 16, 1, 17)

    #   (1, 17) : (2, 17)
    for i in range(17, 21):
        merge(i, i, 1, 2)

    #   (9, 17) : (9, 63)
    merge(17, 63, 9, 9)

    #   (11, 17) : (12, 17)
    for i in range(17, 64):
        merge(i, i, 11, 12)

    #   (1, 21) : (8, 21)
    merge(21, 21, 1, 8)

    #   (1, 22) : (3, 22)
    merge(22, 22, 1, 3)

    #   (5, 22) : (8, 22)
    merge(22, 22, 5, 8)

    #   (1, 24) : (8, 24)
    merge(23, 23, 1, 8)

    #   (1, 24) : (2, 25)
    merge(24, 25, 1, 2)

    #   (8, 24) : (8, 25)
    merge(24, 25, 8, 8)

    #   (1, 26) : (8, 27)
    merge(26, 27, 1, 8)

    #   Weapon / Attack blocks
    #x = 28
    for x in range(28, 59, 6):
        for i in range(2):
            for j in range(1, 9, 2):
                merge(x+i, x+i, j, j+1)
        for i in range(2, 4):
            merge(x+i, x+i, 3, 8)
        merge(x+4, x+5, 1, 8)

    #   T = 19
    #   (19, 0) : (24, 0), (19, 6) : (24, 6)
    for i in range(7):
        merge(i, i, 19, 24)

    for i in range(7, 9):
        merge(i, i, 19, 20)

    merge(7, 8, 24, 24)

    for i in range(9, 11):
        merge(i, i, 23, 24)

    merge(11, 12, 19, 24)

    for i in range(13, 15):
        merge(i, i, 19, 20)

    merge(13, 14, 24, 24)

    for i in range(15, 17):
        merge(i, i, 20, 24)

    merge(17, 18, 19, 24)

    for i in range(19, 21):
        merge(i, i, 19, 20)

    merge(19, 26, 24, 24)

    merge(21, 22, 19, 23)

    for i in range(23, 25):
        merge(i, i, 19, 20)

    merge(25, 26, 19, 23)

    merge(27, 27, 19, 24)

    for i in range(28, 64):
        merge(i, i, 19, 21)

    #   (25, 0) : (25, 63)
    merge(0, 63, 25, 25)
    #   (26, 0) : (28, 0), (29, 0) : (33, 0)
    for i in range(13):
        merge(i, i, 26, 28)
        merge(i, i, 29, 33)

    # AA = 26
    merge(13, 14, 26, 33)

    for i in range(15, 39):
        merge(i, i, 26, 28)
        merge(i, i, 29, 33)

    merge(39, 40, 26, 33)

    for i in range(41, 48):
        merge(i, i, 26, 28)
        merge(i, i, 29, 33)

    merge(48, 49, 26, 28)

    merge(50, 50, 26, 28)

    for i in range(51, 55):
        merge(i, i, 27, 28)

    merge(55, 56, 26, 28)

    for i in range(57, 64):
        merge(i, i, 26, 27)

    merge(0, 48, 34, 35)

    merge(48, 63, 29, 29)

    for i in range(48, 61, 12):
        merge(i, i, 30, 33)

    for i in range(61, 64):
        merge(i, i, 30, 31)

    merge(61, 62, 33, 34)

    merge(63, 63, 32, 34)

    merge(49, 63, 35, 35)

    # AK = 36
    for i in range(3):
        merge(i, i, 36, 41)

    merge(3, 3, 37, 41)

    for i in range(4, 64, 6):
        merge(i, i+5, 36, 36)
        for j in range(i, i+6):
            merge(j, j, 37, 41)

    merge(0, 65, 42, 42)
    merge(64, 65, 1, 41)
