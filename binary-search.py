import random
import pygame
import sys
import os


pygame.init() 
screen = pygame.display.set_mode((800, 800))
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = 5

COLS = 10
ROW = 10
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
        return 'class Cell'

    def show(self):
        pygame.draw.rect(screen, WHITE, (self.i, self.j, self.blockSize, self.blockSize))
        self.showText()
        pygame.display.update()

    def showText(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.number, True, BLUE) 
        font_w, font_h = text.get_size()

        # распологаем в центре текст
        text_x = self.i + (self.blockSize - font_w)  / 2
        text_y = self.j + (self.blockSize - font_h)  / 2
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
   return quicksort(l_nums) + e_nums + quicksort(b_nums)


answer = binarySearch(n)
print(answer)

cell1 = Cell(100, 100, 10)
cell2 = Cell(210, 100, 12)
cell1.show()
cell2.show()

cells = [[] for i in range(len(arr))]
for i in range(COLS):
    for j in range(ROW):
        cells[i] = Cell(i*50, 10, arr[i])
        cells[i].show()

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    pygame.display.update()
