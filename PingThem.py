import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Rooti:
    root = tk.Tk()
    y_or_n = [None]

    def __init__(self):
        self.root.title("PingThem")
        self.root.geometry('300x420+50+50')
        self.root.resizable(False, False)
        self.root.attributes('-topmost', 1)
        self.root.configure(bg='light gray')
        self.root.grid_columnconfigure((0, 1, 2), weight=1)
        self.num_of_ip = simpledialog.askinteger("Input","How many ip addresses? (Min = 1, Max = 17)                                        ")  # We do what we must not what looks logical
        self.alertuser = messagebox.showinfo("Important","Please enter values one after the other")


    def PingController(self, ip):
        # a function that handle's the user ip unput
        try:
            subprocess.check_output("ping " + ip + " -n 1 -w 500", shell=True) #the -n 1 and -w 500 aruguments substantially improve the program speed
            if self.y_or_n[0] is None:
                self.y_or_n[0] = "Ping!"
            else:
                self.y_or_n.append("Ping!")
        except subprocess.CalledProcessError:
            if self.y_or_n[0] is None:
                self.y_or_n[0] = "No Ping!"
            else:
                self.y_or_n.append("No Ping!")

    def ShowError(self):
        #Shows an error if user goes above 17 or below 0 (the window size can't handle more then 17)
        while self.num_of_ip > 17:
            messagebox.showerror("Error!", "Must be under 18")
            exit()
        else:
            0

    def Make_Entry(self):
        #For loop to append the entry value to the entry dict, and place then on the UI
        self.entry_dict = {}
        for i in range(0, self.num_of_ip):
            self.entry_dict.update({i:tk.Entry(self.root)})
            self.entry_dict[i].grid(row=i + 2, column=1)
        return self.entry_dict

    def pingsetter(self):
        #For loop to append the StringVar value to the pingset dict
        self.pingset = {}
        for i in range(0,self.num_of_ip):
            self.pingset.update({i: tk.StringVar()})
        return self.pingset

    def ExecutePing(self):
        #On buttom press this function runs, it executes the PingController function and sets the StringVar to Ping or No ping (based on the PingController function)
      try:
        for i in range(0,self.num_of_ip):
            if len(self.entry_dict[i].get()) != 0:
                self.PingController(str(self.entry_dict[i].get()))
                self.pingset[i].set(self.y_or_n[i])
            else:
                self.pingset[i].set((""))
        del self.y_or_n[:]
        self.y_or_n.append(None)
      except Exception:
         messagebox.showerror("User Error", "Please enter value one after the other")

    def PingButtom(self):
        #The actual ping buttom
        for i in range(self.num_of_ip):
            j = i
        buttom = tk.Button(self.root, text="Ping", command=lambda: self.ExecutePing())
        buttom.grid(row=j + 3, column=1)

    def MakeLabel(self, txt):
        #If statements to a label is make when asked to
        if txt == "PingThem":
            header = tk.Label(self.root, text=txt, bg='light gray')
            header.grid(row=0, column=1)
        elif txt == "Ping":
            for i in range(0, self.num_of_ip):
                pinglabel = tk.Label(self.root, textvariable=self.pingset[i], bg='light gray')
                pinglabel.grid(row=i + 2, column=2)
        elif txt == "Enter IP Address":
            for i in range(0, self.num_of_ip):
                iplabel = tk.Label(self.root, text=txt, bg='light gray')
                iplabel.grid(row=i + 2, column=0)

    def MainLoop(self):
        self.root.mainloop()



window1 = Rooti()
window1.ShowError()
window1.MakeLabel("PingThem")
window1.MakeLabel("Enter IP Address")
window1.Make_Entry()
window1.PingButtom()
window1.pingsetter()
window1.MakeLabel("Ping")

window1.MainLoop()