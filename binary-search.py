import random
import pygame
import sys
from math import ceil

# pygame params
pygame.init()
screen = pygame.display.set_mode((800, 800))

# variables
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1]
n = 5

# settings
COLS = 10
ROW = ceil(len(arr) / COLS)
w = 800 / COLS
h = 800 / ROW
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)


class Cell:
    def __init__(self, x, y, n):
        self.i = x
        self.j = y
        self.number = str(n)
        self.blockSize = 50

    def __repr__(self):
        return 'Cell'

    def show(self):
        posOfRect = (self.i, self.j, self.blockSize, self.blockSize)
        pygame.draw.rect(screen, WHITE, posOfRect)
        self.showText()
        pygame.display.update()

    def showText(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.number, True, BLUE)
        font_w, font_h = text.get_size()

        # распологаем в центре текст
        text_x = self.i + (self.blockSize - font_w) / 2
        text_y = self.j + (self.blockSize - font_h) / 2
        screen.blit(text, (text_x, text_y))


def binarySearch(n):
    array = quickSort(arr)
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] < n:
            low = mid + 1
        elif array[mid] > n:
            high = mid - 1
        else:
            print(array)
            return mid
    return 'try again'


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
    l_nums = [n for n in arr if n < q]
    e_nums = [q] * arr.count(q)
    b_nums = [n for n in arr if n > q]
    return quickSort(l_nums) + e_nums + quickSort(b_nums)


cell1 = Cell(100, 100, 10)
cell2 = Cell(210, 100, 12)
cell1.show()
cell2.show()


def makeFormatedArray(a):
    amountOfArrays = len(a) // COLS
    last_array = len(a) % COLS
    formatedArray = [0 for i in range(amountOfArrays)]
    for i in range(amountOfArrays):
        formatedArray[i] = [0 for i in range(COLS)]
    if len(a) % COLS > 0:
        formatedArray.append([0 for i in range(last_array)])
    return formatedArray


def filFormatedArray():
    filledArray = makeFormatedArray(arr)
    for i in range(ROW):
        index = 10 * i
        for j in range(len(filledArray[i])):
            filledArray[i][j] = arr[index]
            index += 1
    return filledArray


filFormatedArray()


def fill():
    cells = [0 for i in range(ROW)]
    for i in range(ROW):
        cells[i] = [0 for i in range(COLS)]
    print(cells)

    for i in range(ROW):
        for j in range(COLS):
            if i < 1:
                print(f'j= {j}, i = {i}')
                cells[i][j] = Cell(j*50, 10, arr[j])
            else:
                cells[i][j] = Cell(j*50, 100, arr[j])
            cells[i][j].show()
    print(cells)


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    pygame.display.update()
