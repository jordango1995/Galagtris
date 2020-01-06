 ###   ###  #      ###   ###  ##### ####  #####  ####
#     #   # #     #   # #       #   #   #   #   #   
#  ## ##### #     ##### #  ##   #   ####    #    ###
#   # #   # #     #   # #   #   #   #  #    #       #
 #### #   # ##### #   #  ####   #   #   # ##### ####


from random import randrange as rand
import time
import collisionDetection as collFile
import pygame, sys
import random
#from itertools import cycle, islice
#import os
#import signal


config = {
    'cell_size':    10,
    'cols':         30,
    'rows':         16,
    'delay':        60, #Subject to change, lower for higher difficulty
    'maxfps':       60
}


colors = [
    (0,   0,   0  ), #Black - 0
    (255, 0,   0  ), #Red - 1
    (0,   150, 0  ), #Green - 2
    (0  , 0,   255), #Blue - 3
    (255, 120, 0  ), #Orange - 4
    (255, 255, 0  ), #Yellow - 5
    (180, 0,   255), #Purple - 6
    (0,   220, 220), #Light Blue - 7
    (255, 255, 255), #White - 8
    (102, 153, 255), #Custom color for player ship - 9
    (146, 143, 195), #Indigo - 10
    (139,   0, 255)  #Violet - 11
]

c = 1
ship_shapes = [
    [[1, 1, 1],     #shape0
     [0, 1, 0]],

    [[c, c],        #shape1
     [c]],

    [[c, c],        #shape2
     [0, c]],

    [[c],           #shape3
     [c]],

    [[0, 2, 2],     #shape4
     [2, 2]],

    [[0, c],        #shape5
     [c, c]],

    [[3, 3],        #shape6
     [0, 3, 3]],

    [[c],           #shape7
     [c, c]],

    [[4],           #shape8
     [4, 4, 4]],

    [[4],           #shape9
     [0, 4, 4]],

    [[c],           #shape10
     [0, c]],

    [[0, 0, 5],     #shape11
     [5, 5, 5]],
    
    [[0, 0, 5],     #shape12
     [5, 5]],

    [[0, c],        #shape13
     [c]],

    [[6, 6, 6, 6]], #shape14

    [[6, 6, 6]],    #shape15

    [[c, c]],       #shape16

    [[7, 7],        #shape17
     [7, 7]],

    [[4],           #shape18
     [0, 0, 4]],

    [[0, 0, 5],     #shape19
     [5]],

    [[c]],          #shape20 - is same as index 21, but index 21 is reserved for rainbow effect

    [[c]],          #white enemy blast -- used to be 8, now it's c; that's why all code refers to it as white blast

    [[8]],          #player ship. Change the 8 to a c later so that it can be a variable color for the rainbow effect when powerups are added

    [[5]]           #yellow player blast

]

def rotate_clockwise(shape):
    return [[shape[y][x]
                 for y in range(len(shape))]
            for x in range(len(shape[0]) - 1, -1, -1)]


def white_check_collision(blast, blastOffset, ship, shipOffset):
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        return True


def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy + off_y - 1][cx + off_x] += val
    return mat1


def new_board():
    board = [[0 for x in range(config['cols'])]
                 for y in range(config['rows'])]
    board += [[1 for x in range(config['cols'])]]
    return board


class TetrisApp(object):
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((100, 100))
        pygame.key.set_repeat(250, 25)
        self.width = config['cell_size']*config['cols']
        self.height = config['cell_size']*config['rows']
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.event.set_blocked(pygame.MOUSEMOTION) #Blocks mouse motions as they are not needed

        self.init_game()


    def new_ship(self):
        self.badShip = ship_shapes[0]
        self.badShip_x = int(config['cols'] / 2 - len(self.badShip[0]) / 2)
        self.badShip_y = 0

        self.yourShip = ship_shapes[22]
        self.yourShip_x = int(config['cols'] / 2)
        self.yourShip_y = int(config['rows'] - 3)

        self.blastYellow1, self.blastYellow2 = ship_shapes[23], ship_shapes[23] 
        self.blastYellow1_x, self.blastYellow1_y = -1, -1
        self.blastYellow2_x, self.blastYellow2_y = -1, -1

        self.blastWhite1, self.blastWhite2, self.blastWhite3 = ship_shapes[21], ship_shapes[21], ship_shapes[21]
        self.blastWhite1_x, self.blastWhite2_x, self.blastWhite3_x = self.badShip_x + 1, self.badShip_x + 1, self.badShip_x + 1 
        self.blastWhite1_y, self.blastWhite2_y, self.blastWhite3_y = self.badShip_y + 1, self.badShip_y + 1, self.badShip_y + 1 

        self.score = 0

        self.shootFlag1 = False #Only want the player to be able to have two shots on screen at once
        self.shootFlag2 = False

        rainbowFlag = False

        randBadStart = random.randint(0,1) #Randomly decides whether bad ship begins by moving left or right
        if randBadStart == 0:
            self.borderFlag = "Left"
        else:
            self.borderFlag = "Right"

        self.badShipColor = "Red" #Bad ship always begins as red


    def init_game(self):
        self.board = new_board()
        self.new_ship()


    def score_tracker(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = pygame.font.SysFont("couriernew", 12).render(line, False, (255, 255, 255), (0, 0, 0)) #print(pygame.font.get_fonts()) #will print list of all available pygame fonts

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x = 20
            msgim_center_y = 12

            self.screen.blit(msg_image, (200, 140)) #Puts player's score in the bottom right of the board
            #self.width // 2-msgim_center_x,
            #self.height // 2-msgim_center_y+i*22))


    def gameover_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = pygame.font.SysFont("couriernew", 20).render(line, False, (255, 255, 255), (0, 0, 0)) #print(pygame.font.get_fonts()) #will print list of all available pygame fonts

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y = int((1.5)*msgim_center_y) #//= 2

            self.screen.blit(msg_image, (self.width // 2 - msgim_center_x, self.height // 2 - msgim_center_y + i*22)) #Gameover message appears in center of board


    def draw_matrix(self, matrix, offset):
        off_x, off_y = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(self.screen,
                                     colors[val],
                                     pygame.Rect((off_x + x)*config['cell_size'],
                                                (off_y + y)*config['cell_size'],
                                                config['cell_size'], config['cell_size']), 0)


    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.yourShip_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > config['cols'] - len(self.yourShip[0]):
                new_x = config['cols'] - len(self.yourShip[0])
            self.yourShip_x = new_x


    def quit(self):
        self.score_tracker("Exiting...")
        self.testFlag = False
        pygame.display.update()
        exit()
        #os.kill(os.getppid(), signal.SIGTERM)


    def drop(self):
        if not self.gameover and not self.paused:

            if self.score >= 100:
                config['delay'] = 50

            if self.badShip_x == 0: #Checks to see if bad ship is all the way left
                self.borderFlag = "Left"
                self.badShip_x += 1
            elif self.badShip_x == int(config['cols']) - 3: #Checks to see if bad ship is all the way right. Need to make the -3 a variable that changes based off badShip index
                self.borderFlag = "Right"
                self.badShip_x -= 1

            if self.borderFlag == "Left": #Keeps bad ship going right until it reaches border again; may change later to randomize movement behavior
                self.badShip_x += 1
            elif self.borderFlag == "Right": #Keeps bad ship going left until it reaches border again; may change later to randomize movement behavior
                self.badShip_x -= 1

            #Confusing way to make sure that enemy blast can continue even after enemy ship is destroyed
            if self.badShip_y == 0:
                self.blastWhite1_y += 1
                if self.blastWhite2_y >= self.badShip_y:
                    self.blastWhite2_y += 1
                    self.blastWhite3_y += 1
                    if self.blastWhite2_y >= int(config['rows']) + 1: #Resets enemy shots when they've reached bottom edge of board
                        self.blastWhite2_y, self.blastWhite3_y = -1, -1
            else:
                if self.blastWhite1_y != -1:
                    self.blastWhite1_y += 1
                else:
                    if self.blastWhite1_y == int(config['rows']):
                        self.blastWhite1_y = -1


            #Not sure yet why this func won't work
            '''
            def moveYellow(blastYellow_x, blastYellow_y, shootFlag):
                blastYellow_y = -1
                if blastYellow_y == -2:
                    shootFlag = False
                    blastYellow_x, blastYellow_y = -1, -1
            '''


            #For the first yellow enemy blast
            if self.shootFlag1 == True:
                #moveYellow(self.blastYellow1_x, self.blastYellow1_y, self.shootFlag1)
                self.blastYellow1_y -= 1
                if self.blastYellow1_y == -2:
                    self.shootFlag1 = False
                    self.blastYellow1_x, self.blastYellow1_y = -1, -1

            #For the second yellow enemy blast
            if self.shootFlag2 == True:
                #moveYellow(self.blastYellow2_x, self.blastYellow2_y, self.shootFlag2)
                self.blastYellow2_y -= 1
                if self.blastYellow2_y == -2:
                    self.shootFlag2 = False
                    self.blastYellow2_x, self.blastYellow2_y = -1, -1


            #Recolors bad ship when it's supposed to be a new bad ship
            def recolorShip(ship, shipList, newColor):
                ###self.badShip = ship_shapes[newShipIndex] <----Temporarily commenting out
                for i in range(0, len(ship_shapes) - 3): # Triple for loop to go through each cell of each ship. If cell isn't black, it recolors it
                    if i == ship_shapes.index(self.badShip):
                        for j in range(0, len(ship_shapes[i])):
                            for k in range(0, len(ship_shapes[i][j])):
                                if ship_shapes[i][j][k] != 0:
                                    ship_shapes[i][j][k] = newColor


            #This func needs reworking as it makes it impossible to randomize order of enemy ships after defeating one. May try tuple approach
            def healBadShip(ship, blastWhite1_x, blastWhite1_y, blastWhite2_x, blastWhite2_y, currentColor):
                x1, y1 = 1, 2
                x2, y2 = 0, 1
                x3, y3 = 2, 1

                if currentColor == "Green":
                    y1 = 2
                    y2 = 2
                    print("Green")
                elif currentColor == "Blue":
                    y1 = 1
                    y2 = 2
                    print("Blue")
                elif currentColor == "Orange":
                    y1 = 2
                    print("Orange")

                #print(x1, y1, x2, y2, x3, y3)

                #Triple enemy white blast
                self.blastWhite1_x = self.badShip_x + x1 #White center blast 
                self.blastWhite1_y = self.badShip_y + y1 #White center blast
                self.blastWhite2_x = self.badShip_x + x2 #White left blast
                self.blastWhite2_y = self.badShip_y + y2 #White left blast
                self.blastWhite3_x = self.badShip_x + x3 #White right blast
                self.blastWhite3_y = self.badShip_y + y3 #White right blast



            #Checking to see if yellow player blast hit enemy ship
            def updateScore(currentShipIndex, currentColor, newColor, newShipForLeft, newShipForRight, newShipForBack, newShipForCenter):
                #for i in range(0, len(ship_shapes) - 3):
                #if self.badShip == ship_shapes[i]:
                #for j in range(0, 19):
                collCall = "collFile.shape" + str(currentShipIndex) + "_check_collision"
                hitFlag1 = eval(collCall + "(self.blastYellow1, (self.blastYellow1_x, self.blastYellow1_y), self.badShip, (self.badShip_x, self.badShip_y))")
                hitFlag2 = eval(collCall + "(self.blastYellow2, (self.blastYellow2_x, self.blastYellow2_y), self.badShip, (self.badShip_x, self.badShip_y))")

                #There HAS to be a more efficient way to do this; fix later
                if hitFlag1 == "Left" or hitFlag2 == "Left": 
                    if hitFlag1 == "Left":
                        self.blastYellow1_x, self.blastYellow1_y = -1, -1
                        self.shootFlag1 = False
                    elif hitFlag2 == "Left":
                        self.blastYellow2_x, self.blastYellow2_y = -1, -1
                        self.shootFlag2 = False
                    self.score += 100
                    print("Left Wing Hit, Score: " + str(self.score))
                    self.badShip = ship_shapes[newShipForLeft]
                    recolorShip(self.badShip, ship_shapes, currentColor) 
                    
                elif hitFlag1 == "Right" or hitFlag2 == "Right": 
                    if hitFlag1 == "Right":
                        self.blastYellow1_x, self.blastYellow1_y = -1, -1
                        self.shootFlag1 = False
                    elif hitFlag2 == "Right":
                        self.blastYellow2_x, self.blastYellow2_y = -1, -1
                        self.shootFlag2 = False
                    self.score += 100
                    print("Right Wing Hit, Score: " + str(self.score))
                    self.badShip = ship_shapes[newShipForRight]
                    recolorShip(self.badShip, ship_shapes, currentColor)

                elif hitFlag1 == "Center" or hitFlag2 == "Center":
                    self.score = (self.score + 1000) if self.badShip != ship_shapes[3] else (self.score + 100)
                    print("Center Hit, Score: " + str(self.score))
                    if self.badShip != ship_shapes[3]:
                        self.badShip = ship_shapes[newShipForCenter]
                        recolorShip(self.badShip, ship_shapes, newColor)
                    else:
                        self.badShip = ship_shapes[20]
                        recolorShip(self.badShip, ship_shapes, currentColor)

                elif hitFlag1 == "Back" or hitFlag2 == "Back":
                    print("Back Hit... Reviving enemy ship")
                    healBadShip(self.badShip, self.blastWhite1_x, self.blastWhite1_y, self.blastWhite2_x, self.blastWhite2_y, currentColor)
                    self.badShip = ship_shapes[newShipForBack]

                elif hitFlag1 == "Last Cell" or hitFlag2 == "Last Cell":
                    self.score += 500
                    print("Last Cell Hit, Score: " + str(self.score))
                    self.badShip = ship_shapes[newShipForCenter]
                    recolorShip(self.badShip, ship_shapes, newColor)

                    ###EXPERIMENTAL COMPACT VERSION FOR THIS^: ###
                    '''
                if hitFlag1 == "Left":
                    self.blastYellow1_x, self.blastYellow1_y = -1, -1
                    self.shootFlag1 = False
                elif hitFlag2 == "Left":
                    self.blastYellow2_x, self.blastYellow2_y = -1, -1
                    self.shootFlag2 = False
                    #WILL FINISH LATER...
                    '''
                    ####################################


            #This func NEEDS updating to remove redundancy... try unpacking tuples approach later; there's an obvious pattern here
            def nextShip(badShipColor):
                #newColor = self.badShipColor + 1
                #if newColor > 7:
                #    newColor = 1

                if badShipColor == "Red":
                    return 1, 2, 0, 4
                elif badShipColor == "Green":
                    return 2, 3, 4, 6
                elif badShipColor == "Blue":
                    return 3, 4, 6, 8
                elif badShipColor == "Orange":
                    return 4, 5, 8, 11
                elif badShipColor == "Yellow":
                    return 5, 6, 11, 14
                elif badShipColor == "Purple":
                    return 6, 7, 14, 17
                elif badShipColor == "Light Blue":
                    return 7, 1, 17, 0


            badShipIndex = ship_shapes.index(self.badShip)

            currentColor, newColor, newShipForBack, newShipForCenter = nextShip(self.badShipColor)

            if badShipIndex == 0:
                self.badShipColor = "Red"
                newShipForLeft, newShipForRight = 1, 2
            elif badShipIndex == 1:
                newShipForLeft, newShipForRight = 16, 3
            elif badShipIndex == 2:
                newShipForLeft, newShipForRight = 3, 16
            elif badShipIndex == 3:
                newShipForLeft, newShipForRight = newShipForCenter, newShipForCenter
            elif badShipIndex == 4:
                self.badShipColor = "Green"
                newShipForLeft, newShipForRight = 1, 5
            elif badShipIndex == 5:
                newShipForLeft, newShipForRight = 3, 13
            elif badShipIndex == 6:
                self.badShipColor = "Blue"
                newShipForLeft, newShipForRight = 7, 2
            elif badShipIndex == 7:
                newShipForLeft, newShipForRight = 10, 3
            elif badShipIndex == 8:
                self.badShipColor = "Orange"
                newShipForLeft, newShipForRight = 9, 7
            elif badShipIndex == 9:
                newShipForLeft, newShipForRight = 18, 10
            elif badShipIndex == 10:
                newShipForLeft, newShipForRight = 10, 20
            elif badShipIndex == 11:
                self.badShipColor = "Yellow"
                newShipForLeft, newShipForRight = 5, 12
            elif badShipIndex == 12:
                newShipForLeft, newShipForRight = 13, 19
            elif badShipIndex == 13:
                newShipForLeft, newShipForRight = 20, 13
            elif badShipIndex == 14:
                self.badShipColor = "Purple"
                newShipForLeft, newShipForRight = 15, 15
            elif badShipIndex == 15:
                newShipForLeft, newShipForRight = 16, 16
            elif badShipIndex == 16:
                newShipForLeft, newShipForRight = 20, 20
            elif badShipIndex == 17:
                self.badShipColor = "Light Blue"
                newShipForLeft, newShipForRight = 2, 1
            elif badShipIndex == 18:
                newShipForLeft, newShipForRight = 18, 20
            elif badShipIndex == 19:
                newShipForLeft, newShipForRight = 20, 19
            elif badShipIndex == 20:
                newShipForLeft, newShipForRight = newShipForCenter, newShipForCenter

            currentColor, newColor, newShipForBack, newShipForCenter = nextShip(self.badShipColor)

            updateScore(ship_shapes.index(self.badShip), currentColor, newColor, newShipForLeft, newShipForRight, newShipForBack, newShipForCenter)


            #Checking to see if white enemy blast(s) hits player
            if white_check_collision(self.blastWhite1, (self.blastWhite1_x, self.blastWhite1_y), self.yourShip, (self.yourShip_x, self.yourShip_y)) or \
               white_check_collision(self.blastWhite2, (self.blastWhite2_x, self.blastWhite2_y), self.yourShip, (self.yourShip_x, self.yourShip_y)) or \
               white_check_collision(self.blastWhite3, (self.blastWhite3_x, self.blastWhite3_y), self.yourShip, (self.yourShip_x, self.yourShip_y)):
                self.gameover = True

            #Resets white enemy blast when it goes offscreen
            if self.blastWhite1_y > int(config['rows']) and self.badShip_y == 0:
                randShot = random.randint(0, 2) #1/3 chance that enemy ship will shoot immediately after its first shot disappears
                if randShot == 1:
                    self.blastWhite1_x, self.blastWhite1_y = self.badShip_x + 1, self.badShip_y + 2 #This may need to be adjusted later when the enemy ship has a front that is a different offset than x+1 and y+2
                    
            #Rainbow effect
            '''
            if rainbowFlag == True:
                rainbowList = [1, 4, 5, 2, 3, 10, 11]
                yourShipIndex = 22 #ship_shapes.index(self.yourShip) #<----For some reason this won't work; it gives incorrect index...

                for i in range(0, len(rainbowList)):
                    if ship_shapes[yourShipIndex][0][0] == rainbowList[i]:
                        if i != len(rainbowList) - 1:
                            ship_shapes[yourShipIndex][0][0] = rainbowList[i+1]
                        else:
                            ship_shapes[yourShipIndex][0][0] = rainbowList[0]
                        break
            else:
                ship_shapes[22][0][0] = colors[8]
            '''
            rainbowList = [1, 4, 5, 2, 3, 10, 11]
            whiteBlast1Index = 21 #ship_shapes.index(self.yourShip) #<----For some reason this won't work; it gives incorrect index...

            for i in range(0, len(rainbowList)):
                if ship_shapes[whiteBlast1Index][0][0] == rainbowList[i]:
                    if i != len(rainbowList) - 1:
                        ship_shapes[whiteBlast1Index][0][0] = rainbowList[i+1]
                    else:
                        ship_shapes[whiteBlast1Index][0][0] = rainbowList[0]
                    break


            #print(time.monotonic())


    def shoot(self):
        if self.shootFlag1 == True:
            self.shootFlag2 = True

        self.shootFlag1 = True
        
        if not self.gameover and not self.paused:
            if self.blastYellow1_x == -1 and self.blastYellow1_y == -1:
                self.blastYellow1_x, self.blastYellow1_y = self.yourShip_x, self.yourShip_y - 1
            if self.blastYellow2_x == -1 and self.blastYellow2_y == -1 and self.shootFlag2 == True:
                self.blastYellow2_x, self.blastYellow2_y = self.yourShip_x, self.yourShip_y - 1


    def toggle_pause(self):
        self.paused = not self.paused


    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False


    def restart(self):
        self.badShip = [[1, 1, 1], #Hardcoded to always start with red enemy ship; might change this later if I randomize enemy ship order
                        [0, 1, 0]]
        self.gameover = True
        self.start_game()


    def run(self):
         
        key_actions = {
            'ESCAPE':       self.quit,
            'LEFT':         lambda:self.move(-1),
            'RIGHT':        lambda:self.move(+1),
            'DOWN':         self.drop,
            #'UP':           self.rotate_clockwise,
            'p':            self.toggle_pause,
            'SPACE':        self.shoot,
            'RSHIFT':       self.restart
        }

        self.gameover = False
        self.paused = False
                
        pygame.time.set_timer(pygame.USEREVENT+1, config['delay'])
        dont_burn_my_cpu = pygame.time.Clock()

        while 1:
            self.screen.fill((0, 0, 0))
            if self.gameover:
                self.gameover_msg("Game Over\n\nYour Score: " + str(self.score) + "\n\nPress shift to play again")
            else:
                if self.paused:
                    self.score_tracker("Paused")
                else:
                    c = 3 #May or may not still need this
                    #Draws the matrixes of everything (enemy, player, yellow blasts, and white blasts) using their updated coordinates
                    self.draw_matrix(self.board, (0, 0))
                    self.draw_matrix(self.badShip, (self.badShip_x, self.badShip_y))
                    self.draw_matrix(self.yourShip, (self.yourShip_x, self.yourShip_y))
                    self.draw_matrix(self.blastYellow1, (self.blastYellow1_x, self.blastYellow1_y))
                    self.draw_matrix(self.blastYellow2, (self.blastYellow2_x, self.blastYellow2_y))
                    self.draw_matrix(self.blastWhite1, (self.blastWhite1_x, self.blastWhite1_y))
                    self.draw_matrix(self.blastWhite2, (self.blastWhite2_x, self.blastWhite2_y))
                    self.draw_matrix(self.blastWhite3, (self.blastWhite3_x, self.blastWhite3_y))

            if self.gameover != True:
                self.score_tracker("Score: " + str(self.score))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT+1:
                    self.drop()
                elif event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    for key in key_actions:
                        if event.key == eval("pygame.K_" + key):
                            key_actions[key]()

            dont_burn_my_cpu.tick(config['maxfps'])

if __name__ == '__main__':
    App = TetrisApp()
    App.run()
                    
         
                
                
                    
                        
            

            



    
