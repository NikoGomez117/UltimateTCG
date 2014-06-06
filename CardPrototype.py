import random
from cmath import *

#F(COST) = Stat
def TroopsFunct(points):
    return points*1.25 + .5
def MovesFunct(points):
    return points*3
def DrawFunct(points):
    return points*.5 + .25
def DiscardFunct(points):
    return points*.5
def FaithFunct(points):
    return points*1.25 + 1.5
def SabatogeFunct(points):
    return points*1.25 + 1.5

#F(Stat) = Cost
def TroopsInvFunct(points):
    return (points - .5)*.8
def MovesInvFunct(points):
    return points*.333
def DrawInvFunct(points):
    return (points - .25)*2
def DiscardInvFunct(points):
    return points*2
def FaithInvFunct(points):
    return (points - 1.5)*.8
def SabatogeInvFunct(points):
    return (points - .5)*.8
def HybridInvFunct(points):
    return points

while True:
    #List of Edict Ideologies (Like Colors in magic)
    #Anarchy (Moves,Draw) Atheism (Draw,Sabatoge) Socialism (Sabatoge,Troops) Totalitarianism (Troops,Discard) Religion (Discard,Faith) Capitalism (Faith,Moves)
    ideologies = ["Anarchy","Atheism","Socialism","Totalitarianism","Religion","Capitalism","(Moves,Draw)","","","","",""]
    
    #List of the base stats of a card
    stats = ["Troops","Moves","Draw","Discard","Faith","Sabatoge"]

    #List of Basic Modifier
    baseMODS = ["Secret","Continuous","Sabatoge","Colorless"]
    baseMODS_table = {"Secret" : (lambda x : x + 2),"Continuous" : (lambda x : x * 2.5),"Sabatoge" : (lambda x : x + 3),"Colorless" : (lambda x : x + (int(x/3))*.5 + 1)}
    
    #List of X modifiers to a Card
    XMODS = ["Territories","Troops","Cards in Hand","Affinity to Color","Troops on Zone","Edicts Played"]
    XMODS_table = {"Territories" : 3,"Troops" : 6,"Cards in Hand" : 3,"Affinity to Color" : 2,"Troops on Zone" : 2,"Edicts Played" : 3}

    #List of Pain Modifiers (Color => Ideology(Socialist (Troops,Decay), Capitalist (Power,Moves), Libralism(Draw,Moves), Conservatism(), Religous(), Atheist()))
    painMODS = ["Troops","Discard","Hybrid"]
    
    #Select the Cost of the Card
    partOneCost = random.randrange(1,5)
    partTwoCost = random.randrange(0,5)
    
    #Select The Type of Card Desired
    rndType = random.randrange(0,3)
    #rndType = 0

    #Select the Base Stat
    rndStat = random.randrange(0,6)
    stat = stats[rndStat]

    text = ""

    if rndType == 0:
        text += "Cost: "+str(partOneCost+partTwoCost)
        text += " "+stat+": "+str(eval(stat+"Funct("+str(partOneCost)+")"))

        #Select anouther Stat
        rndStat = random.randrange(0,6)
        stat = stats[rndStat]
        
        text += " "+stat+": "+str(eval(stat+"Funct("+str(partTwoCost)+")"))

    elif rndType == 1:
        mod = XMODS[random.randrange(0,len(XMODS))]
        
        text += "Cost: "+str(eval(stat+"InvFunct("+str(XMODS_table[mod])+")"))
        text += " "+stat+": X where X = "+mod
        
    elif rndType == 2:
        mod = baseMODS[random.randrange(0,len(baseMODS))]

        text += "Cost: "+str(baseMODS_table[mod](partOneCost))
        text += " "+stat+": "+str(eval(stat+"Funct("+str(partOneCost)+")"))
        text += " -"+mod
        
    elif rndType == 3:
        mod = painMODS
    
    print(text)
    print("NextCard?")
    x = raw_input()
    
