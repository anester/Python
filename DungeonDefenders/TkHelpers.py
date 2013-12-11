import sys
import tkinter as TK

class SimpleListBox:
    """"""

    def __init__(self, frame):
        """"""
        self.root = frame
        self.listbox = TK.Listbox(frame, relief=TK.SUNKEN, exportselection=False)
        self.vbar = TK.Scrollbar(frame, command=self.listbox.yview)
        self.hbar = TK.Scrollbar(frame, orient=TK.HORIZONTAL,  command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)

        self.vbar.pack(side=TK.RIGHT, fill=TK.Y)
        self.hbar.pack(side=TK.BOTTOM, fill=TK.X)
        self.listbox.pack(side=TK.LEFT, expand=TK.YES, fill=TK.BOTH)

    def GetSelection(self):
        return self.listbox.get(TK.ACTIVE)

    def Clear(self):
        self.listbox.delete(0, TK.END)
        
    def Append(self, itm):
        self.listbox.insert(TK.END, itm)
    
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
        self.msg = TK.Text(self.root, relief=TK.SUNKEN, background='white')
        self.vbar = TK.Scrollbar(frame, command=self.msg.yview)
        self.msg.config(yscrollcommand=self.vbar.set) #, xscrollcommand=self.hbar.set)

        self.vbar.pack(side=TK.RIGHT, fill=TK.Y)
        #self.hbar.pack(side=TK.BOTTOM, fill=TK.X)
        self.msg.pack(side=TK.LEFT, expand=TK.YES, fill=TK.BOTH)

    def OverWrite(self, text):
        self.msg.delete('1.0', TK.END)
        self.msg.insert('1.0', text)

    def Append(self, text):
        self.msg.insert(TK.END, text)

    def Write(self, text):
        self.msg.insert('1.0', text)

    def Puts(self, text):
        self.msg.insert('1.0', text + "\n")

def buildForm(widget, fieldarr, labelWidth=15):
    valueDict = {}
    entries = {}
    
    for tple in fieldarr:
        if len(tple) == 2:
            value = TK.StringVar(value=tple[1])
            key = tple[0]
            valueDict[key] = value
        
            row = TK.Frame(widget)
            label = TK.Label(row, text=key, width=labelWidth)
            ent = TK.Entry(row, text=value)
            row.pack(side=TK.TOP, fill=TK.X)
            label.pack(side=TK.LEFT)
            ent.pack(side=TK.RIGHT, expand=TK.YES, fill=TK.X)
            entries[key] = ent
        elif len(tple) == 1:
            key = tple[0]
            row = TK.Frame(widget)
            label = TK.Label(row, text=key)
            row.pack(side=TK.TOP, fill=TK.X)
            label.pack(side=TK.TOP, fill=TK.BOTH, expand=True)
            

    return valueDict
