import sys
from tkinter import *
from tkinter.ttk import *

class SimpleListBox:
    """"""

    def __init__(self, frame):
        """"""
        self.root = frame
        self.listbox = Listbox(frame, relief=SUNKEN, exportselection=False)
        self.vbar = Scrollbar(frame, command=self.listbox.yview)
        self.hbar = Scrollbar(frame, orient=HORIZONTAL,  command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        self.vbar.pack(side=RIGHT, fill=Y)
        self.hbar.pack(side=BOTTOM, fill=X)
        self.listbox.pack(side=LEFT, expand=YES, fill=BOTH)

    def GetSelection(self):
        return self.listbox.get(ACTIVE)

    def Clear(self):
        self.listbox.delete(0, END)
        
    def Append(self, itm):
        self.listbox.insert(END, itm)
    
    def Fill(self, arr):
        self.Clear()
        for a in arr:
            self.Append(a)

    def Top(self):
        return self.listbox.get(0)

class ScrollableMessage:
    """"""

    def __init__(self, frame):
        """"""
        self.root = frame
        self.msg = Text(self.root, relief=SUNKEN, background='white')
        self.vbar = Scrollbar(frame, command=self.msg.yview)
        self.msg.config(yscrollcommand=self.vbar.set) #, xscrollcommand=self.hbar.set)

        self.vbar.pack(side=RIGHT, fill=Y)
        #self.hbar.pack(side=BOTTOM, fill=X)
        self.msg.pack(side=LEFT, expand=YES, fill=BOTH)

    def OverWrite(self, text):
        self.msg.delete('1.0', END)
        self.msg.insert('1.0', text)

    def Append(self, text):
        self.msg.insert(END, text)

    def Write(self, text):
        self.msg.insert('1.0', text)

    def Puts(self, text):
        self.msg.insert('1.0', text + "\n")

def buildForm(widget, fieldarr, labelWidth=15, fieldWidth=25):
    valueDict = {}
    entries = {}
    
    for tple in fieldarr:
        if len(tple) == 2:
            value = StringVar(value=tple[1])
            key = tple[0]
            valueDict[key] = value
        
            row = Frame(widget)
            label = Label(row, text=key, width=labelWidth)
            ent = Entry(row, text=value, width=fieldWidth)
            row.pack(side=TOP, fill=X, expand=NO)
            label.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=NO, fill=X)
            entries[key] = ent

        elif len(tple) == 3:
            value = StringVar(value=tple[1])
            key = tple[0]
            valueDict[key] = value
            
            row = Frame(widget)
            label = Label(row, text=key, width=labelWidth)
            ent = Combobox(row, textvariable=value, values=tple[2], width=fieldWidth, state = 'readonly')
            row.pack(side=TOP, fill=X, expand=NO)
            label.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=NO, fill=X)
            entries[key] = ent

        elif len(tple) == 1:
            key = tple[0]
            row = Frame(widget)
            label = Label(row, text=key)
            row.pack(side=TOP, fill=X)
            label.pack(side=TOP, fill=BOTH, expand=True)
            

    return (valueDict, entries)
