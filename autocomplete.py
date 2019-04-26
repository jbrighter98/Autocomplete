from Trie import *
from tkinter import *
from tkinter import ttk

class AutoComplete:
    def __init__(self, master):
        # this method creates the GUI with all the components
        # this initializes the trie and implements he library of words
        
        self.trie = TrieStructure()
        create_trie(self.trie)
        self.master = master
        master.title("Autocomplete")

        self.label = ttk.Label(master, text="Enter characters")
        self.label.pack()

        v = StringVar()
        self.e = ttk.Entry(master, textvariable = v)
        self.e.bind("<Key>", self.key)
        self.e.pack()

        self.listbox = Listbox(master)
        self.listbox.pack()

        words = list(self.trie.all_words(self.e.get()))
        self.listbox.delete(0,END)
        for item in words:
            self.listbox.insert(END, item)

    def key(self, event):
        # this method reads each key stroke
        # this delay was added because there was an issue of
        #   the listbox not updating
        self.master.after(10, self.update)

    def update(self):
        # this method updtes the listbox
        words = list(self.trie.all_words(self.e.get()))
        self.listbox.delete(0,END)
        for item in words:
            self.listbox.insert(END, item)

root = Tk()
root.geometry("300x250")
gui = AutoComplete(root)
root.mainloop()








