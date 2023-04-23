import pygame

class Controls:

    def __init__(self):
        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False
    
    def listenToKeyboard(self):
        keys = pygame.key.get_pressed()
        
        # Right
        if keys[pygame.K_RIGHT]:
            self.right = True
        else:
            self.right = False
        
        # Left
        if keys[pygame.K_LEFT]:
            self.left = True
        else:
            self.left = False

        # Forward
        if keys[pygame.K_UP]:
            self.forward = True
        else:
            self.forward = False

        # Reverse
        if keys[pygame.K_DOWN]:
            self.reverse = True
        else:
            self.reverse = False
        
    def resetKeys(self):
        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False
