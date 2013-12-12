
class Entity:
    """"""

    def __init__(self, name):
        """"""
        self.name = name

        self.herohealth = 0
        self.herodamage = 0
        self.herospeed = 0
        self.herocastingrate = 0

        self.herospecial1 = 0
        self.herospecial2 = 0

        self.defensehealth = 0
        self.defensedamage = 0
        self.defenseareaeffect = 0
        self.defenseattackrate = 0

        self.resistgeneric = 0
        self.resistfire = 0
        self.resisteletric = 0
        self.resistpoison = 0

class Item(Entity):
    """"""

    def __init__(self, name, cost):
        """"""
        Entity.__init__(self, name)
        self.cost = cost


class Armor(Item):
    """"""

    def __init__(self, name, cost):
        """"""
        Item.__init__(self, name, cost)

        self.armortype = ''
        self.armorsettype = ''
        self.armorkind = ''
        self.armorlevel = 0
        self.armormaxlevel = 0

class Weapon(Item):
    """"""

    def __init__(self, name, cost):
        """"""
        Item.__init__(self, name, cost)

class ItemCollection:
    """"""

if __name__ == '__main__':
    print('test')