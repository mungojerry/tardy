
from PIL import Image

# def inputNumber(message, name):
#   while True:
#     try:
#        userInput = int(input(message))       
#     except ValueError:
#        print("Not a number "+name+"! Try again please.")
#        continue
#     else:
#        return userInput 
#        break 

# msg = 3+7

# print(msg)

# print('Enter your name:')
# name = input()


# numTimes = inputNumber('How many times do you want to print?', name)

# print()
# print('-----------------------')
# print()

# for i in range(numTimes):  
#   if i == 0:
#     print('Hello, ' + name + '.')
#   else:
#     print('Hello again, ' + name + '.')
  
from random import randrange
import pygame

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tardy tardigrade')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('car.png')

carImg = pygame.transform.smoothscale(carImg, (75, 75))

bg = pygame.image.load('bg.jpg')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x = carImg.get_width()
y = -carImg.get_height()/2
angle=0

vx = 2
vy = 2

dvdEffect = False
rotate = False
randColor = (randrange(255), randrange(255), randrange(255))
while not crashed:
    angle=angle+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                vy = -6
                vx = (5, -5)[pygame.mouse.get_pos()[0]<x]


    if (angle/10)%2==0:
      randColor = (randrange(255), randrange(255), randrange(255))
    gameDisplay.blit(bg, (0,0))
    mouse_pos = pygame.mouse.get_pos()
   
    x = x + vx
    y = y + vy

    if y > display_height-(carImg.get_height()):
       y = display_height-(carImg.get_height())
       vy = -vy
       vy *= 0.9
       vx *= 0.9
    if y < (carImg.get_height()):
       y = (carImg.get_height())
       vy = -vy

    if not dvdEffect:
      vy += 0.2

    if x > display_width-(carImg.get_width()):
        x = display_width-(carImg.get_width())
        vx = -vx
        vx *= 0.9
    if x < 0:
        x = 0
        vx = -vx
        vx *= 0.9

    if rotate:
        gameDisplay.blit( pygame.transform.rotate(carImg, angle), (x, y))
    else:
        gameDisplay.blit( carImg, (x, y))
    pygame.display.update()

    

    clock.tick(160)

pygame.quit()
quit()

