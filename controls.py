import pygame

class Controls:

    def __init__(self, type):
        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False
        self.type = type
    
    def listenToKeyboard(self):
        if self.type == "DUMMY":
            self.forward = True
            return
        elif self.type == "AI":
            return
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
