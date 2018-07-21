import tkinter as tk# Tkinter is Python's 2.* Gui-toolkit (tkinter for 3.*) 
#Tkinter-docu see http://effbot.org/tkinterbook/pack.htm
from Ringer import FamilyOrFriend, Deliverer


def pressed():
    print("clicked B! Deliverer")
    ringer = Deliverer()
        
        
class FullScreenApp(object):
    padding=3
    dimensions="{0}x{1}+0+0"

    def __init__(self, master, **kwargs):
        self.master=master
        width=master.winfo_screenwidth()-self.padding
        height=master.winfo_screenheight()-self.padding
        master.geometry(self.dimensions.format(width, height))

#         a = tk.Button(self.master, text="KLik A!", command=pressed)
#         a.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

        b = tk.Button(self.master, text="Duw B!", command= pressed)
        b.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    def pressed(self, AorB):
        if AorB == "A":
            print("clicked A! Family or Friend")
            ringer = FamilyOrFriend()
            print("End of clicked A! Family or Friend")
        elif AorB == "B":
            print("clicked B! Deliverer")
            ringer = Deliverer()
            
        

root=tk.Tk()
root.wm_attributes('-fullscreen','true')

app=FullScreenApp(root)

root.mainloop()
