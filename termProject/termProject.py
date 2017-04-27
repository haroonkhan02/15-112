import pygame
import datetime
import time

class PygameGame(object):
    def init(self):
        self.brushColor=(0,0,0)
        self.brushRad=5
        self.currPosition=None
        self.brush=[]
        self.eraser=[]
        self.mode="brushMode"
        self.brushSlider=(70,505)
        self.dragBrushSlider=False
        self.wentEraserMode=False
        self.isImageSaved=False
        self.undo=[]

    def mousePressed(self, x, y):
        if 50> x > 10 and 90> y > 50:       #click brush button
            self.mode="brushMode"
        if self.brushSlider[0] +25/2 >x >self.brushSlider[0] -25/2 and\
        self.brushSlider[1] +25/2 >y >self.brushSlider[1]-25/2:
            self.dragBrushSlider=True
        if 140>x>10 and 790>y>660:      #get brush color
            self.currPosition= (x,y)
        if 85+50 > x >50 and 100 > y > 50:
            self.mode="eraserMode" 
        if 720+50 >x>720 and 60>y>10:
            self.isImageSaved=True
        
    def mouseReleased(self, x, y):
        if self.dragBrushSlider==True:
           self.dragBrushSlider=False 

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        if x>150 and y>60:      #drawing brush strokes
            if self.mode=="brushMode":
                self.lastColor=self.brushColor
                if self.wentEraserMode==True:
                    self.brushColor=self.lastColor
                self.brush.append((x,y,self.brushRad,self.brushColor))
            if self.mode=="eraserMode":
                self.wentEraserMode=True
                self.brushColor=(255,255,255)
                self.brush.append((x,y,self.brushRad,self.brushColor))
        if self.dragBrushSlider:        #brush slider
            if self.brushSlider[0]>=20 and self.brushSlider[0]<=130:
                if x>self.brushSlider[0]:
                    self.brushRad+=1
                if x<self.brushSlider[0] and self.brushRad>0:
                    self.brushRad-=1
                self.brushSlider= (x,self.brushSlider[1])
            if self.brushSlider[0]>=135:
                self.brushSlider= (130,self.brushSlider[1])
            if  self.brushSlider[0]<=15:
                self.brushSlider= (20,self.brushSlider[1])
            
    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def getLayout(self,screen):
        pygame.draw.rect(screen,(32,32,32),(0,0,150,self.height)) #vert
        pygame.draw.rect(screen,(32,32,32),(0,0,self.width,60))    #horiz
        self.getText(screen)
        self.getButtons(screen)
        self.drawBrush(screen)
        if self.mode=="brushMode":
            self.brushSizeSlider(screen)
            self.getBrushColor(screen)
        if self.mode=="eraserMode":
            self.brushSizeSlider(screen)

    def getButtons(self,screen):
        self.brushButton(screen)
        self.eraserButton(screen)
        self.saveImageButton(screen)
        self.undoButton(screen)
        self.redoButton(screen)
        if self.isImageSaved==True:
            self.saveImage(screen)
     
    def undoButton(self,screen): 
        pygame.draw.rect(screen,(128,128,128),(660,10,45,45))
        save= pygame.image.load('undo.png')
        save= pygame.transform.scale(save,(45,45))
        screen.blit(save,(660,10))

    def redoButton(self,screen): 
        pygame.draw.rect(screen,(128,128,128),(600,10,45,45))
        save= pygame.image.load('undo.png')
        save= pygame.transform.flip(save,True,False)
        save= pygame.transform.scale(save,(45,45))
        screen.blit(save,(600,10))
        
    def saveImageButton(self,screen):
        pygame.draw.rect(screen,(128,128,128),(720,10,45,45))
        save= pygame.image.load('save.png')
        save= pygame.transform.scale(save,(45,45))
        screen.blit(save,(720,10))
    
    def eraserButton(self,screen):
        if self.mode=="eraserMode":
            pygame.draw.rect(screen,(255,153,255),(85,50,50,50))
        else:
            pygame.draw.rect(screen,(128,128,128),(85,50,50,50))
        eraser= pygame.image.load('eraser.png')
        eraser= pygame.transform.scale(eraser,(50,50))
        screen.blit(eraser,(85,50))
        
    def brushButton(self,screen):
        if self.mode=="brushMode":
            pygame.draw.rect(screen,(255,153,255),(20,50,50,50))
        else:
            pygame.draw.rect(screen,(128,128,128),(20,50,50,50))
        brushSymbol= pygame.image.load('pen.png')
        brushSymbol= pygame.transform.scale(brushSymbol,(50,50))
        screen.blit(brushSymbol,(20,50))

    def drawBrush(self,screen):
        for i in self.brush:
            x,y,rad,color= i
            pygame.draw.circle(screen,color,(x,y),rad)
    
    def brushSizeSlider(self,screen):
        pygame.draw.rect(screen,(192,192,192),(20,500,110,10))
        pygame.draw.circle(screen,(128,128,128),self.brushSlider,12)
        pygame.font.init()
        font= pygame.font.SysFont('Cambria',25)
        if self.mode=="brushMode":
            textsurface= font.render('- Brush Size +',False,(255,255,255))
        if self.mode=="eraserMode":
            textsurface= font.render('- Eraser Size +',False,(255,255,255))
        screen.blit(textsurface,(20,520))
    
    def getBrushColor(self,screen):
        wheel= pygame.image.load('color.jpg')
        wheel= pygame.transform.scale(wheel,(130,130))
        screen.blit(wheel,(10,660))
        if self.currPosition!=None:
            self.brushColor=screen.get_at(self.currPosition)

    def getText(self,screen):
        pygame.font.init()
        font= pygame.font.SysFont('Cambria',50)
        textsurface= font.render('Paint 112',False,(0,153,153))
        screen.blit(textsurface,(self.width/2-50,0))
     
    def saveImage(self,screen):
        self.isImageSaved=False
        getTime=time.asctime(time.localtime(time.time()))
        getTime=getTime.replace(" ", "_")
        getTime= getTime.replace(":",".")
        saveFile= "c:\Desktop\15-112\termProject.py" + getTime+ ".jpg"
        pygame.image.save(screen, saveFile)
        pygame.font.init()
        font= pygame.font.SysFont('Cambria',30)
        textsurface= font.render('Saved' ,False,(0,0,0))
        screen.blit(textsurface,(715,65))

    def redrawAll(self, screen):
        self.getLayout(screen)

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=800, height=800, fps=100, title="Paint 112"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()

#framework from: https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py