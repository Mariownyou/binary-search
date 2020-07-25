import random
import pygame
import sys
from math import ceil

# pygame params
pygame.init()
screen = pygame.display.set_mode((900, 900))
screen.fill((255, 255, 255))

# variables
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 5

# settings
COLS = 10
ROW = ceil(len(arr) / COLS)
w = 800 / COLS
h = 800 / ROW
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)


class Cell:
    def __init__(self, x, y, n):
        self.i = x
        self.j = y
        self.number = str(n)
        self.blockSize = w
        self.is_choosen = False

    def __repr__(self):
        return 'Cell'

    def show(self):
        posOfRect = (self.i, self.j, self.blockSize, self.blockSize)
        posOfRectBorder = (self.i, self.j, self.blockSize, self.blockSize)
        if self.is_choosen:
            pygame.draw.rect(screen, GREEN, posOfRectBorder, 10)
        else:
            pygame.draw.rect(screen, BLACK, posOfRectBorder, 10)
        pygame.draw.rect(screen, WHITE, posOfRect)
        self.showText()
        pygame.display.update()

    def showText(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.number, True, BLACK)
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


def makeFormatedArray(a):
    amountOfArrays = len(a) // COLS
    last_array = len(a) % COLS
    formatedArray = [0 for i in range(amountOfArrays)]
    for i in range(amountOfArrays):
        formatedArray[i] = [0 for i in range(COLS)]
    if len(a) % COLS > 0:
        formatedArray.append([0 for i in range(last_array)])
    return formatedArray


def filArrayWithCells():
    listOfCells = [i for i in arr]
    x = 0
    y = 0
    for i in range(len(listOfCells)):
        listOfCells[i] = Cell(x, y, listOfCells[i])
    return listOfCells


def drawRect(a):
    cellsArray = makeFormatedArray(arr)
    x = 0
    y = 0
    step = w
    gap = 10
    index = 0
    for i in range(ROW):
        x = 5
        y += gap + i * step
        index = i * 10
        for j in range(len(cellsArray[i])):
            a[index].i = x
            a[index].j = y
            a[index].show()
            x += gap + step
            index += 1


drawRect(filArrayWithCells())


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    pygame.display.update()
