import tkinter as tk


class InputBox ():
    """Creates a simple input box with a Validate button and the possibility to press Enter to validate and close the box
    To get the value of the input box, call the variable 'userinput'
    
    Example :
    
    input = InputBox().userinput
    
    """
    
    def __init__(self, texte_principal=None, texte_secondaire=None,): #donner une valeur aux titres rends les aruments optionnels
        super().__init__()
        self.root = tk.Tk()
        self.root.title(texte_principal)
        self.label = tk.Label(self.root, text=texte_secondaire, font="Roboto")
        self.entry = tk.Entry(self.root, width=50, justify="center", borderwidth=6, font="Roboto")
        self.entry.focus() #permet de focus le curseur sur le champ d'input
        self.entry.bind('<Return>', lambda x: self.get_input_enter(self.entry.get()))
        self.btn = tk.Button(self.root, text="Valider", padx=20, command= self.get_input_button)
        self.userinput = ""

        self.label.pack() #affiche le texte secondaire
        self.entry.pack() #affiche le champ d'input
        self.btn.pack() #affiche le bouton

        self.root.mainloop()


    def get_input_button(self):
        self.userinput = self.entry.get()
        self.root.destroy()

    def get_input_enter(self, value):
        self.userinput = value
        self.root.destroy()

