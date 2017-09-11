from tkinter import *
from tkinter import filedialog
from datetime import *

class zapisek():
     
     def __init__(self, master):

          menu = Menu(master)
          master.config(menu = menu)

          file_menu = Menu(menu)
          menu.add_cascade(label = "Opravilo", menu= file_menu)

          file_menu.add_command(label="Odpri", command=self.odpri)
          file_menu.add_command(label="Shrani", command=self.shrani)
          file_menu.add_command(label="Izhod", command=master.destroy)

          Label(master, text = "Izračun Bazalnega Metabolizma",
                fg = "blue", font = "Helvetica 16 bold").grid(row = 0, columnspan=4)
          Label(master, text = "BMR je število kilokalorij, ki jih pokurimo med počitkom",
                font = "Helvetica 14 italic").grid(row = 1, columnspan = 4)

          self.spol = IntVar()
          Label(master, text= "Izberi splol:",
                font = "Helvetica 14 bold").grid(row=2, column=0)
          self.gumb_zenska = Radiobutton(master, variable = self.spol, value = 1, text = "ženska")
          self.gumb_zenska.grid(row=2, column=1)
          self.gumb_moski = Radiobutton(master, variable= self.spol, value= 2, text = "moški")
          self.gumb_moski.grid(row=2, column=2)

          Label(master, text = "teža (kg):").grid(row = 3, column = 0)
          Label(master, text = "višina(cm):").grid(row = 3, column = 1)
          Label(master, text = "starost (leta):").grid(row = 3, column = 2)

          gumb_izracunaj = Button(master, text = "Izračunaj moj BMR", command = self.izracun)
          gumb_izracunaj.grid(row = 6, rowspan = 2, column = 1)

          Label(master, text = "BMR").grid(row = 5, column = 0)

          self.listi = Listbox(master, selectmode = SINGLE)
          self.listi.grid(row = 8, rowspan = 2, column = 0, columnspan = 4, sticky = E+W+N+S)

          self.teza = DoubleVar(master, value = 0)
          self.visina = DoubleVar(master, value = 0)
          self.starost = DoubleVar(master, value = 0)
          self.bmr = DoubleVar(master, value = 0)

          polje_teza = Entry(master, textvariable = self.teza)
          polje_teza.grid(row = 4, column = 0)

          polje_visina = Entry(master, textvariable = self.visina)
          polje_visina.grid(row = 4, column = 1)

          polje_starost = Entry(master, textvariable = self.starost)
          polje_starost.grid(row = 4, column = 2)

          polje_bmr = Entry(master, textvariable = self.bmr)
          polje_bmr.grid(row = 6, column = 0)

          self.sez_vseh = []

          self.stanje = StringVar(value = "Manjkajoči podatki.")
          napis_stanja = Label(master, textvariable = self.stanje)
          napis_stanja.grid(row = 11, column = 0, columnspan = 3)
          Label(master, text = "Datoteko lahko shranite s pritiskom na meni Opravilo.").grid(row = 12, columnspan = 4)


     def izracun(self):

          if self.spol.get() == 2:
               self.bmr.set(66.47 + (13.7 * self.teza.get()) + (5* self.visina.get()) - (6.8 * self.starost.get()))
               self.stanje.set(self.bmr.get())
               self.listi.insert(0, str(date.today()) + ": " + str(self.bmr.get()) + " ... [" + str(self.teza.get()) + " kg; " + str(self.visina.get()) + " m; " + str(self.starost.get()) + " let]")
               self.sez_vseh += [str(date.today()) + ": " + str(self.bmr.get()) + " ... [" + str(self.teza.get()) + " kg; " + str(self.visina.get()) + " m; " + str(self.starost.get()) + " let]"]
          elif self.spol.get() == 1:
               self.bmr.set(655.1 + (9.6 * self.teza.get()) + (1.8*self.visina.get()) - (4.7 * self.starost.get()))
               self.stanje.set(self.bmr.get())
               self.listi.insert(0, str(date.today()) + ": " + str(self.bmr.get()) + "... [" + str(self.teza.get()) + " kg; " + str(self.visina.get()) + " m; " + str(self.starost.get()) + " let]")
               self.sez_vseh += [str(date.today()) + ": " + str(self.bmr.get()) + " ... [" + str(self.teza.get()) + " kg; " + str(self.visina.get()) + " m; " + str(self.starost.get()) + " let]"]

     def shrani(self):
        ime = filedialog.asksaveasfilename()
        if ime == "": 
            return
        with open(ime, "wt", encoding="utf8") as f:
            for i in self.sez_vseh:
                f.write(i + "\n")

     def odpri(self):
        ime = filedialog.askopenfilename()
        if ime == "": 
            return
        with open(ime, encoding="utf8") as f:
            for vrstica in f:
                self.listi.insert(0, vrstica)

          

root = Tk()
aplikacija = zapisek(root)
root.mainloop()
