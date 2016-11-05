#Det Zuper Zinzyge Zpil
#Textbased RPG
#GUI Underway
#
#TODO:
# Add inventory function
# Add main funtion

print ("Hi and Welcome to my game!")
import random
from random import randint

#Hero startstats
level           = 1
damage          = 1+level
minAttack       = 1
maxAttack       = 2
maxHealth       = 20+(level*10)
health          = 20+(level*10)
experience      = 0
experienceReq   = (level*100)
x               = 10
y               = 10
heroPos         = (x,y)
weakAttackMul   = 1
mediumAttackMul = 2
strongAttackMul = 3
world           = None

#World and monster list
worlds                      = ("ice-land", "mars", "underwater-world", "100 meter forest", "McDonald's playground")
iceLandMonsters             = ("a yeti", "a frost-giant", "a wampa", "the sirius patrol","a snow wolf","a snow giant", "a evil snowman", "a angry snow rabit", "avalance")
iceLandBosses               = ("a ice dragon", "a evil snowqueen", "putin")
iceLandUberBoss             = ("Santa Klaus")
marsMonsters                = ("mars-rover","meteor","alien","predetor","darude","zombie astronaut","exogorth","the silver surfer","parademon","baron of hell")
marsBosses                  = ("dark martian manhunter","jabba the hut","olifant")
marsUberBoss                = ("evil mars bar")
underWaterWorldMonsters     = ("shark","bikini bitch","steel-eel","mermaid","squirtle","sebastian","commander Rourge","goldfish","cursed pirate")
underWaterWorldBosses       = ("ariel","spongebob squarepants","davy jones")
underWaterWorldUberBoss     = ("Neptune")
hundredMeterForestMonsters  = ("ent","ewok","harambe","clayton","giant ant","quicksand","a gryll bear","ogre","troll")
hundredMeterForestBosses    = ("aragog","bulbasaur","shrek")
hundredMeterForestUberBoss  = ("winnie the poo")
mcDonaldsPlaygroundMonsters = ("cheese burger","fat bitch","mother of seven","hipster zombie","sagarin","nerd","rich kid","dj mcmuffin","mclovin")
mcDonaldsPlaygroundBosses   = ("the dude","biff tannen","donald trump")
mcDonaldsPlaygroundUberBoss = ("the burger king")

# Inventory list and stats
# List of stats as follows:
# Attack, defence,
# List of inventory as follows:
# Weapon, shoe, hat, pants, shirt, shield
basicSword      =(1,0)
basicShoe       =(0,1)
basicHat        =(1,1)
basicPants      =(0,1)
basicShirt      =(0,1)
basicShield     =(0,1)
heroInventory   =(basicSword,basicShoe,basicHat,basicPants,basicShirt,none)
inventoryUsed   =(basicSword,basicShoe,basicHat,basicPants,basicShirt,none)


def levelCal():
    '''
    Updates the xp of the character
    Also updates the stats of the character depending on the level
    '''
    global experience
    global level
    experienceGained=experience+(level*(randint(30,40)))
    experience=experience+experienceGained
    print ("You gained "+str(experienceGained)+" experience")
    if experience>=experienceReq:
        experience=experience-experienceReq
        level+=1
        damage=1+level
        health=20+(level*10)
        print "You leveled up!"

def moveandcheck():
    '''
    Movement lader en flytte sig rundt i et 20x20 grid ved at spoerge hvor man
    man rykke hen og aendrer x og y hvis man stadig er inde for mapped
    '''
    global x
    global y
    global heroPos
    while True:
        print ("You are currently at "+str(heroPos))
        move=raw_input("Where do you want to go from here?(up,down,right,left)")
        if move=="up" or "UP" or "Up":
            if y<10:
                y+=1
                heroPos=(x,y)
                print ("you are now at "+str(heroPos))
                break
            else:
                print "you can't go there"
        elif move=="down" or "Down" or "DOWN":
            if y>(-10):
                y-=1
                heroPos=(x,y)
                print ("you are now at "+str(heroPos))
                break
            else:
                print "you can't go there"
        elif move=="right" or "Right" or "RIGHT":
            if x<10:
                x+=1
                heroPos=(x,y)
                print ("you are now at "+str(heroPos))
                break
            else:
                print "you can't go there"
        elif move=="left" or "Left" or "LEFT":
            if x>(-10):
                x-=1
                heroPos=(x,y)
                print ("you are now at "+str(heroPos))
                break
            else:
                print "you can't go there"
        else:
            print "that is not an option"

def rollMonster():
    '''
    Monster roll bestemmer monster ud fra level
    og world og definerer monster stats derudfra
    '''
    global level
    global world
    global iceLandMonsters
    global iceLandBosses
    global marsMonsters
    global marsBosses
    global underWaterWorldMonsters
    global underWaterWorldBosses
    global hundredMeterForestMonsters
    global hundredMeterForestBosses
    global mcDonaldsPlaygroundMonsters
    global mcDonaldsPlaygroundBosses
    #TODO: This part should be done using a list of lists in the world variables
    if world=="ice-land":
        monsterClass=iceLandMonsters
        bossClass=iceLandBosses
    if world=="mars"
        monsterClass=marsMonsters
        bossClass=marsBosses
    if world=="underwater-world"
        monsterClass=underWaterWorldMonsters
        bossClass=underWaterWorldBosses
    if world=="100 meter forest"
        monsterClass=hundredMeterForestMonsters
        bossClass=hundredMeterForestBosses
    if world=="McDonald's playground"
        monsterClass=mcDonaldsPlaygroundMonsters
        bossClass=mcDonaldsPlaygroundBosses
    if level<10:
        monster=random.choice(monsterClass)
        if level<3:
            monsterLevel=level
        else:
            monsterLevel=randint(level-2,level+2)
        monsterHealth=randint(15+(10*monsterLevel),30+(10*monsterLevel))
        monsterMinAttack=monsterLevel
        monsterMaxAttack=monsterLevel+2
        print ("you met "+str(monster)+" it is level "+str(monsterLevel)+" and it has "+str(monsterHealth)+" health")
    else:
        bossRoll=randint(1,10)
        if bossRoll==1:
            monster=random.choice(bossClass)
            monsterLevel=15
            monsterHealth=200
            monsterMinAttack=20
            monsterMaxAttack=30
            print ("you met "+str(monster)+" it is level "+str(monsterLevel)+" and it has "+str(monsterHealth)+" health")
        else:
            monster=random.choice(monsterClass)
            monsterLevel=randint(level-2,level+2)
            monsterHealth=randint(15+(10*monsterLevel),30+(10*monsterLevel))
            monsterMinAttack=monsterLevel
            monsterMaxAttack=monsterLevel+2
            print ("you met "+str(monster)+" it is level "+str(monsterLevel)+" and it has "+str(monsterHealth)+" health")

def heroAttack():
    '''
    Heroattack attacks once with weak medium or strong and
    changes global variable: monsterHealth
    '''
    global monsterHealth
    global monster
    global minAttack
    global maxAttack
    while True:
        weakAttack=randint(90,100)
        mediumAttack=randint(40,60)
        strongAttack=randint(23,43)
        attackRoll=randint(1,100)
        while monsterHealth > 0:
            attackStrength=raw_input("which attack do you want to use? weak("+str(weakAttack)+"% chance)or medium("+str(mediumAttack)+"% chance) or strong("+str(strongAttack)+"% chance)?(weak,medium,strong)")
            if attackStrength=="weak":
                if attackRoll>weakAttack:
                    print "you miss(happens to even the best of us)"
                    break
                else:
                    dmgCal=randint(minAttack*weakAttackMul,maxAttack*weakAttackMul)
                    monsterHealth-=dmgCal
                    print ("you deal "+str(dmgCal)+" damage to "+str(monster))
                    break
            if attackStrength=="medium":
                if attackRoll>mediumAttack:
                    print "you miss(happens to even the best of us)"
                    break
                else:
                    dmgCal=randint(minAttack*mediumAttackMul,maxAttack*mediumAttackMul)
                    monsterHealth-=dmgCal
                    print ("you deal "+str(dmgCal)+" damage to "+str(monster))
                    break
            if attackStrength=="strong":
                if attackRoll>strongAttack:
                    print "you miss(happens to even the best of us)"
                    break
                else:
                    dmgCal=randint(minAttack*strongAttackMul,maxAttack*strongAttackMul)
                    monsterHealth-=dmgCal
                    print ("you deal "+str(dmgCal)+" damage to "+str(monster))
                    break
            else:
                print "that is not an attack"
        break
#print (str(level)+" level "+str(experience)+" experience")

def inventoryIndex():
    '''
    Shows which inventory items is currently being used, and which is in storage
    '''
    print "You currently have the following items in your possesion:"
    for item in heroInventory:
        print heroInventory(item)
    print "and you have the following on:"
    for item in inventoryUsed:
        print inventoryUsed(item)

def newItem(item):
    '''
    The process of adding an item to storage
    '''
    heroInventory+=item

def changeClothes():
    '''
    The act of putting clothes on or taking clothes off
    '''
    on_off=raw_input("What do you want to put on or off?")
    #Check wether the item is on or off and determine if the item should be put on or off depending on the outcome
    if on_off in inventoryUsed:
        print "taking off"+on_off
        inventoryUsed[on_off]=none
        heroInventory
    elif on_off in heroInventory:
        print "putting on"+on_off
        heroInventory.remove(on_off)
        inventoryUsed.append(on_off)
    else:
        print "The item does not exist in either your inventory or on you"
