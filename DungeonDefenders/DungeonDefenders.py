import sys
#from tkinter import *
import tkinter as TK
from datetime import date, datetime
from DbHelpers import DbMngr
from TkHelpers import SimpleListBox, ScrollableMessage, buildForm
import shelve
from DDObjects import *

class EquipmentWindow(TK.Toplevel):
    """Manage Equipment from this window"""
    
    def __init__(self, value, *args, **kwargs):
        TK.Toplevel.__init__(self, *args, **kwargs)

        rightFrame = TK.Frame(self)
        leftFrame = TK.Frame(self)
        equipmentLstBx = SimpleListBox(leftFrame)

        self.rightFrame = rightFrame
        self.leftFrame = leftFrame

        self.armor = value
        self.label = TK.Label(self, text="Equipment Window")
        self.label.pack(side=TK.TOP, fill=TK.X);

        self.formvalues = buildForm(rightFrame, [('Name',''),
                                           ('Set Type', ''),
                                           ('Type', ''),
                                           ('Kind', ''),
                                           ('Level', 1),
                                           ('Max Level', 99),
                                           ('Cost', 0),
                                           ('Hero Health',0),
                                           ('Hero Damage',0),
                                           ('Hero Speed',0),
                                           ('Hero Casting',0),
                                           ('Hero Special 1',0),
                                           ('Hero Special 2',0),
                                           ('Defense Health',0),
                                           ('Defense Damage',0),
                                           ('Defense Area Effect',0),
                                           ('Defense Attack Rate',0),
                                           ('Resistance Generic',0),
                                           ('Resistance Fire',0),
                                           ('Resistance Electric',0),
                                           ('Resistance Poison',0)], 
                                    labelWidth=30)
        for k in self.formvalues.keys():
            val = self.formvalues[k]
            val.trace('w', lambda a,b,c,d=k: self.valueChanged(d))

        self.setValues(value)

        rightFrame.pack(side=TK.RIGHT, expand=True, fill=TK.BOTH)
        leftFrame.pack(side=TK.LEFT, expand=True, fill=TK.BOTH)

    def valueChanged(self, name):
        """"""

        if name == 'Name':
            self.armor.name = self.formvalues[name].get()
        elif name == 'Set Type':
            self.armor.armorsettype = self.formvalues[name].get()
        elif name == 'Type':
            self.armor.armortype = self.formvalues[name].get()
        elif name == 'Kind':
            self.armor.armorkind = self.formvalues[name].get()
        elif name == 'Level':
            self.armor.armorlevel = self.formvalues[name].get()
        elif name == 'Max Level':
            self.armor.armormaxlevel = self.formvalues[name].get()
        elif name == 'Cost':
            self.armor.cost = self.formvalues[name].get()
        elif name == 'Hero Health':
            self.armor.herohealth = self.formvalues[name].get()
        elif name == 'Hero Damage':
            self.armor.herodamage = self.formvalues[name].get()
        elif name == 'Hero Speed':
            self.armor.herospeed = self.formvalues[name].get()
        elif name == 'Hero Casting':
            self.armor.herocastingrate = self.formvalues[name].get()
        elif name == 'Hero Special 1':
            self.armor.herospecial1 = self.formvalues[name].get()
        elif name == 'Hero Special 2':
            self.armor.herospecial2 = self.formvalues[name].get()
        elif name == 'Defense Health':
            self.armor.defensehealth = self.formvalues[name].get()
        elif name == 'Defense Damage':
            self.armor.defensedamage = self.formvalues[name].get()
        elif name == 'Defense Area Effect':
            self.armor.defenseareaeffect = self.formvalues[name].get()
        elif name == 'Defense Attack Rate':
            self.armor.defenseattackrate = self.formvalues[name].get()
        elif name == 'Resistance Generic':
            self.armor.resistgeneric = self.formvalues[name].get()
        elif name == 'Resistance Fire':
            self.armor.resistfire = self.formvalues[name].get()
        elif name == 'Resistance Electric':
            self.armor.resisteletric = self.formvalues[name].get()
        elif name == 'Resistance Poison':
            self.armor.resistpoison = self.formvalues[name].get()

    def setValues(self, values):
        if values is dict:
            for k in values.keys():
                self.formvalues[k].set(values[k])

        elif values is Armor:
            a = Armor('',0)
            self.setValues({'Name':a.name,
                            'Set Type':a.armorsettype,
                            'Type':a.armortype,
                            'Kind':a.armorkind,
                            'Level':a.armorlevel,
                            'Max Level':a.armormaxlevel,
                            'Cost':a.cost,
                            'Hero Health':a.herohealth,
                            'Hero Damage':a.herodamage,
                            'Hero Speed':a.herospeed,
                            'Hero Casting':a.herocastingrate,
                            'Hero Special 1':a.herospecial1,
                            'Hero Special 2':a.herospecial2,
                            'Defense Health':a.defensehealth,
                            'Defense Damage':a.defensedamage,
                            'Defense Area Effect':a.defenseareaeffect,
                            'Defense Attack Rate':a.defenseattackrate,
                            'Resistance Generic':a.resistgeneric,
                            'Resistance Fire':a.resistfire,
                            'Resistance Electric':a.resisteletric,
                            'Resistance Poison':a.resistpoison
                            })


class HeroWindow(TK.Toplevel):
    """Manage Heros from this window"""

    def __init__(self, *args, **kwargs):
        TK.Toplevel.__init__(self, *args, **kwargs)
        self.title('Hero Manager')

        self.label = TK.Label(self, text="Hero Window")
        self.label.pack();

class DDApp(TK.Tk):
    """Top Level app"""

    def __init__(self, *args, **kwargs):
        TK.Tk.__init__(self, *args, **kwargs)

        self.protocol('WM_DELETE_WINDOW', lambda: self.onExit())

        self.library = shelve.open('DDLibrary', 'c')
        self.equipment = []
        self.heroes = []

        if 'equipment' in self.library.keys():
            self.equipment = self.library['equipment']
        if 'heroes' in self.library.keys():
            self.heroes = self.library['heroes']

        #mf = TK.Frame(self)
        heroBtn = TK.Button(self, text="Hero Mngr", command=self.launchHeroMngr)
        equipmentBtn = TK.Button(self, text="Equipment Mngr", command=self.launchEquipMngr)

        heroBtn.pack(side=TK.LEFT)
        equipmentBtn.pack(side=TK.LEFT)
        #mf.pack()

        self.heroBtn= heroBtn
        self.equipmentBtn = equipmentBtn
        #self.mainFrame = mf

    def onExit(self):
        """"""
        self.library['equipment'] = self.equipment
        self.library['heroes'] = self.heroes

        self.library.close()

    def launchEquipMngr(self):
        a = Armor('',0)
        self.equipWin = EquipmentWindow(a)

    def launchHeroMngr(self):
        self.win = HeroWindow(self)

if __name__ == '__main__':
    app = DDApp()
    app.mainloop()