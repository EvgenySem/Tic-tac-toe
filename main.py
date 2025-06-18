import tkinter as tk
from tkinter import messagebox

class Window(tk.Toplevel):
    def __init__(self):

        super().__init__(window)
        self.attributes("-topmost", True)
        self.title('Selection')
        self.geometry(f'300x200+{width}+{height}')
        self.protocol("WM_DELETE_WINDOW", self.dismiss)  # перехватываем нажатие на крестик

        self.label = tk.Label(self, text='Choose your symbol!', font=("Arial", 18))
        self.button_X = tk.Button(self, text='X', font=('Arial', 40), command= self.chosen_x)
        self.button_0 = tk.Button(self, text='0', font=('Arial', 40), command= self.chosen_0)

        self.label.place(relwidth=1, relheight=0.25, rely=0.1)
        self.button_X.place(relwidth=0.28, relheight=0.4, relx=0.15, rely=0.45)
        self.button_0.place(relwidth=0.28, relheight=0.4, relx=0.57, rely=0.45)

        self.grab_set()

    def chosen_x(self):
        self.dismiss()

    def chosen_0(self):
        self.dismiss()

    def dismiss(self):
        self.grab_release()
        self.destroy()


def select():
    window.attributes("-topmost", False)
    select_window = Window()


window = tk.Tk()
window.attributes("-topmost", True)
window.title('Tic-tac-toe')
width = window.winfo_screenwidth() // 2 - 150
height = window.winfo_screenheight() // 2 - 200
window.geometry(f'300x400+{width}+{height}')

# Frames
game_frame = tk.Frame(window)
game_frame.place(relwidth=1, relheight=0.75)

bottom_frame = tk.Frame(window)
bottom_frame.place(relwidth=1, relheight=0.25, rely=0.75)

label_frame = tk.Frame(bottom_frame)
label_frame.place(relwidth=1, relheight=0.5)

button_frame = tk.Frame(bottom_frame)
button_frame.place(relwidth=1, relheight=0.5, rely=0.5)

# Labels
player_one_label = tk.Label(label_frame, text='Player one "X": 0', font=("Arial", 18))
player_two_label = tk.Label(label_frame, text='0 :Player two "0"', font=("Arial", 18))
player_one_label.place(relwidth=0.5, rely=0.2)
player_two_label.place(relwidth=0.5, relx=0.5, rely=0.2)

# Menu buttons
select_button = tk.Button(button_frame, text='Select: X / 0', command= select)
select_button.place(relwidth=0.5, relheight=0.7)
reset_button = tk.Button(button_frame, text='Reset')
reset_button.place(relwidth=0.5, relheight=0.7, relx=0.5)
# X and 0 buttons on the msbx

# Game stuff
cur_player = 'X'
buttons = []


def on_click(row, col):
    pass


for c in range(3):
    game_frame.columnconfigure(index=c, weight=1)
for r in range(3):
    game_frame.rowconfigure(index=r, weight=1)

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(game_frame, text='', font=('Arial', 20), command=on_click(i, j)) #command=lambda r=i, c=j: on_click(r, c)
        btn.grid(row=i, column=j, sticky='NSEW') #padx=, pady=, ipadx=, ipady=
        row.append(btn)
    buttons.append(row)






window.mainloop()