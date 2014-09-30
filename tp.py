#Pygame barebones taken from:
#Sample Python/Pygame Program
#Simpson College Computer Science
#http://cs.simpson.edu
 
import pygame
import sys
import random
import copy
from pygame.locals import *

pygame.init()

def loadTextList():
    #Loads a text file.  Copied from Kosbie.net
    fileHandler = open("save.txt", "rt") # rt stands for read text
    text = fileHandler.read()
    # read the entire file into a single string
    fileHandler.close() # close the file
    toReturn = ""
    for element in text:
        toReturn += element
    return [toReturn]

def saveText(text):
  #Saves a file
    fileHandler = open("save.txt", "wt") # wt stands for write text
    toSave = ""
    for element in text:
        toSave += str(element)
    fileHandler.write(toSave) # write the text
    fileHandler.close() # close the file

def defineColors():
    #Defines black, green, khaki, and red colors.
    return (0,0,0),(0,100,0),(240,230,140),(255,0,0)

def displayVariables():
    #Initializes lineNumber,descriptionsText,
    #display, and randList variables.
    return 0, [], -1, [], " "

def initialScores():
    #Initializes scores.
    return 100,10,0,150

def initLengths():
    #Initializes score lengths.
    return 0,2,3,3

def initScrolling():
    #Initialize scrolling variables.
    #imageScroll,backHor, and backVer.
    return 0,20,20

def initDrag():
    #Scroll and drag variables set.
    return False

def initScorePositions():
    #Score positions.
    return [470-6,1], [670-9,1],[870,1],[270-9,1]

def initStates():
    #Initializes variables that control which screens are displayed:
    #Splash screen, pause screen, game over screen, name screen.
    return True,False,False,True

def makeCanvas():
    # Set the height and width of the screen
    size = [1200,700]
    pygame.display.set_caption("EcoCity")
    return pygame.display.set_mode(size)

screen = makeCanvas()

def initLargeLists():
    #Description display variable
     printed =\
    [[False]*10,
     [False]*10,
     [False]*10, #Resevoir
     [False]*10,
     [False]*10,
     [False]*10, #Hospital
     [False]*10,
     [False]*10,
     [False]*10,
     [False]*10,
     [False]*10,
     [False]*10,
     [False]*10]
     newImages = [[0]*4,
                  [0]*4,
                  [0]*4,
                  [0]*4]
     occupied = [[False]*4,
                 [False]*4,
                 [False]*4,
                 [False]*4]
     oldOccupied = [[False]*4,
                    [False]*4,
                    [False]*4,
                    [False]*4]
     oldImages = []
     usedImages = []
     return printed, newImages,occupied,oldOccupied,oldImages,usedImages

def dPosition(printed):
     descriptionPosition = []
     x = 927
     y0 = 475
     step = 20
     for i in xrange(len(printed[0])):
         descriptionPosition += [[x,y0+step*i]]
     return descriptionPosition

#Image uploads.  All improvement images are my screenshots from the
#computer game Civilization IV.  Doing this is a copyright
#infringement, even though I am citing the game.  Therefore,
#this game can not be distributed.
farmImage = pygame.image.load("Corn.png").convert()
universityImage = pygame.image.load("University3.png").convert()
resevoirImage = pygame.image.load("Resevoir.png").convert()
airportImage = pygame.image.load("Airport.png").convert()
factoryImage = pygame.image.load("Factory.png").convert()
hospitalImage = pygame.image.load("Hospital.png").convert()
marketImage = pygame.image.load("Market.png").convert()
massMediaImage = pygame.image.load("Mass Media.png").convert()
militaryImage = pygame.image.load("Military.png").convert()
bombImage = pygame.image.load("Bomb.png").convert()
fishImage = pygame.image.load("Fish.png").convert()
oilImage = pygame.image.load("Oil.png").convert()
cowsImage = pygame.image.load("Cows.png").convert()
manImage = pygame.image.load("Man.png").convert()
upArrowImage = pygame.image.load("Up.png").convert()
downArrowImage = pygame.image.load("Down.png").convert()
highX = pygame.image.load("highx.png").convert()
highY = pygame.image.load("highy.jpg").convert()
corner1 = pygame.image.load("Corner1.png").convert()
corner2 = pygame.image.load("Corner2.png").convert()
corner3 = pygame.image.load("Corner3.jpg").convert()
corner4 = pygame.image.load("Corner4.png").convert()
miniGrass = pygame.image.load("miniGrass.jpg").convert()

imageList = [farmImage,universityImage,resevoirImage,airportImage,
factoryImage,hospitalImage,marketImage,massMediaImage,militaryImage,
bombImage,fishImage,oilImage,cowsImage]
imageNamesPositionsXList = [996,1022,1025,1027,1027,1026,1029,1015,
1027,995,1030,1004,1010]

def initSidebarImages(imageList):
    #Establishes the improvement images that should appear
    #on the sidebar initially.
    i1 = imageList[0]
    i2 = imageList[1]
    i3 = imageList[2]
    return i1,i2,i3

def initTextPositions(imageNamesPositionsXList):
    #Establishes the initial positions improvement captions have.
    #It is necessary to have different positions for each captions
    #because I want the captions to be centered and each caption
    #has different lengths.
    y0 = 165
    step = 130
    oneTextPosition = [imageNamesPositionsXList[0],y0]
    twoTextPosition = [imageNamesPositionsXList[1],y0+step]
    threeTextPosition = [imageNamesPositionsXList[2],y0+step*2]
    return oneTextPosition,twoTextPosition,threeTextPosition

def restarting(imageList,imageNamesPositionsXList):
    #Returns initial values for many different variables.  This allows
    #for game restarts.  I also use this function upon program load.
    lineNumber,descriptionsText,display,randList,name = displayVariables()
    satisfactionScore,populationScore,score,credits = initialScores()
    scoreLength,populationLength,satisfactionLength,creditsLength = initLengths()
    imageScroll,backHor,backVer = initScrolling()
    oneTextPosition,twoTextPosition,threeTextPosition =\
    initTextPositions(imageNamesPositionsXList)
    populationPosition,satisfactionPosition,scorePosition,creditsPosition =\
    initScorePositions() 
    drOne = drTwo = drThree = recentlyScrolled = recentlyScrolled2 =\
    displayThem = initDrag()
    printed, newImages,occupied,oldOccupied,oldImages,usedImages =\
    initLargeLists()
    descriptionPosition = dPosition(printed)
    imageOne,imageTwo,imageThree = initSidebarImages(imageList)
    splashScreen,pauseScreen,over,nameScreen = initStates()
    highScores = loadTextList()
    return (lineNumber,descriptionsText,display,randList,satisfactionScore,
    populationScore,score,credits,scoreLength,populationLength,
    satisfactionLength,creditsLength,imageScroll,backHor,backVer,oneTextPosition,
    twoTextPosition,threeTextPosition,populationPosition,
    satisfactionPosition,scorePosition,creditsPosition,drOne,drTwo,drThree,
    recentlyScrolled,recentlyScrolled2,displayThem,descriptionPosition,
    printed,newImages,occupied,oldOccupied,oldImages,usedImages,imageOne,imageTwo,imageThree,
    splashScreen,pauseScreen,over,nameScreen,name,highScores)

#Restarting() is called here upon game load.
(lineNumber,descriptionsText,display,randList,satisfactionScore,
populationScore,score,credits,scoreLength,populationLength,
satisfactionLength,creditsLength,imageScroll,backHor,backVer,
oneTextPosition,twoTextPosition,threeTextPosition,populationPosition,
satisfactionPosition,scorePosition,creditsPosition,drOne,drTwo,drThree,
recentlyScrolled,recentlyScrolled2,displayThem,descriptionPosition,
printed,newImages,occupied,oldOccupied,oldImages,usedImages,imageOne,
imageTwo,imageThree,splashScreen,pauseScreen,over,nameScreen,name,highScores) = restarting(imageList,imageNamesPositionsXList)

black,green,khaki,red = defineColors() #Defines colors

def updatedPositions(imageScroll,populationLength,satisfactionLength,
scoreLength,creditsLength,imageNamesPositionsXList):
    #Updates X Values of improvements captions.
    oneTextPosition =\
    [imageNamesPositionsXList[imageScroll],165]
    twoTextPosition =\
    [imageNamesPositionsXList[imageScroll+1],295]
    threeTextPosition =\
    [imageNamesPositionsXList[imageScroll+2],425]
    populationPosition = [470-3*populationLength,1]
    satisfactionPosition = [670-3*satisfactionLength,1]
    scorePosition = [870-3*scoreLength,1]
    creditsPosition = [270-3*creditsLength,1]
    return (oneTextPosition,twoTextPosition,threeTextPosition,
    populationPosition,satisfactionPosition,
    scorePosition,creditsPosition)


#Map background.  Taken from myinkblog.com.
backgroundImage = pygame.image.load("Oversized.jpg").convert()

def populationGrowth(newImages,universityImage):
    #Determines the speed of population growth.  If a university
    #is built, population grows by 5 per game frame.  Otherwise,
    #the population grows by 10 per frame.
    for i in range(len(newImages)):
        for j in range(len(newImages[0])):
            if newImages[i][j] == universityImage:
                return 5
    return 10

def imageDrag(drOne,drTwo,drThree,imageScroll,display,event,
onSidebar,newImages,credits,score,satisfactionScore,lineNumber,
descriptionsList,descriptionsText,descriptionPosition,printed,
imageOne,imageTwo,imageThree,usedImages,backHor,backVer):
    #Important function that is effective when an improvement has
    #been clicked on the sidebar for dragging.  Sets "dr" variables
    #to indicate that an image is being dragged.  This function is
    #also effective when a user is reading improvement descriptions.
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
    # Fetch the x and y out of the list,
    #just like we'd fetch letters out of a string.
    x=pos[0]
    y=pos[1]
    botOne = 166
    topOne = 60
    incr = 130
    left = 935
    right = 1165
    scoreAdd = 50
    betweenOneTwo = y >= botOne and y <= topOne + incr
    betweenTwoThree = y >= botOne+incr and\
    y <= topOne+incr*2
    boxOne = y > topOne and y < botOne
    boxTwo = y > topOne + incr and y < botOne + incr
    boxThree = y > topOne + incr*2 and y < botOne + incr*2
    if x <= left or x >= right or y <= topOne or y >= botOne+incr*2\
    or betweenOneTwo == True or betweenTwoThree == True:
        #Resets description display.
        miniMap(backHor,backVer,newImages)
        for lineNumbers in range(len(printed[display])):
            printed[display][lineNumbers] = False
            descriptionsText = []
    else:
        conditionals = (drOne == False and drTwo == False\
                        and drThree == False)
        if boxOne and conditionals == True and\
        imageOne not in usedImages:
            #Checks if another description being displayed.
            display = imageScroll
            lineNumber = 0
            if event.type == MOUSEBUTTONDOWN:
                drOne = True
                score += scoreAdd #Reward for building improvement
                usedImages += [imageOne]
                satisfactionScore,credits =\
                changeCreditsAndSatisfaction(imageOne,
                satisfactionScore,credits)
        elif boxTwo and conditionals == True and\
        imageTwo not in usedImages:
            display = imageScroll + 1
            lineNumber = 0
            if event.type == MOUSEBUTTONDOWN:
                drTwo = True
                score += scoreAdd #Reward for building improvement
                usedImages += [imageTwo]
                satisfactionScore,credits =\
                changeCreditsAndSatisfaction(imageTwo,
                satisfactionScore,credits)
        elif boxThree and conditionals == True and\
        imageThree not in usedImages:
            display = imageScroll + 2
            lineNumber = 0
            if event.type == MOUSEBUTTONDOWN:
                drThree = True
                score += scoreAdd #Reward for building improvement
                usedImages += [imageThree]
                satisfactionScore,credits =\
                changeCreditsAndSatisfaction(imageThree,
                satisfactionScore,credits)
        for line in descriptionsList[display].splitlines():
            if lineNumber < len(printed[display]):
                if printed[display][lineNumber] == False:
                    descriptionFont =\
                    pygame.font.Font("Caslon Old Face Heavy BT.ttf",13)
                    descriptionsText += [
                    descriptionFont.render(line,True,black)]
                    printed[display][lineNumber] = True
                    lineNumber += 1
        if len(descriptionsText) > 4:
            printIt(descriptionsText,descriptionPosition)
    return (drOne,drTwo,drThree,imageScroll,display,event,
            onSidebar,newImages,credits,score,satisfactionScore,
            lineNumber,descriptionsText,x,y,printed,usedImages)

def changeCreditsAndSatisfaction(image,satisfactionScore,credits):
    #Changes a user's score when an improvement is purchased.
    #Updates credits and satisfactionScore.
    satAdd = 25
    if image == farmImage:
        satisfactionScore += satAdd
        credits -= 19
    elif image == universityImage:
        credits -= 15
    elif image == resevoirImage:
        satisfactionScore += satAdd
        credits -= 16
    elif image == airportImage:
        satisfactionScore += satAdd
        credits -= 34
    elif image == factoryImage:
        satisfactionScore += satAdd
        credits -= 21
    elif image == hospitalImage:
        satisfactionScore += satAdd
        credits -= 19
    elif image == marketImage:
        satisfactionScore += satAdd
        credits -= 21
    elif image == massMediaImage:
        satisfactionScore += satAdd
        credits -= 2
    elif image == militaryImage:
        satisfactionScore += satAdd
        credits -= 40
    elif image == bombImage:
        credits -= 50
    elif image == fishImage:
        satisfactionScore += satAdd
        credits -= 21
    elif image == oilImage:
        satisfactionScore += satAdd
        credits -= 59
    elif image == cowsImage:
        satisfactionScore += satAdd
        credits -= 36
    return satisfactionScore,credits

def isGameOver(credits,satisfactionScore,over):
    #Determines whether the user has lost.
    if credits <= 0 or satisfactionScore <= 0 or over == True:
        return True
    return False

def printIt(descriptionsText,descriptionPosition):
    #Prints descriptions provided by imageDrag().
    dLength = 9
    for lineNum in range(len(descriptionsText)):
        if lineNum > dLength:
            lineNum = 0
            continue
        screen.blit(
        descriptionsText[lineNum],descriptionPosition[lineNum]) 

def randomSelection(populationScore,satisfactionScore,manImage,
                    randl,backHor,backVer):
    #Randomly selects a location for an image of a man to be blitted.
    popThreshold = 1000
    if populationScore % popThreshold == 0:
        randList = []
        randX,randY = doRand(populationScore)
        #Calls doRand to set random person coordinates if
        #the populationScore eclipses the population threshold.
        if randX != -1 and randY != -1:
            decrement = 20
            randList = [randX,randY]
            if len(randList) > 0:
                if checkRand(randl,randList) == False:
                    randList = []
            satisfactionScore -= decrement #Satisfaction decremented.
            #Adds coordinates of a random person when the person is
            #first brought into being.
            return randList,satisfactionScore
    return [],satisfactionScore
            
def doRand(populationScore):
    #Random location selection of a man occurs here.
    topLeftB = 21
    rightB = 888
    botB = 587
    trial = populationScore/1000
    for times in range(trial):
        x = random.randint(topLeftB,rightB)
        y = random.randint(topLeftB,botB)
        return x,y
    return -1,-1

def checkRand(randl,randList):
    #Ensures that no man overlaps each other. 
    x,y = randList[0],randList[1]
    width = 31
    height = 71
    for i in range(0,len(randl),2):
        if abs(x-randl[i]) < width and abs(y-randl[i+1]) < height\
        and (randl[i] != x and randl[i+1] != y):
            return False
    return True

imageNamesList = ["Vegetable Farm", "University", "Resevoir", "Airport",
"Factory", "Hospital", "Market", "Mass Media", "Military",
 "Bomb Development","Fishing", "Oil Production", "Cattle Farm"]

descriptionsList = ["""          Industrial Vegetable Farm

Provides food to population at high
ecological costs.  Synthetic fertilizers,
herbicides, pesticides, and insecticides
deplete the soil. Fertilizer runoff harms
ecosystems in nearby bodies of water.

                  +25 Satisfaction
                       -19 Credits""",
"""                        University

Provides education.  In general,
well-off, educated families produce
fewer children than do poor families.
Therefore, university construction slows
the rate of population growth.

                       -15 Credits
            -50% Population Growth""",
"""                         Resevoir

Provides water to population.

                  +25 Satisfaction
                       -16 Credits
                       
                       
                       
                       """,
"""                         Airport

Provides passengers high-speed
transportation at high fuel costs.  Car
transportation is more eco-friendly.

                   +25 Satisfaction
                       -34 Credits
                       
                       """,
"""                          Factory

Allows for mass production of products
and greater product accessability.
Supply chains are ecologically damaging
because they produce excessive
amounts of waste and require trucking.

                   +25 Satisfaction
                       -21 Credits""",
"""                         Hospital

Provides health care to population.

                  +25 Satisfaction
                       -19 Credits
                       

                       
                       """,
"""                     Supermarket

Allows for easier access to wide range
of products. Fosters a culture of
immoderate consumption.  Favors
industrial production practices,
rather than small-scale production.

                   +25 Satisfaction
                       -21 Credits""",
"""                        Mass Media

Provides population entertainment.
Commercial advertisements encourage
population to consume immoderately.

                   +25 Satisfaction
                       -2 Credits
                       
                       """,
"""                          Military

Maintains national security at high
economic costs. Also, Modern warfare
is ecologically costly.

                   +25 Satisfaction
                       -40 Credits
                       
                       """,
"""                Bomb Development

Modern warfare has increasingly
involved use of bombs.  In times of
peace and war, bombs are developed
and maintained at high economic and
ecological costs.

                       -50 Credits
                       """,
"""                         Fishing

Provides high-protein food.  
Industrial fishing practices
deplete natural fish sources.

                   +25 Satisfaction
                       -21 Credits
                       
                       """,
"""                   Oil Production

Oil is drilled overseas, then
transported, refined, and converted
into gasoline fuel.  Gasoline is
used for many purposes: transportation,
electricity, heating, and more.

                   +25 Satisfaction
                       -59 Credits""",
"""             Industrial Cattle Farm

Provides food to population at high
ecological costs. Animals are overfed
with corn and produce methane, a heat
trapping gas.  Worker conditions are
sometimes dangerous and unhealthy.

                   +25 Satisfaction
                       -36 Credits"""]

def blitCover():
    #Blits green rectangles everywhere except where the map
    #is displayed in order to allow the map to be displayed
    #only where the map should be when it is being scrolled.
    pygame.draw.rect(screen,green,[920,0,1200,700],0)
    pygame.draw.rect(screen,green,[0,0,1100,20],0)
    pygame.draw.rect(screen,green,[0,0,20,700],0)
    pygame.draw.rect(screen,green,[0,680,1100,700],0) 

def blitBoard(backgroundImage,backgroundPosition,imageOne,
              imageTwo,imageThree,upArrowImage,
              downArrowImage,newImages,occupied,
              highX,highY,corner1,corner2,corner3,corner4,backHor,
              backVer,toAdd,randList,manImage):
    #This function blits stationary objects.  It also calls
    #blitAddedImages() which blits moving objects.
    screen.blit(backgroundImage,backgroundPosition) 
    blitAddedImages(newImages,occupied,highX,highY,
                    corner1,corner2,corner3,corner4,backHor,backVer)
    randList = addRand(toAdd,randList,manImage,backHor,backVer)
    blitCover()
    upArrowPosition = [939,427]
    downArrowPosition = [1119,428]
    imageOnePosition=[935,60]
    imageTwoPosition = [935,190]
    imageThreePosition = [935,320]
    sidescreenPosition = [920,20,260,660]
    mapPosition = [20,20,900,660]
    screen.blit(imageOne,imageOnePosition)
    screen.blit(imageTwo,imageTwoPosition)
    screen.blit(imageThree,imageThreePosition)
    screen.blit(downArrowImage,upArrowPosition)
    screen.blit(upArrowImage,downArrowPosition)
    increment = 130
    #Lines
    pygame.draw.rect(screen,khaki,sidescreenPosition,2) #Sidescreen
    pygame.draw.rect(screen,khaki,mapPosition,2) #Map
    for i in xrange(4):
        pygame.draw.rect(screen,khaki,
        [830-(200*i),0,90,20],2) #Score
        pygame.draw.line(screen,khaki,[920,470],
        [1180,470],2) #Partition
    for i in xrange(3):
        pygame.draw.rect(screen,khaki,
        [935,60+(i*increment),230,106],2) #Buttons
    #"Improvements" word in sidebar.
    improvementsFont = pygame.font.Font("Carleton.ttf", 25)
    improvementsText = improvementsFont.render(
    "Improvements",True,black)
    improvementsPosition=[960,30]
    screen.blit(improvementsText,improvementsPosition)
    nameFont = pygame.font.Font("Caslon Old Face Heavy BT.ttf",16)
    nameText = nameFont.render(name,True,black)
    namePosition = [1045-len(name)*5,0]
    screen.blit(nameText,namePosition)
    #Score caption text
    popTextPosition = [345,2]
    satisfactionTextPosition = [535,2]
    scoreTextPosition = [781,2]
    creditsTextPosition = [148,2]
    scoreFont = pygame.font.Font("Charrington Bold.ttf",15)
    popText = scoreFont.render("Population:",True,black)
    screen.blit(popText,popTextPosition)
    satisfactionText = scoreFont.render("Satisfaction:",True,black)
    screen.blit(satisfactionText,satisfactionTextPosition)
    scoreText = scoreFont.render("Score:", True,black)
    screen.blit(scoreText,scoreTextPosition)
    creditsText = scoreFont.render("EcoCredits:",True,black)
    screen.blit(creditsText,creditsTextPosition)
    return randList #randList changes when blitAddedImages() called.

def blitAddedImages(newImages,occupied,highX,highY,
                    corner1,corner2,corner3,corner4,backHor,backVer):
    #Blits improvements that the user drags on to the map.
    #Responsible for adjusting improvement positions if the map
    #had been scrolled.
    xSize = 330
    ySize = 206
    xOffset = 138
    road = 50
    diff = 41
    for i in range(len(newImages)):
        for j in range(len(newImages[0])):
            if newImages[i][j] != 0 and type(newImages[i][j]) != list:
                #Note: backHor, backVer are map scrolling variables.
                #They stand for backgroundHorizontal
                #and backgroundVertical.
                tempImage = newImages[i][j]
                tempPosition = [j*xSize-xOffset + backHor,
                i*ySize+road+2+backVer]
                screen.blit(tempImage,tempPosition)
                screen.blit(highX,
                [j*xSize-xOffset + backHor,i*ySize+2 + backVer])
                screen.blit(highX,
                [j*xSize-xOffset+backHor,i*ySize+ySize-road+2+backVer])
                screen.blit(highY,
                [j*xSize-xOffset-road-1+backHor,i*ySize+road+2+backVer]) 
                screen.blit(highY,
                [j*xSize+road+diff+1+backHor,i*ySize+road+2+backVer])
                screen.blit(corner2,
                [j*xSize-xOffset-road + backHor,i*ySize+1 + backVer])
                screen.blit(corner1,
                [j*xSize+road+diff+backHor,i*ySize+1 + backVer])
                screen.blit(corner3,
                [j*xSize-xOffset-road + backHor,
                i*ySize+ySize-road+1+backVer])
                screen.blit(corner4,
                [j*xSize+road+diff+1+backHor,
                i*ySize+ySize-road+1+backVer])

def fillOccupied(occupied,newImages,image):
    #Fills the "occupied" list, which is a list that ensures
    #that images added to the map do not overlap each other.
    cont = True
    for i in range(len(occupied)):
        if cont == True:
            for j in range(len(occupied[0])): 
                if occupied[i][j] == False and cont == True:
                    occupied[i][j] = True
                    newImages[i][j] = image
                    cont = False
    return occupied,newImages

def crossOut(screen,imageList, onSidebar, newImages,khaki):
    #Crosses out appropriate image on improvements list when
    #an improvement is purchased.
    x0 = 935
    x1 = 1165
    y0 = 60
    y1 = 165
    increment = 130
    for image in imageList:
        for i in range(len(newImages)):
            for j in range(len(newImages[0])):
                if image == newImages[i][j]:
                    if image == onSidebar[0]:
                        pygame.draw.line(screen,
                        khaki,[x0,y0],[x1,y1],2)
                        pygame.draw.line(screen,
                        khaki,[x1,y0],[x0,y1],2)
                    elif image == onSidebar[1]:
                        pygame.draw.line(screen,khaki,
                        [x0,y0+increment],[x1,y1+increment],2)
                        pygame.draw.line(screen,khaki,
                        [x1,y0+increment],[x0,y1+increment],2)
                    elif image == onSidebar[2]:
                        pygame.draw.line(screen,khaki,
                        [x0,y0+increment*2],[x1,y1+increment*2],2)
                        pygame.draw.line(screen,khaki,
                        [x1,y0+increment*2],[x0,y1+increment*2],2)

def arrowButtons(event,x,y,imageScroll,
imageList,lineNumber,descriptionsText,
recentlyScrolled,recentlyScrolled2):
    #The arrow buttons section.  Changes important variables when
    #an arrow button on the sidebar is clicked.
    topBound = 470
    botBound = 432
    upALeft = 938
    upARight = 984
    downALeft = 1119
    downARight = 1164
    if event.type == MOUSEBUTTONDOWN and\
    y > botBound and y < topBound:
        #recentlyScrolled and recentlyScrolled2 slow
        #down sidebar image scrolling.
        if recentlyScrolled == True:
            recentlyScrolled = False
        elif recentlyScrolled2 == True:
            recentlyScrolled2 = False
        elif x > upALeft and x <\
        upARight and imageScroll < len(imageList) - 3:
        #Up clicked
            imageScroll += 1
            #Important variable that establishes
            #which images to display on the sidebar.
            recentlyScrolled = True
            recentlyScrolled2 = True
            lineNumber = 0
            descriptionsText = []
        elif x > downALeft and x <\
        downARight and imageScroll > -len(imageList) + 2:
        #Down clicked
            imageScroll -= 1 
            recentlyScrolled = True
            recentlyScrolled2 = True
            lineNumber = 0
            descriptionsText = []
    return (lineNumber,descriptionsText,imageScroll,
    recentlyScrolled,recentlyScrolled2)

def dragAndPlace(drOne,drTwo,drThree,imageOne,imageTwo,
                 imageThree,x,y,occupied,newImages):
    #IMAGE IS BEING DRAGGED AND THEN PLACED SECTION.
    if drOne == True:
        screen.blit(imageOne,[x,y])
        #Blits image at mouse location during dragging.
        for eventOne in pygame.event.get():
            if eventOne.type == MOUSEBUTTONDOWN:
                drOne = False #No longer dragging.
                occupied,newImages =\
                fillOccupied(occupied,newImages,imageOne)
    elif drTwo == True:
        screen.blit(imageTwo,[x,y])
        for eventTwo in pygame.event.get():
            if eventTwo.type == MOUSEBUTTONDOWN:
                drTwo = False
                occupied,newImages =\
                fillOccupied(occupied,newImages,imageTwo)
    elif drThree == True:
        screen.blit(imageThree,[x,y])
        for eventThree in pygame.event.get():
            if eventThree.type == MOUSEBUTTONDOWN:
                drThree = False
                occupied,newImages =\
                fillOccupied(occupied,newImages,imageThree)
    return drOne,drTwo,drThree,occupied,newImages

def addRand(toAdd,randList,manImage,backHor,backVer):
    if len(toAdd) > 0:
        #Adds coordinates of new random person to randList.
        randList += toAdd
        #This randList is complete with all random people positions.
    blitRand(randList,manImage,backHor,backVer)
    return randList

def blitRand(randList,manImage,backHor,backVer):
    for i in xrange(0,len(randList),2):
        #Blits random people.
        screen.blit(manImage,
        [randList[i]+backHor,randList[i+1] + backVer])

def defineImages(imageList, imageScroll):
    #Returns the image that should be displayed on the sidebar.
    #This is a function that is repeatedly called in main loop.
    return (imageList[imageScroll],
    imageList[imageScroll+1],imageList[imageScroll+2])

def blitScores():
    #Blits the score numbers.
    scoreNumberFont = pygame.font.Font(
    "Caslon Old Face Heavy BT.ttf",15)
    thresh = 1000
    if populationScore % thresh == 0:
        col = khaki
    else:
        col = black
    satText =\
    scoreNumberFont.render(str(satisfactionScore),True,black)
    screen.blit(satText,satisfactionPosition)
    popText = scoreNumberFont.render(str(populationScore),True,col)
    screen.blit(popText,populationPosition)
    scoreText = scoreNumberFont.render(str(score),True,black)
    screen.blit(scoreText,scorePosition)
    creditsText = scoreNumberFont.render(str(credits),True,black)
    screen.blit(creditsText,creditsPosition)

def sidebarText(imageNamesList,imageScroll,oneTextPosition,
twoTextPosition,threeTextPosition):
    #Blits improvement descriptions.  Called repeatedly in main loop.
    font = pygame.font.Font("Care Bear Family.ttf",18)
    oneText = font.render(imageNamesList[imageScroll],True,black)
    screen.blit(oneText,oneTextPosition)
    twoText = font.render(imageNamesList[imageScroll+1],True,black)
    screen.blit(twoText,twoTextPosition)
    threeText = font.render(imageNamesList[imageScroll+2],True,black)
    screen.blit(threeText,threeTextPosition)

def displaySplashScreen(event):
    #Displays the splash screen.
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        #Splash screen disappears and game begins when s pressed.
        return False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
        displayInstructions()
        return True
    else:
        y = 0
        outerPos = [20,20,1160,660]
        spacing = 40
        splashMessage = """                             ECO CITY
        
                      By Raphael Astrow
        
        Purchase city improvements to satisfy
        your city's rapidly growing population.
        Every improvement costs credits, as will be
        described during the game. If you run
        into debt or your population's satisfaction
        reaches zero, it is game over.

         Press and hold i to read instructions
        
                      PRESS S TO START!"""

        pygame.draw.rect(screen,khaki,outerPos,2) 
        splashFont = pygame.font.Font("Carleton.ttf", 40)
        for line in splashMessage.splitlines():
            splashText = splashFont.render(
            line,True,black)
            screen.blit(splashText,[100,70+y*spacing])
            y += 1
        return True

def displayInstructions():
    #Displays the game instructions.
    y = 0
    outerPos = [20,20,1160,660]
    spacing = 50
    instructionsMessage ="""                          INSTRUCTIONS

    1. Press p to pause.
    2. Press r to restart.
    3. Use the arrow keys to scroll the map.
    4. Purchase improvements from the
    "Improvements" sidebar.
    5. Do not allow your credits or
    satisfaction score to reach zero.
    
                          PRESS S TO START!"""
    pygame.draw.rect(screen,khaki,outerPos,2)
    instructionsFont = pygame.font.Font("Carleton.ttf", 40)
    for line in instructionsMessage.splitlines():
        instructionsText = instructionsFont.render(
        line,True,black)
        screen.blit(instructionsText,[100,70+y*spacing])
        y += 1

def displayPauseScreen(event):
    #Displays the pause screen.
    outerPos = [20,20,1160,660]
    spacing = 40
    if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
        #If u is pressed, game is unpaused.
        return False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
        displayInstructions()
        return True
    else:
        y = 0
        pauseMessage = """                           Game paused.
        
                       Press u to unpause.
       Press and hold i to view instructions."""
        pygame.draw.rect(screen,khaki,outerPos,2)
        pauseFont = pygame.font.Font("Carleton.ttf", 40)
        for line in pauseMessage.splitlines():
            pauseText = pauseFont.render(
            line,True,black)
            screen.blit(pauseText,[100,270+y*spacing])
            y += 1
        return True 

def displayGameOver(event,highScores,displayThem):
    #Displays the game over screen.
    outerPos = [20,20,1160,660]
    spacing = 40
    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        return False,False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
        #If h is pressed and held, high score list appears.
        displayThem = displayHighScores(event,highScores)
        return True,displayThem
    else:
        y = 0
        pauseMessage = """                         GAME OVER.
         
                      Press r to restart.

          Hold down h to view high scores."""
        pygame.draw.rect(screen,khaki,outerPos,2)
        pauseFont = pygame.font.Font("Carleton.ttf", 40)
        for line in pauseMessage.splitlines():
            pauseText = pauseFont.render(
            line,True,black)
            screen.blit(pauseText,[100,270+y*spacing])
            y += 1
        return True,displayThem

def displayHighScores(event,highScores):
    #Displays the high score list.
    outerPos = [20,20,1160,660]
    spacing = 40
    yStart = 270
    nums = []
    y1 = y2 = 0
    high = highScores[0].split()
    for element in high:
        sor = element.split("...")
        nums += [int(sor[1])]
    nums.sort()
    scoreMessage = """                         HIGH SCORES
    
                        Press r to restart"""
    pygame.draw.rect(screen,khaki,outerPos,2)
    scoreFont = pygame.font.Font("Carleton.ttf", 40)
    for line in scoreMessage.splitlines():
        messageText = scoreFont.render(line,True,black)
        screen.blit(messageText,[100,100+y1*spacing])
        y1 += 1
    toUse = []
    for scr in range(len(nums)-1,-1,-1):
        for listing in high:
            if str(nums[scr]) in listing and listing not in toUse:
                toUse += [listing]
                break
    length = len(toUse)
    for element in range(len(toUse)):
        if element < 5:
            scoreText = scoreFont.render(
            toUse[element],True,black)
            numberText = scoreFont.render(str(y2+1),True,black)
            dotText = scoreFont.render(".",True,black)
            screen.blit(scoreText,[530,yStart+y2*spacing])
            screen.blit(numberText,[480,yStart+y2*spacing])
            screen.blit(dotText,[505,yStart+y2*spacing])
            y2 += 1

def displayNameScreen(event,name,recentlyPressed,recentlyPressed2,
                        recentlyPressed3):
    #Displays the name screen and establishes a name entering
    #system by defining key presses.
    y = 0
    outerPos = [20,20,1160,660]
    spacing = 40
    nameMessage = """              PRESS ENTER TO START!
    
    Please enter your first name or nickname.
    
                  (Limit 8 characters)"""
  
    pygame.draw.rect(screen,khaki,outerPos,2)
    pygame.draw.rect(screen,khaki,[285,300,600,150],2)
    nameFont = pygame.font.Font("Carleton.ttf",40)
    for line in nameMessage.splitlines():
        messageText = nameFont.render(line,True,black)
        screen.blit(messageText,[120,70+y*spacing])
        y += 1
    limit = 7
    if event.type == pygame.KEYDOWN:
        if recentlyPressed == False:
        #Recently pressed variables are used to prevent
        #double counting of key presses.
            recentlyPressed = True
        elif recentlyPressed2 == False:
            recentlyPressed2 = True
        elif recentlyPressed3 == False:
            recentlyPressed3 = True
        elif event.key == K_RETURN:
            name += ""
            return False,name,False,False,False
        elif event.key == K_BACKSPACE:
            name = name[:-1]
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_a and len(name) <= limit:
            name += "A"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_b and len(name) <= limit:
            name += "B"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_c and len(name) <= limit:
            name += "C"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_d and len(name) <= limit:
            name += "D"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_e and len(name) <= limit:
            name += "E"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_f and len(name) <= limit:
            name += "F"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_g and len(name) <= limit:
            name += "G"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_h and len(name) <= limit:
            name += "H"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_i and len(name) <= limit:
            name += "I"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_j and len(name) <= limit:
            name += "J"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_k and len(name) <= limit:
            name += "K"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_l and len(name) <= limit:
            name += "L"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_m and len(name) <= limit:
            name += "M"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_n and len(name) <= limit:
            name += "N"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_o and len(name) <= limit:
            name += "O"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_p and len(name) <= limit:
            name += "P"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_q and len(name) <= limit:
            name += "Q"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_r and len(name) <= limit:
            name += "R"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_s and len(name) <= limit:
            name += "S"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_t and len(name) <= limit:
            name += "T"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_u and len(name) <= limit:
            name += "U"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_v and len(name) <= limit:
            name += "V"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_w and len(name) <= limit:
            name += "W"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_x and len(name) <= limit:
            name += "X"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_y and len(name) <= limit:
            name += "Y"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
        elif event.key == K_z and len(name) <= limit:
            name += "Z"
            recentlyPressed = recentlyPressed2 =\
            recentlyPressed3 = False
    if name != None:
        nameText = nameFont.render(name,True,black)
        screen.blit(nameText,[550-len(name)*11,352])
    return (True,name,recentlyPressed,
    recentlyPressed2,recentlyPressed3)

def miniMap(backHor,backVer,newImages):
    #Displays a minimap that mimics the main map.
    n = newImages
    adjust = 9
    screen.blit(miniGrass,[960,490])
    pygame.draw.rect(screen,khaki,[960,490,170,170],2) 
    pygame.draw.rect(screen,black,[1012-backHor/adjust,
    529-backVer/adjust,66,92],1)#This rectangle slides according
    #to main map scrolling.
    for i in range(len(newImages)):
        for j in range(len(newImages[0])):
            if newImages[i][j] != False:
                tempPosition = [j*31+981,i*26+520]
                new =\
                pygame.transform.scale(newImages[i][j],(30,30))
                screen.blit(new,tempPosition)
                miniFont =\
                pygame.font.Font("Charrington Bold.ttf", 50)

def keyPressedInGame(event,backVer,backHor,pauseScreen,over):
    #Calls function outside main loop that draws init images.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and backHor <= 450\
        and not drOne and not drTwo and not drThree:
            backHor += 6
        elif event.key == pygame.K_RIGHT and backHor >= -447\
        and not drOne and not drTwo and not drThree:
            backHor -= 6
        elif event.key == pygame.K_UP and backVer <= 325\
        and not drOne and not drTwo and not drThree:
            backVer += 6
        elif event.key == pygame.K_DOWN and backVer >= -331\
        and not drOne and not drTwo and not drThree:
            backVer -= 6
        elif event.key == pygame.K_p:
            pauseScreen = True
        elif event.key == pygame.K_r:
            over = True
    #Map position changed according to user scrolling.
    backgroundPosition = [backHor-430,backVer-308]
    return backVer,backHor,pauseScreen,over,backgroundPosition

def addScore(over):
    if over == True:
        c1 = ""
        for element in highScores:
            c1 += str(element)
        combo = c1 + " " + name + "..." + str(score)
        saveText(combo)

recentlyPressed = recentlyPressed2 =\
recentlyPressed3 = False
#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(green)

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    #Control which screen is displayed.
    if splashScreen == True:
        splashScreen = displaySplashScreen(event)
    elif nameScreen == True:
        (nameScreen,name,recentlyPressed,
        recentlyPressed2,recentlyPressed3) =\
        displayNameScreen(event,name,recentlyPressed,
        recentlyPressed2,recentlyPressed3)
    elif pauseScreen == True:
        pauseScreen = displayPauseScreen(event)
    elif over == True:
        highScores = loadTextList()
        over,displayThem =\
        displayGameOver(event,highScores,displayThem)
        if over == False:
        #Restarts the game.
            highScores = loadTextList()
            (lineNumber,descriptionsText,display,randList,
            satisfactionScore,populationScore,score,credits,
            scoreLength,populationLength,satisfactionLength,
            creditsLength,imageScroll,backHor,backVer,
            oneTextPosition,twoTextPosition,threeTextPosition,
            populationPosition,satisfactionPosition,
            scorePosition,creditsPosition,drOne,drTwo,drThree,
            recentlyScrolled,recentlyScrolled2,displayThem,
            descriptionPosition,printed,newImages,occupied,
            oldOccupied,oldImages,usedImages,imageOne,
            imageTwo,imageThree,splashScreen,pauseScreen,over,
            nameScreen,name,highScores) =\
            restarting(imageList,imageNamesPositionsXList)
    else:
        #Image scrolling control.
        imageOne,imageTwo,imageThree =\
        defineImages(imageList,imageScroll) 
        onSidebar = [imageOne,imageTwo,imageThree]
        #Scrolling and other in game key presses.
        backVer,backHor,pauseScreen,over,backgroundPosition =\
        keyPressedInGame(event,backVer,backHor,pauseScreen,over)
        #Random person variables.
        toAdd,satisfactionScore = randomSelection(
        populationScore,satisfactionScore,manImage,
        randList,backHor,backVer)
        randList = blitBoard(backgroundImage,backgroundPosition,
        imageOne,imageTwo,imageThree,upArrowImage,
        downArrowImage,newImages,occupied,highX,
        highY,corner1,corner2,corner3,corner4,backHor,backVer,
        toAdd,randList,manImage)
        #Cross out used images.
        crossOut(screen,imageList, onSidebar, newImages,khaki)
        #Score lengths
        scoreLength = len(str(score))-1
        populationLength = len(str(populationScore))-1
        satisfactionLength = len(str(satisfactionScore))-1
        creditsLength = len(str(credits))-1
        #Updates X Values of improvements captions.
        (oneTextPosition,twoTextPosition,threeTextPosition,
        populationPosition,satisfactionPosition,scorePosition,
        creditsPosition) =\
        updatedPositions(imageScroll,populationLength,
        satisfactionLength,scoreLength,creditsLength,
        imageNamesPositionsXList)
        
        #Scores and sidebar text
        sidebarText(imageNamesList,imageScroll,oneTextPosition,
        twoTextPosition,threeTextPosition) 
        blitScores()
        #Population growth
        populationScore +=\
        populationGrowth(newImages,universityImage)
        over = isGameOver(satisfactionScore,credits,over) 
        addScore(over)
        #INITIALIZE IMAGE DRAG SECTION
        (drOne,drTwo,drThree,imageScroll,display,event,
        onSidebar,newImages,credits,score,satisfactionScore,
        lineNumber,descriptionsText,x,y,printed,usedImages) =\
        imageDrag(drOne,drTwo,drThree,imageScroll,display,event,
        onSidebar,newImages,credits,score,satisfactionScore,
        lineNumber,descriptionsList,descriptionsText,
        descriptionPosition,printed,imageOne,imageTwo,
        imageThree,usedImages,backHor,backVer)
        #Arrow button clicking
        (lineNumber,descriptionsText,imageScroll,
        recentlyScrolled,recentlyScrolled2) =\
        arrowButtons(event,x,y,imageScroll,imageList,lineNumber,
        descriptionsText,recentlyScrolled,recentlyScrolled2)

        #IMAGE IS BEING DRAGGED AND THEN PLACED SECTION
        drOne,drTwo,drThree,occupied,newImages =\
        dragAndPlace(drOne,drTwo,drThree,imageOne,
        imageTwo,imageThree,x,y,occupied,newImages)
        
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
