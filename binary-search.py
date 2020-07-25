import random
import pygame
import sys
from math import ceil
from time import sleep

# pygame params
pygame.init()
screen = pygame.display.set_mode((900, 900))
screen.fill((255, 255, 255))

# variables
arr = [1, 4, 3, 7, 1, 2, 5, 3, 2, 8, 33, 1, 8, 9, 3]
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
        self.number = int(n)
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
        text = font.render(str(self.number), True, BLACK)
        font_w, font_h = text.get_size()

        # распологаем в центре текст
        text_x = self.i + (self.blockSize - font_w) / 2
        text_y = self.j + (self.blockSize - font_h) / 2
        screen.blit(text, (text_x, text_y))


def makeFormatedArray(arr):
    amountOfArrays = len(arr) // COLS
    last_array = len(arr) % COLS
    formatedArray = [0 for i in range(amountOfArrays)]
    for i in range(amountOfArrays):
        formatedArray[i] = [0 for i in range(COLS)]
    if len(arr) % COLS > 0:
        formatedArray.append([0 for i in range(last_array)])
    return formatedArray


def filArrayWithCells():
    listOfCells = [i for i in arr]
    x = 0
    y = 0
    for i in range(len(listOfCells)):
        listOfCells[i] = Cell(x, y, listOfCells[i])
    return listOfCells


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
    a = filArrayWithCells()
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(a)
        q.is_choosen = True
        print(q.number)
    l_nums = [n for n in arr if n < q.number]
    e_nums = [q.number] * arr.count(q.number)
    b_nums = [n for n in arr if n > q.number]
    drawRect(a)
    return quickSort(l_nums) + e_nums + quickSort(b_nums)


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

quickSort(arr)

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    pygame.display.update()
