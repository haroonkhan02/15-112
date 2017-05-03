import pygame
import datetime
import time
import math
import random

class PygameGame(object):
    def init(self):
        self.brushColor=(0,0,0)
        self.brushRad=7
        self.currPosition=None
        self.currPositionbrsh= None
        self.brush=self.lastBrushDot=[]
        self.eraser=[]
        self.mode="brushMode"
        self.brushSlider=(70,505)
        self.stampPtsSlider=(70,555)
        self.stampMSlider=(70,605)
        self.dragBrushSlider=self.dragStampPtSlider=self.dragStampMSlider=False
        self.txtLoc=None
        self.text=[]
        self.stampHere=None
        self.initBoolsForDayz()
        self.initPicInfo()
        self.initStarInfo()
        
    def initBoolsForDayz(self):
        self.wentEraserMode=False
        self.isImageSaved=False
        self.makeStamp=False
        self.drawing=False
        self.start=True
        self.starRadChange=False
        self.stampSliderClicked=False
        self.changeStarColor=False
        self.getPic=False
        self.movePic=False
        self.typing=False
        self.copying=False
        self.stamping=False
        self.clear=False
        self.help=False
        
    def initPicInfo(self):
        self.picCorners=[]
        self.picName=None
        self.picDims=(300,300)
        self.picLocation=(300,300)
        self.picCorners=[self.picLocation,(self.picLocation[0]+self.picDims[0],\
        self.picLocation[1]), (self.picLocation[0],self.picLocation[1]+\
        self.picDims[1]), (self.picLocation[0]+self.picDims[0],\
        self.picLocation[1]+self.picDims[1])]
    
    def initStarInfo(self):
        self.starRadLarge=30
        self.starRadSmall=10
        self.nextStarRad=(self.starRadLarge,self.starRadSmall)
        self.nextStarColor=self.brushColor
        self.numStarPoints=5
        self.starPoints=[]

### USER INTERACTION

    def mousePressed(self, x, y):
        self.MPSliders(x,y)
        if 70> x > 20 and 100> y > 50:       #brush button
            self.mode="brushMode"
            self.stamping=False
        if 140>x>10 and 790>y>660:      #get brush color
            self.currPositionbrsh= (x,y)
            if self.mode=="stampMode":
                self.changeStarColor=True
        if x>150 and y>60:              #get stamps
            self.MPgetStamp(x,y)
        if 85+50 > x >50 and 100 > y > 50:  #eraser button
            self.mode="eraserMode" 
            self.stamping=False
        if 720+50 >x>720 and 60>y>10:       #save button
            self.isImageSaved=True
        if 70>x>20 and 170>y>120:           #stamp button
            self.mode="stampMode"
            self.stamping=False
        if 135>x>85 and 170 >y>120:
            self.mode="picMode"
            self.stamping=False
        if 70>x>20 and 190+50>y>190:       #text button
            self.mode="textMode"
            self.stamping=False
        if self.mode=="textMode":
            self.txtLoc=(x,y)
            if self.typing:
                self.typing=False
                self.text=[]
        if self.mode=="picMode":
            if 110>x>30 and 623>y>600:      #import pic
                self.getPic=True
            if self.picLocation[0]+self.picDims[0] >x> self.picLocation[0] and\
            self.picLocation[1] + self.picDims[1] >y> self.picLocation[1]: 
                self.nextPicLocation=(int(x-self.picDims[0]/2),\
                int(y-self.picDims[1]/2))
                self.getPic=True            #click on pic ^
                self.movePic=True
        if 85+50 >x>85 and 190+50>y>190:
            self.mode="copyMode"
            self.stamping=False
        if 700>x>630 and 45>y>20:
            self.clear=True
        if 545+70>x>545 and 45>y>20:
            if self.help==False:
                self.help=True
                self.mode="helpMode"
            else:
                self.help=False
                self.mode="brushMode"
                self.clear=True
    
    def MPgetStamp(self,x,y):
        if self.mode=="stampMode":
            self.currPosition= (x,y)
            self.starRadChange=False
            self.makeStamp=True
            self.changeStarColor=False
            self.getStarPoints()
        if self.mode=="copyMode":
            if 670+50>x>670 and 670+50>y>670:
                self.copying=False
                self.stamping=True
            elif self.stamping==True and self.copying==False:
                self.stampHere=(x,y)
            if self.stampHere==None and self.stamping==False and\
            self.copying==False:
                self.copySquare=[x,y]
                self.copying=True
        
    def MPSliders(self,x,y):
        if self.brushSlider[0] +25/2 >x >self.brushSlider[0] -25/2 and\
        self.brushSlider[1] +25/2 >y >self.brushSlider[1]-25/2:
            self.dragBrushSlider=True
        if self.stampPtsSlider[0] +25/2 >x >self.stampPtsSlider[0] -25/2 and\
        self.stampPtsSlider[1] +25/2 >y >self.stampPtsSlider[1]-25/2:
            self.dragStampPtSlider=True
        if self.stampMSlider[0] +25/2 >x >self.stampMSlider[0] -25/2 and\
        self.stampMSlider[1] +25/2 >y >self.stampMSlider[1]-25/2:
            self.dragStampMSlider=True
        
    def mouseReleased(self, x, y):
        if self.dragBrushSlider:
           self.dragBrushSlider=False
        if self.dragStampPtSlider:
            self.dragStampPtSlider=False
        if self.dragStampMSlider:
            self.dragStampMSlider=False
        if self.mode=="stampMode":
            if self.stampSliderClicked:
                self.starRadChange=False
        if self.mode=="brushMode":
            self.lastBrushDot=self.brush=[]
        if self.copying:                        #make rectangle
            self.copySquare.append(x-self.copySquare[0])
            self.copySquare.append(y-self.copySquare[1])

    def mouseDrag(self, x, y):
        if x>150 and y>60:      #drawing brush strokes
            if self.mode=="brushMode":
                self.lastColor=self.brushColor
                if self.wentEraserMode==True:
                    self.brushColor=self.lastColor
                if self.brush!=[] and self.brush[0]!=x and self.brush[1]!=y:
                    self.lastBrushDot=(self.brush[0],self.brush[1])
                self.brush=[x,y,self.brushRad,self.brushColor]
                self.drawing=True
            if self.mode=="eraserMode":
                self.wentEraserMode=True
                if self.brush!=[] and self.brush[0]!=x and self.brush[1]!=y:
                    self.lastBrushDot=(self.brush[0],self.brush[1])
                self.brush=[x,y,self.brushRad,(255,255,255)]
                self.drawing=True
        if self.dragBrushSlider:
            self.MDBrushSlider(x,y)
        if self.dragStampPtSlider:
            self.MDstampPointSlider(x,y)
        if self.dragStampMSlider:
            self.MDstampSlopeSlider(x,y)
        if self.mode=="picMode":
            if self.picLocation[0]+self.picDims[0] >x> self.picLocation[0] and\
            self.picLocation[1] + self.picDims[1] >y> self.picLocation[1]:
                self.nextPicLocation=(int(x-self.picDims[0]/2),\
                int(y-self.picDims[1]/2))
                self.getPic=True
                self.movePic=True
    
    def MDBrushSlider(self,x,y):
        if self.brushSlider[0]>=20 and self.brushSlider[0]<=130:
            if x>self.brushSlider[0]:
                if self.mode=="brushMode" or self.mode=="eraserMode":
                    self.brushRad+=1
                if self.mode=="stampMode":
                    self.starRadLarge+=2
                    self.starRadSmall+=1
                    self.starRadChange=True
            if x<self.brushSlider[0] and self.brushRad>0:
                if self.mode=="brushMode" or self.mode=="eraserMode":
                    self.brushRad-=1
                if self.mode=="stampMode":
                    self.starRadLarge-=2
                    self.starRadSmall-=1
                    self.starRadChange=True
            self.brushSlider= (x,self.brushSlider[1])
        if self.brushSlider[0]>=135:
            self.brushSlider= (130,self.brushSlider[1])
        if  self.brushSlider[0]<=15:
            self.brushSlider= (20,self.brushSlider[1])
        
    def MDstampPointSlider(self,x,y):
        if self.stampPtsSlider[0]>=20 and self.stampPtsSlider[0]<=130:
            if x>self.stampPtsSlider[0]:
                    self.numStarPoints+=1
                    self.starRadChange=True
            if self.numStarPoints>2 and x<self.stampPtsSlider[0]:
                    self.numStarPoints-=1
                    self.starRadChange=True
            self.stampPtsSlider= (x,self.stampPtsSlider[1])
        if self.stampPtsSlider[0]>=135:
            self.stampPtsSlider= (130,self.stampPtsSlider[1])
        if  self.stampPtsSlider[0]<=15:
            self.stampPtsSlider= (20,self.stampPtsSlider[1])
    
    def MDstampSlopeSlider(self,x,y):
        if self.stampMSlider[0]>=20 and self.stampMSlider[0]<=130:
            if x>self.stampMSlider[0]:
                    self.starRadSmall+=1
                    self.starRadChange=True
            if self.starRadSmall>1 and x<self.stampPtsSlider[0]:
                    self.starRadSmall-=1
                    self.starRadChange=True
            self.stampMSlider= (x,self.stampMSlider[1])
        if self.stampMSlider[0]>=135:
            self.stampMSlider= (130,self.stampMSlider[1])
        if  self.stampMSlider[0]<=15:
            self.stampMSlider= (20,self.stampMSlider[1])
                
    def mouseMotion(self, x, y):
        pass        
            
    def keyPressed(self, keyCode, modifier):
        if self.mode=="textMode":
            key= pygame.key.name(keyCode)
            if key=="backspace":
                self.text=self.text[:-1]
            if key=="space":
                self.text+=" "
            else:
                self.text.append(key)
            self.typing=True

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

### LAYOUT 

    def getLayout(self,screen):
        pygame.draw.rect(screen,(32,32,32),(0,0,150,self.height)) #vert
        pygame.draw.rect(screen,(32,32,32),(0,0,self.width,60))    #horiz
        self.getTitle(screen)
        self.getButtons(screen)
        if self.drawing:
            self.drawBrush(screen)
            self.drawing=False
        if self.mode=="brushMode":
            self.brushSizeSlider(screen)
            self.getBrushColor(screen)
        if self.mode=="eraserMode":
            self.brushSizeSlider(screen)
        if self.mode=="stampMode":
            self.brushSizeSlider(screen)
            self.getBrushColor(screen)
            self.stampPointsSlider(screen)
            self.slopeStampSlider(screen)
            if self.makeStamp:
                self.getStarPoints()
                self.drawStamps(screen)
        if self.mode=="picMode":
            self.getPicButtons(screen)
            if self.getPic:
                self.importPic(screen)
        if self.mode=="textMode":
            self.getText(screen)
        if self.mode=="copyMode":
            if self.copying==True or self.stamping==True:
                self.copyArea(screen)
        if self.clear:
            pygame.draw.rect(screen,(255,255,255),\
            (150,60,self.width,self.height))
            self.clear=False
        if self.help:
            self.helpInfo(screen)
    
    def helpInfo(self,screen):
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",28)
        pygame.draw.line(screen,(192,192,192),(742,55),(350,145),3)#save button
        save= font.render('SAVE BUTTON: save art to Desktop',False,(0,0,0))
        screen.blit(save,(205,140))
        pygame.draw.line(screen,(0,0,0),(665,45),(460,115),3)  #clear tool
        clear= font.render('CLEAR SCREEN TOOL: reverts to blank canvas',False,\
        (0,0,0))
        screen.blit(clear,(205,110))
        pygame.draw.line(screen,(0,0,0),(35,85),(200,175),3) #brush tool
        brushTxt= font.render('BRUSH TOOL: allows free-handed drawing',False,\
        (0,0,0))
        screen.blit(brushTxt,(205,170))
        pygame.draw.line(screen,(0,0,0),(110,85),(200,205),3) #eraser tool
        eraserTxt= font.render('ERASER TOOL: erases drawing',False,(0,0,0))
        screen.blit(eraserTxt,(205,200))
        pygame.draw.line(screen,(0,0,0),(35,145),(200,245),3)   #stamp tool
        stamp= font.render('STAMP TOOL: place stamps on canvas',False,(0,0,0))
        screen.blit(stamp,(205,240))
        pygame.draw.line(screen,(0,0,0),(110,145),(200,275),3) #import pic tool
        importtxt= font.render('IMPORT TOOL: upload pictures onto canvas',\
        False,(0,0,0))
        screen.blit(importtxt,(205,270))
        pygame.draw.line(screen,(0,0,0),(35,215),(200,315),3)     #text tool
        txt= font.render('TEXT TOOL: display messages on canvas',False,(0,0,0))
        screen.blit(txt,(205,310))
        pygame.draw.line(screen,(0,0,0),(110,215),(200,360),3)#copy/paste tool
        txt= font.render('UNIQUE SQUARE TOOL: select an area of the',False,\
        (0,0,0))
        txt2=font.render(' canvas to create your own unique stamp',False,\
        (0,0,0))
        screen.blit(txt,(205,355))
        screen.blit(txt2,(205,385))
        txt= font.render('Press "Help" to return to game',False,(0,0,0))
        screen.blit(txt,(300,500))
    
    def getPicButtons(self,screen):
        pygame.draw.rect(screen,(192,192,192),(30,600,80,23))   #import button
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",18)
        importTxt= font.render('Import',False,(0,0,0))
        screen.blit(importTxt,(35,605))
    
    def getTitle(self,screen):
        pygame.font.init()
        font= pygame.font.Font("alba.ttf",40)
        textsurface= font.render('Paint 112',False,(0,153,153))
        screen.blit(textsurface,(self.width/2-50,0))
    
    def brushSizeSlider(self,screen):
        pygame.draw.rect(screen,(192,192,192),(20,500,110,10))
        pygame.draw.circle(screen,(128,128,128),self.brushSlider,12)
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",18)
        if self.mode=="brushMode":
            textsurface= font.render('- Brush Size +',False,(255,255,255))
        if self.mode=="eraserMode":
            textsurface= font.render('- Eraser Size +',False,(255,255,255))
        if self.mode=="stampMode":
            textsurface= font.render('- Stamp Size +',False,(255,255,255))
        screen.blit(textsurface,(20,520))
    
    def stampPointsSlider(self,screen):
        pygame.draw.rect(screen,(192,192,192),(20,550,110,10))
        pygame.draw.circle(screen,(128,128,128),self.stampPtsSlider,12)
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",18)
        textsurface= font.render('- # of Points +',False,(255,255,255))
        screen.blit(textsurface,(20,570))
    
    def slopeStampSlider(self,screen):
        pygame.draw.rect(screen,(192,192,192),(20,600,110,10))
        pygame.draw.circle(screen,(128,128,128),self.stampMSlider,12)
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",18)
        textsurface= font.render('- Slope +',False,(255,255,255))
        screen.blit(textsurface,(30,620))

### DRAW OBJECTS ON CANVAS
     
    def drawBrush(self,screen):
        if self.drawing==True and self.lastBrushDot!=[]:
            x=self.brush[0]
            y=self.brush[1]
            rad=self.brush[2]
            color=self.brush[3]
            pygame.draw.line(screen,color,self.lastBrushDot,(x,y),rad)
            
    def drawStamps(self,screen):
        points=self.starPoints[:-1]
        color=self.starPoints[-1]
        pygame.draw.polygon(screen,color,points)

### BUTTONS

    def getButtons(self,screen):
        self.brushButton(screen)
        self.eraserButton(screen)
        self.saveImageButton(screen)
        self.clearScreenButton(screen)
        self.helpButton(screen)
        self.stampButton(screen)
        self.importPicButton(screen)
        self.textButton(screen)
        self.copyButton(screen)
        if self.isImageSaved==True:
            self.saveImage(screen)
    
    def stampButton(self,screen):
        if self.mode=="stampMode":
            pygame.draw.rect(screen,(255,153,255),(20,120,50,50))
        else:
            pygame.draw.rect(screen,(128,128,128),(20,120,50,50))
        brushSymbol= pygame.image.load('stamp.png')
        brushSymbol= pygame.transform.scale(brushSymbol,(50,50))
        screen.blit(brushSymbol,(20,120))
        """stamp icon from: https://commons.wikimedia.org/wiki/File:
        Femuddig_stjärna.svg"""
    
    def textButton(self,screen):
        if self.mode=="textMode":
            pygame.draw.rect(screen,(255,153,255),(20,190,50,50))
        else:
            pygame.draw.rect(screen,(128,128,128),(20,190,50,50))
        txt= pygame.image.load('text.png')
        txt= pygame.transform.scale(txt,(43,43))
        screen.blit(txt,(22,194))
        """text icon from: https://www.iconfinder.com/icons/519853/t-
        square_text_format_text_formatting_text_symbol_text_tool_writing
        _text_icon"""
    
    def copyButton(self,screen):
        if self.mode=="copyMode":
            pygame.draw.rect(screen,(255,153,255),(85,190,50,50))
            pygame.font.init()
            font= pygame.font.Font("neon.ttf",20)
            textsurface= font.render('Stickers:',False,(0,0,0))
            screen.blit(textsurface,(660,650))
        else:
            pygame.draw.rect(screen,(128,128,128),(85,190,50,50))
            pygame.draw.rect(screen,(255,255,255),(630,640,150,150))
        copy= pygame.image.load('copy.png')
        copy= pygame.transform.scale(copy,(45,45))
        screen.blit(copy,(87,192))
        """copy icon from: https://www.iconfinder.com/icons/282311/clone_copy
        _copy_paste_documents_duplicate_sheets_text_icon"""
        
    def saveImageButton(self,screen):
        pygame.draw.rect(screen,(128,128,128),(720,10,45,45))
        save= pygame.image.load('save.png')
        save= pygame.transform.scale(save,(45,45))
        screen.blit(save,(720,10))
        #save icon from: http://ktmc.info/save-icon-png
    
    def clearScreenButton(self,screen):
        pygame.draw.rect(screen,(128,128,128),(630,20,70,25))
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",22)
        importTxt= font.render('Clear',False,(0,0,0))
        screen.blit(importTxt,(640,23))
    
    def helpButton(self,screen):
        if self.mode=="helpMode":
            pygame.draw.rect(screen,(255,153,255),(545,20,70,25))
        else:
            pygame.draw.rect(screen,(128,128,128),(545,20,70,25))
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",22)
        importTxt= font.render('Help',False,(0,0,0))
        screen.blit(importTxt,(560,23))
    
    def eraserButton(self,screen):
        if self.mode=="eraserMode":
            pygame.draw.rect(screen,(255,153,255),(85,50,50,50))
        else:
            pygame.draw.rect(screen,(128,128,128),(85,50,50,50))
        eraser= pygame.image.load('eraser.png')
        eraser= pygame.transform.scale(eraser,(50,50))
        screen.blit(eraser,(85,50))
        """eraser icon from: https://www.iconfinder.com/icons/323358/clean_
        clear_creative_delete_education_erase_eraser_grid_pencil_remove
        _rubber_shape_tool_icon"""
        
    def brushButton(self,screen):
        if self.mode=="brushMode":
            pygame.draw.rect(screen,(255,153,255),(20,50,50,50))
        else:
            pygame.draw.rect(screen,(128,128,128),(20,50,50,50))
        brushSymbol= pygame.image.load('pen.png')
        brushSymbol= pygame.transform.scale(brushSymbol,(50,50))
        screen.blit(brushSymbol,(20,50))
        """pen image from: http://www.keyword-suggestions.com/
        cGVuY2lsIGVyYXNlciBpY29u/"""
    
    def importPicButton(self,screen):
        if self.mode=="picMode":
            pygame.draw.rect(screen,(255,153,255),(85,120,50,50))
        else:
            pygame.draw.rect(screen,(128,128,128),(85,120,50,50))
        importSymbol= pygame.image.load('import.png')
        importSymbol= pygame.transform.scale(importSymbol,(47,47))
        screen.blit(importSymbol,(85,120))
        """import symbol from: http://www.newdesignfile.com/post_import-
        database-icon-png_249195/"""
    
### COMPUTATIONAL STUFF

    def getStarPoints(self):
        x,y=self.currPosition
        if self.brushColor==(255,255,255) or self.brushColor==(255,255,255,255):
            self.brushColor=(0,0,0)
        thetaChange= 2*math.pi/self.numStarPoints
        thetaCurr=math.pi*3/2
        if self.starRadChange:
            self.nextStarRad= (self.starRadLarge,self.starRadSmall)
        else:
            self.starPoints=[]
            self.starRadLarge=self.nextStarRad[0]
            self.starRadSmall=self.nextStarRad[1]
            for i in range(self.numStarPoints):
                x0= self.starRadLarge*math.cos(thetaCurr) + x
                y0= self.starRadLarge*math.sin(thetaCurr) + y
                thetaCurr=thetaCurr+thetaChange/2
                x1=self.starRadSmall*math.cos(thetaCurr) + x
                y1= self.starRadSmall *math.sin(thetaCurr) + y
                thetaCurr=thetaCurr+thetaChange/2
                self.starPoints+=[[x0,y0],[x1,y1]]
            if self.changeStarColor:
                self.brushColor=self.nextStarColor
            self.starPoints.append(self.brushColor)
            
    def getBrushColor(self,screen):
        wheel= pygame.image.load('color.jpg')
        wheel= pygame.transform.scale(wheel,(130,130))
        screen.blit(wheel,(10,660))
        if self.currPositionbrsh!=None:
            self.brushColor=screen.get_at(self.currPositionbrsh)
        if self.mode=="stampMode":
            self.nextStarColor=self.brushColor
        """color wheel image from: https://www.ndsu.edu/pubweb/~rcollins/
        362design/broadsheetexercise.html"""
     
    def saveImage(self,screen):
        self.isImageSaved=False
        getTime=time.asctime(time.localtime(time.time()))
        getTime=getTime.replace(" ", "_")
        getTime= getTime.replace(":",".")
        saveFile= "c:\Desktop\15-112\termProject.py" + getTime+ ".jpg"
        rect= pygame.Rect(150,60, self.width-150, self.height-60)
        sub= screen.subsurface(rect)
        pygame.image.save(sub, saveFile)
        pygame.font.init()
        font= pygame.font.Font("neon.ttf",20)
    
    def importPic(self,screen):
        if self.movePic:
            pygame.draw.rect(screen,(255,255,255),(self.picLocation[0],\
            self.picLocation[1],self.picDims[0],self.picDims[1]))
            self.picLocation=self.nextPicLocation
            userInput=self.picName
            image= pygame.image.load(userInput+'.jpg')
            image= pygame.transform.scale(image,self.picDims)
            screen.blit(image, self.picLocation)
            self.getPic=False
            self.movePic=False
        else:
            print("Enter Image Name (JPGs only plz)")
            userInput=input()
            print(userInput+ ".jpg imported")
            self.picName=userInput
            image= pygame.image.load(userInput+'.jpg')
            image= pygame.transform.scale(image,self.picDims)
            screen.blit(image, self.picLocation)
            self.getPic=False
            self.movePic=False
    #imported image from video: http://www.kosbie.net/cmu/
    
    def getText(self,screen):
        if self.txtLoc!=None:
            txt=''
            for i in self.text:
                txt+=i
            txt.replace("'", "")
            pygame.font.init()
            font= pygame.font.Font("neon.ttf",23)
            txt= font.render(txt,False,(0,0,0))
            screen.blit(txt,self.txtLoc)
    
    def copyArea(self,screen):
        savedStamp=self.copySquare
        if self.copying==True and len(self.copySquare)==4:
            saveFile= str(random.randint(1,100)) + ".jpg"
            rect= pygame.Rect(self.copySquare[0],self.copySquare[1],\
            self.copySquare[2], self.copySquare[3])
            sub= screen.subsurface(rect)
            pygame.image.save(sub, saveFile)
            image= pygame.image.load(saveFile)
            image= pygame.transform.scale(image,(50,50))
            screen.blit(image, (670,670))
            self.copySquare=[]
            self.stamping=False
        if self.stamping:
            saveFile= str(random.randint(1,100)) + ".jpg"
            rect= pygame.Rect(670,670,50, 50)
            sub= screen.subsurface(rect)
            pygame.image.save(sub, saveFile)
            image= pygame.image.load(saveFile)
            image= pygame.transform.scale(image,(50,50))
            if self.stampHere!=None:
                screen.blit(image, self.stampHere)
                self.stampHere=None

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
            if self.start:
                screen.fill(self.bgColor)
                self.start=False
            else:
                background=pygame.Surface.copy(screen)
                screen.blit(background,(0,0))
            self.redrawAll(screen)
            pygame.display.flip()
        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()

"""framework from: https://github.com/LBPeraza/Pygame-Asteroids/blob/master/
pygamegame.py"""