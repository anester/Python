import sys
from tkinter import *
from tkinter.ttk import *
from datetime import date, datetime
from DbHelpers import DbMngr
from TkHelpers import SimpleListBox, ScrollableMessage, buildForm
import shelve
from DDObjects import *
from DDData import *

class EquipmentWindow(Toplevel):
    """Manage Equipment from this window"""
    
    def __init__(self, value, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        rightFrame = Frame(self)
        leftFrame = Frame(self)
        bottomFrame = Frame(rightFrame)

        nextBtn = Button(bottomFrame, text="N")
        prevBtn = Button(bottomFrame, text="P")
        updateBtn = Button(bottomFrame, text="U")
        addBtn = Button(bottomFrame, text="A")

        self.bind('<Control a>', lambda e: self.__addnew__())
        self.bind('<Control c>', lambda e: self.__clear__())

        equipmentLstBx = SimpleListBox(leftFrame)
        equipmentLstBx.listbox.configure(width=100, height=45)

        self.rightFrame = rightFrame
        self.leftFrame = leftFrame
        self.bottomFrame = bottomFrame

        self.armor = value
        self.label = Label(self, text="Equipment Window")
        self.label.pack(side=TOP, fill=X)

        self.nextBtn = nextBtn
        self.prevBtn = prevBtn
        self.updateBtn = updateBtn
        self.addBtn = addBtn

        self.formvalues, self.entries = buildForm(
            rightFrame, [
                ('Name',''),
                ('Set Type', 'Mythical', ('Mythical', 'Transcendent', 'Supreme', 'Ultimate')),
                ('Type', 'Leather', ('Leather','Mail','Chain','Plate','Pristine')),
                ('Kind', 'Helm', ('Helm','Chest','Gloves','Boots')),
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
                ('Resistance Poison',0)
            ], 
            labelWidth=30,
            fieldWidth=50
        )

        for k in self.formvalues.keys():
            val = self.formvalues[k]
            val.trace('w', lambda a,b,c,d=k: self.valueChanged(d))

        nextBtn.pack(side=RIGHT)
        prevBtn.pack(side=RIGHT)
        updateBtn.pack(side=RIGHT)
        addBtn.pack(side=RIGHT)

        self.setValues(value)
        bottomFrame.pack(side=TOP, expand=NO, fill=X)
        rightFrame.pack(side=RIGHT, expand=NO, fill=BOTH)
        leftFrame.pack(side=LEFT, expand=YES, fill=BOTH)

    def __focusfirst__(self):
        ''''''
        self.entries['Name'].focus()

    def __clear__(self):
        ''''''
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

    def __addnew__(self):
        """"""
        vals = list([(k, self.formvalues[k].get()) for k in self.formvalues])
        self.vals = vals
        self.event_generate('<<addnew>>')

        self.__focusfirst__()

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
            a = Armor()
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


class HeroWindow(Toplevel):
    """Manage Heros from this window"""

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('Hero Manager')

        self.label = Label(self, text="Hero Window")
        self.label.pack()

class DDApp(Tk):
    """Top Level app"""

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.db = DDDb('dundef.db')
        self.protocol('WM_DELETE_WINDOW', lambda: self.onExit())

        self.library = shelve.open('DDLibrary', 'c')
        self.equipment = []
        self.heroes = []

        if 'equipment' in self.library.keys():
            self.equipment = self.library['equipment']
        if 'heroes' in self.library.keys():
            self.heroes = self.library['heroes']

        #mf = Frame(self)
        heroBtn = Button(self, text="Hero Mngr", command=self.launchHeroMngr)
        equipmentBtn = Button(self, text="Equipment Mngr", command=self.launchEquipMngr)

        heroBtn.pack(side=LEFT)
        equipmentBtn.pack(side=LEFT)
        #mf.pack()

        self.heroBtn = heroBtn
        self.equipmentBtn = equipmentBtn
        #self.mainFrame = mf

    def onExit(self):
        """"""
        self.library['equipment'] = self.equipment
        self.library['heroes'] = self.heroes

        self.library.close()
        self.destroy()

    def launchEquipMngr(self):
        a = Armor()
        self.equipWin = EquipmentWindow(a)
        self.equipWin.bind('<<addnew>>', self.addequipment)

    def launchHeroMngr(self):
        self.win = HeroWindow(self)

    def addequipment(self, e, b=None):
        ''''''
        vals = dict(e.widget.vals)
        d = {}
        
        d['Stats_Value'] = vals['Cost']
        d['Stats_Level'] = vals['Level']
        d['Stats_Max_Level'] = vals['Max Level']

        d['Stats_Hero_Health'] = vals['Hero Health']
        d['Stats_Hero_Damage'] = vals['Hero Damage']
        d['Stats_Hero_Speed'] = vals['Hero Speed']
        d['Stats_Hero_Casting_Rate'] = vals['Hero Casting']

        d['Stats_Hero_Special1'] = vals['Hero Special 1']
        d['Stats_Hero_Special2'] = vals['Hero Special 2']

        d['Stats_Defense_Health'] = vals['Defense Health']
        d['Stats_Defense_Damage'] = vals['Defense Damage']
        d['Stats_Defense_Area_Effect'] = vals['Defense Area Effect']
        d['Stats_Defense_Attack_Rate'] = vals['Defense Attack Rate']

        d['Stats_Armor_Resist_Base'] = vals['Resistance Generic']
        d['Stats_Armor_Resist_Fire'] = vals['Resistance Fire']
        d['Stats_Armor_Resist_Electric'] = vals['Resistance Electric']
        d['Stats_Armor_Resist_Poison'] = vals['Resistance Poison']

        d['Armor_Name'] = vals['Name']
        d['Armor_Quality'] = vals['Set Type']
        d['Armor_Type'] = vals['Type']
        d['Armor_Kind'] = vals['Kind']

        self.db.insert_armor(d)
                

if __name__ == '__main__':
    app = DDApp()
    app.mainloop()
