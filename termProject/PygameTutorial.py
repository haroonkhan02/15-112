import pygame

class Pygame(class):
    
    def init(self):
        pass
        
    def mousePressed(self,x,y):
        pass
        
    def keyPressed(self,x,y):
        pass
    
    def mouseMoved(self):
        pass
    
    def timerFired(self):
        pass
    
    def redrawAll(self,screen):
        pass
    
    
    def run(width,height,fps=50): #fps=frames per sec
        pygame.init()
        clock=pygame.time.Clock()
        screen=pygame.display.set_mode((width,height))
        
        playing=True
        
        while playing:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing=False
                elif event.type== pygame.MOUSEBUTTONDOWN and event.button==1:
                    self.mousePressed(*event.pos)


####

class Dot(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        