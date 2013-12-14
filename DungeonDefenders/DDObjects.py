
class Entity:
    """"""
    def __init__(self):
        """"""
        value = None
        
        self.value = value
        self.level = value
        self.maxlevel = value
        self.herohealth = value
        self.herodammage = value
        self.herospeed = value
        self.herocastingrate = value
        self.herospecial1 = value
        self.herospecial2 = value
        self.defensehealth = value
        self.defensedamage = value
        self.defenseareaeffect = value
        self.defenseattackrate = value
        self.armorresistbase = value
        self.armorresistfire = value
        self.armorresistelectric = value
        self.armorresistpoison = value

    def __setattr__(self, name, value):
        if name == 'Stats_Value':
            self.value = value
        elif name == 'Stats_Level':
            self.level = value
        elif name == 'Stats_Max_Level':
            self.maxlevel = value
        elif name == 'Stats_Hero_Health':
            self.herohealth = value
        elif name == 'Stats_Hero_Damage':
            self.herodammage = value
        elif name == 'Stats_Hero_Speed':
            self.herospeed = value
        elif name == 'Stats_Hero_Casting_Rate':
            self.herocastingrate = value
        elif name == 'Stats_Hero_Special1':
            self.herospecial1 = value
        elif name == 'Stats_Hero_Special2':
            self.herospecial2 = value
        elif name == 'Stats_Defense_Health':
            self.defensehealth = value
        elif name == 'Stats_Defense_Damage':
            self.defensedamage = value
        elif name == 'Stats_Defense_Area_Effect':
            self.defenseareaeffect = value
        elif name == 'Stats_Defense_Attack_Rate':
            self.defenseattackrate = value
        elif name == 'Stats_Armor_Resist_Base':
            self.armorresistbase = value
        elif name == 'Stats_Armor_Resist_Fire':
            self.armorresistfire = value
        elif name == 'Stats_Armor_Resist_Electric':
            self.armorresistelectric = value
        elif name == 'Stats_Armor_Resist_Poison':
            self.armorresistpoison = value
        else:
            object.__setattr__(self, name, value)

class Armor(Entity):
    """"""

    def __init__(self):
        """"""
        Entity.__init__(self)
        self.statsid = None
        self.armorname = None
        self.armorquality = None
        self.armortype = None
        self.armorkind = None

    def __setattr__(self, name, value):
        if name == 'Stats_ID':
            self.statsid = value
        elif name == 'Armor_Name':
            self.armorname = value
        elif name == 'Armor_Quality':
            self.armorquality = value
        elif name == 'Armor_Type':
            self.armortype = value
        elif name == 'Armor_Kind':
            self.armorkind = value
        else:
            object.__setattr__(self, name, value)

class Hero(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.statsid = None
        self.heroname = None
        self.armorsetid = None
        
    def __setattr__(self, name, value):
        if name == 'Stats_ID':
            self.statsid = value
        elif name == 'Hero_Name':
            self.heroname = value
        elif name == 'armorsetid':
            self.armorsetid = value
        else:
            object.__setattr__(self, name, value)

if __name__ == '__main__':
    print(__name__)
