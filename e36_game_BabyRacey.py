#copied heavily from "https://pythonprogramming.net/pygame-python-3-part-1-intro/"
import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

car_width = 73
block_color = (53, 115, 255)


gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Baby Racey')
clock = pygame.time.Clock()    #use this to track time within the game, and this is mostly used for FPS, or "frames per second."
carimg = pygame.image.load('resources/car.png')    #same directory as python opened

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Baby Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 350, 400, 100, 50, green, white, game_loop)

        pygame.display.update()
        clock.tick(15)

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+ str(count), True, black)
	gameDisplay.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
	gameDisplay.blit(carimg, (x, y))    #"Blit" basically just draws the image to the screen
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()    #using .get_rect() to get the rectangle that is somewhat invisible, so we can reference it and center the text.

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 80)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	
	pygame.display.update()
	
	time.sleep(2)

	game_loop()

def crash():
	message_display('You Crashed')

def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.85)
	
	x_change = 0

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height =100

	thingCount = 1
	dodged = 0
	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()			

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -10
				elif event.key == pygame.K_RIGHT:
					x_change = 10
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change
		gameDisplay.fill(white)

		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed
		car(x, y)
		things_dodged(dodged)

		if x > display_width - car_width or x < 0:
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged *1.31)

		if y < thing_starty + thing_height:
			print 'y croosover'
			
			if x > thing_startx and x < thing_startx + thing_width or x+ car_width > thing_startx and x + car_width < thing_startx + thing_width:
				print 'x crossover'
				crash()


		pygame.display.update()    #Display.flip will update the entire surface. Basically the entire screen. Display.update can just update specific areas of the screen.
		clock.tick(60)    #how many frames per second we are running. In this case, we are running 60 FPS.

game_intro()
game_loop()
pygame.quit()
quit()

