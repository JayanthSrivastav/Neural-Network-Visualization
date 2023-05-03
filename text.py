import pygame
#These is just the text being displayed on pygame window
infoX = 620
infoY = 50 
white = (255,255,255)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 15) 

text3 = font.render('S - Save', True, white)
text4 = font.render('L - Show/Hide Sensors', True, white)
text5 = font.render('R - Reset', True, white)
text6 = font.render('B - Show Only Best Car', True, white)
text7 = font.render('T -Infinite Traffic', True, white)
text3Rect = text3.get_rect().move(infoX,infoY )
text4Rect = text4.get_rect().move(infoX,infoY+2*text3Rect.height)
text5Rect = text5.get_rect().move(infoX,infoY+4*text3Rect.height)
text6Rect = text6.get_rect().move(infoX,infoY+6*text3Rect.height)
text7Rect = text7.get_rect().move(infoX,infoY+8*text3Rect.height)

def displayTexts(gameDisplay, generation, num_of_nnCars, alive, lines, showOnlyBestCar, it):  
    infotext1 = font.render('Gen: ' + str(generation), True, white) 
    infotext2 = font.render('Cars: ' + str(num_of_nnCars), True, white)
    infotext3 = font.render('Alive: ' + str(alive), True, white)
    infotext4 = font.render('Infinite Traffic: ' + str(it), True, white)
    infotext5 = font.render('Best Car: ' + str(showOnlyBestCar), True, white)
    
    if lines == True:
        infotext5 = font.render('Lines ON', True, white)
    else:
        infotext5 = font.render('Lines OFF', True, white)
    infotext1Rect = infotext1.get_rect().move(infoX,infoY+10*text3Rect.height)
    infotext2Rect = infotext2.get_rect().move(infoX,infoY+12*text3Rect.height)
    infotext3Rect = infotext3.get_rect().move(infoX,infoY+14*text3Rect.height)
    infotext4Rect = infotext4.get_rect().move(infoX,infoY+16*text4Rect.height)
    infotext5Rect = infotext5.get_rect().move(infoX,infoY+18*text3Rect.height)


    pygame.draw.rect(gameDisplay, (0,0,0), pygame.Rect(600,0,800,400))
    gameDisplay.blit(text3, text3Rect) 
    gameDisplay.blit(text4, text4Rect) 
    gameDisplay.blit(text5, text5Rect) 
    gameDisplay.blit(text6, text6Rect)
    gameDisplay.blit(text7, text7Rect) 
    gameDisplay.blit(infotext1, infotext1Rect)  
    gameDisplay.blit(infotext2, infotext2Rect)  
    gameDisplay.blit(infotext3, infotext3Rect) 
    gameDisplay.blit(infotext4, infotext4Rect) 
    gameDisplay.blit(infotext5, infotext5Rect) 

    return
 

