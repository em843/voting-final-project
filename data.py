"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang

Data section containing all of the keys


"""



class User():
    def __init__(self, name, reg_num):
        self.name = name
        self.reg_num = reg_num
        self.val_num = 0
        self.priv = 0
        self.pub = 0
    def __str__(self):
        return self.name


grimp = User("Grimp", 9781532)
gumpy = User("Gumpy", 1692423)
grimble = User("Grimble", 2583532)
gronk = User("Gronk", 3474423)
grilbo = User("Grilbo", 4565312)
garth = User("Garth", 5656423)
gert = User("Gert", 6747512)
gyre = User("Gyre", 7656423)






# Voters and their public keys
public_key = {
    "Grimp": 20589956143748776736423548596554255238200715774836381779016556915581272048674357522077319748461570390825705038439082279911876325241392261508451015477206259066392391994398597533141595049057975743527202236676445852276626475201413935229711598651198462746097525275834211965215274772754005794941042068520433642800804555576398371115042994864489965686818357474903109631893898398559749718253380377837448268546428276073964299883752295978675004154802107498957817478782100557610351930541222877903146697538531022398351433415988134778600780012012846609387848240273501125340077855848637618115615914075775942284860293542635426785731,
    "Gumpy": 432473298
}

# Validation 
validation_number = {}


#registers
# name, public keys, validation numbers

# validation numbers generated on sign-in


priv_key = {
    "Grimp": 5153065606752940110637030136879669414482935443167467750117179097751865726877287823322889337538591597880940751643771114868159901835746461895747647219999955158261257205733033198629605291585652656443431513282070660375684383573456083824980234693027712375627380099397786664837586963436092635436821520787832104142912943437419101728125466802751136676826219894772741012182199152979229732059757478785641552511389295057269157395677320938384173587903628514913710244382814510925877227795509825209639206359583128631306068040392882622138841827582025475313987706388801771660222095777323941772098770124843020997608393552436609046017,
    "Gumpy": 2322343
}

aes_keys = {}
