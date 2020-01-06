
def white_check_collision(blast, blastOffset, ship, shipOffset):
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        return True

def shape0_check_collision(blast, blastOffset, ship, shipOffset): #
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 0, 1, 0, 2, 0, 1, 1) 
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):
        hitFlag = "Right"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''

def shape1_check_collision(blast, blastOffset, ship, shipOffset): #May need to use null to see if gen_check works for funcs without certain hitFlags, such as this one which has no center
    #return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 0, 0, 1, 0, null, null) 
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):      #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 0, 0, 1, 0, -10, -10) 

    

def shape2_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):  #No Center
    #    hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 0, 1, 0, 1, 1, -10, -10) 

def shape3_check_collision(blast, blastOffset, ship, shipOffset): #This is a tricky shape because there's only a center and back. If player hits center, I think this shape should go to the Last Cell shape
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    #if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):        #No Left
     #   hitFlag = "Left"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    #elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):      #No Right
     #   hitFlag = "Right"
    elif (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, -10, -10, 0, 0, -10, -10, 0, 1) 

def shape4_check_collision(blast, blastOffset, ship, shipOffset):
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 1, 0, 2, 0, 1, 1) 
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):
        hitFlag = "Right"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''

def shape5_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):      #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 1, 0, 1, 1, -10, -10) 

def shape6_check_collision(blast, blastOffset, ship, shipOffset):
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 0, 1, 0, 2, 1, 1, 1) 
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):
        hitFlag = "Right"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''

def shape7_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):      #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 0, 0, 1, 1, -10, -10) 

def shape8_check_collision(blast, blastOffset, ship, shipOffset):
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 0, 0, 2, 1, 1, 1) 
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):
        hitFlag = "Right"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''

def shape9_check_collision(blast, blastOffset, ship, shipOffset): #Subject to change. Current settings may be difficult for player
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    #if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):        #No Left
     #   hitFlag = "Left"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Right"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, -10, -10, 0, 0, 2, 1, 1, 1) 

def shape10_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    #if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):        #No Left
     #   hitFlag = "Left"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):      #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, -10, -10, 0, 0, 1, 1, -10, -10) 

def shape11_check_collision(blast, blastOffset, ship, shipOffset):
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 2, 0, 2, 1, 1, 1) 
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):
        hitFlag = "Right"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''

def shape12_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    #elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):      #No Right
     #   hitFlag = "Right"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 2, 0, -10, -10, 1, 1) 

def shape13_check_collision(blast, blastOffset, ship, shipOffset): #NOTE: I CHANGED THIS SO THAT THERE IS ONLY A LEFT AND A BACK. IT USED TO BE ONLY CENTER AND BACK
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):        
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    #elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):  #No Right
     #   hitFlag = "Right"
    #elif (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1): #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 1, 0, -10, -10, -10, -10) 

def shape14_check_collision(blast, blastOffset, ship, shipOffset):
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x and blast_off_y == ship_off_y) or (blast_off_x == ship_off_x + 1 and blast_off_y == ship_off_y):
        hitFlag = "Left"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):      #No Back
     #   hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2 and blast_off_y == ship_off_y) or (blast_off_x == ship_off_x + 3 and blast_off_y == ship_off_y):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):  #No Center
     #   hitFlag = "Center"
    return hitFlag

def shape15_check_collision(blast, blastOffset, ship, shipOffset):
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):      #No Back
     #   hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1 and blast_off_y == ship_off_y) or (blast_off_x == ship_off_x + 2 and blast_off_y == ship_off_y):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):      #No Center
     #   hitFlag = "Center"
    return hitFlag

def shape16_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Left"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):    #No Back
     #   hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):   #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 0, -10, -10, 1, 0, -10, -10) 

def shape17_check_collision(blast, blastOffset, ship, shipOffset): #Two Backs for this shape, but not two Centers
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x and blast_off_y == ship_off_y) or (blast_off_x == ship_off_x + 1 and blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):      #No Center
     #   hitFlag = "Center"
    return hitFlag

def shape18_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    #if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):        #No Left
     #   hitFlag = "Left"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):  #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, -10, -10, 0, 0, 2, 1, -10, -10) 

def shape19_check_collision(blast, blastOffset, ship, shipOffset):
    '''
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y + 1):
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):
        hitFlag = "Back"
    #elif (blast_off_x == ship_off_x + 2) and (blast_off_y == ship_off_y):      #No Right
     #   hitFlag = "Right"
    #elif (blast_off_x == ship_off_x + 1) and (blast_off_y == ship_off_y + 1):      #No Center
     #   hitFlag = "Center"
    return hitFlag
    '''
    return gen_check(blast, blastOffset, ship, shipOffset, 0, 1, 2, 0, -10, -10, -10, -10) 

def shape20_check_collision(blast, blastOffset, ship, shipOffset):
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x) and (blast_off_y == ship_off_y):
        hitFlag = "Last Cell"
    return hitFlag

def gen_check(blast, blastOffset, ship, shipOffset, x1, y1, x2, y2, x3, y3, x4, y4):
    blast_off_x, blast_off_y = blastOffset
    ship_off_x, ship_off_y = shipOffset
    hitFlag = "None"
    if (blast_off_x == ship_off_x + x1 and blast_off_y == ship_off_y + y1) and x1 != -10:
        hitFlag = "Left"
    elif (blast_off_x == ship_off_x + x2 and blast_off_y == ship_off_y + y2) and x2 != -10:
        hitFlag = "Back"
    elif (blast_off_x == ship_off_x + x3 and blast_off_y == ship_off_y + y3) and x3 != -10:
        hitFlag = "Right"
    elif (blast_off_x == ship_off_x + x4 and blast_off_y == ship_off_y + y4) and x4 != -10:
        hitFlag = "Center"
    return hitFlag
