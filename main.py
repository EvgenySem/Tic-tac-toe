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
        global cur_player
        cur_player = players["one"][0] = 'X'
        players["two"][0] = '0'

        player_one_label['text'] = f'Player one "{players["one"][0]}": {players["one"][1]}'
        player_two_label['text'] = f'{players["two"][1]} :Player two "{players["two"][0]}"'
        self.dismiss()

    def chosen_0(self):
        global cur_player
        cur_player = players["one"][0] = '0'
        players["two"][0] = 'X'

        player_one_label['text'] = f'Player one "{players["one"][0]}": {players["one"][1]}'
        player_two_label['text'] = f'{players["two"][1]} :Player two "{players["two"][0]}"'
        self.dismiss()

    def dismiss(self):
        self.grab_release()
        self.destroy()


def select():
    window.attributes("-topmost", False)
    select_window = Window()


def reset():
    global cur_player, players, turns
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
            buttons[row][col]['state'] = ['normal']

    cur_player = players['one'][0]
    turns = 0

    if players['one'][1] == 3 or players['two'][1] == 3:
        players['one'][1] = players['two'][1] = 0
        select_button['state'] = ['normal']

    player_one_label['text'] = f'Player one "{players["one"][0]}": {players["one"][1]}'
    player_two_label['text'] = f'{players["two"][1]} :Player two "{players["two"][0]}"'


# Game stuff
cur_player = 'X'
players = {'one': ['X', 0], 'two': ['0', 0]}
buttons = []
turns = 0

# Window
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
player_one_label = tk.Label(label_frame, text=f'Player one "{players["one"][0]}": {players["one"][1]}', font=("Arial", 18))
player_two_label = tk.Label(label_frame, text=f'{players["two"][1]} :Player two "{players["two"][0]}"', font=("Arial", 18))
player_one_label.place(relwidth=0.5, rely=0.2)
player_two_label.place(relwidth=0.5, relx=0.5, rely=0.2)

# Menu buttons
select_button = tk.Button(button_frame, text='Select: X / 0', command=select)
select_button.place(relwidth=0.5, relheight=0.7)
reset_button = tk.Button(button_frame, text='Reset', command=reset)
reset_button.place(relwidth=0.5, relheight=0.7, relx=0.5)


def check_win():
    for i in range(3):
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True

    return False


def on_click(row, col):
    global cur_player, turns

    if buttons[row][col]['text'] != '':
        return

    buttons[row][col]['text'] = cur_player
    select_button['state'] = ['disabled']

    turns += 1

    if check_win():
        # window.attributes("-topmost", False)
        messagebox.showinfo('Congratulation!',f'Player {cur_player} won the round!', parent=window)
        # window.lift()

        if cur_player == players['one'][0]:
            players['one'][1] += 1
        else:
            players['two'][1] += 1

        player_one_label['text'] = f'Player one "{players["one"][0]}": {players["one"][1]}'
        player_two_label['text'] = f'{players["two"][1]} :Player two "{players["two"][0]}"'

        if players['one'][1] == 3 or players['two'][1] == 3:
            messagebox.showinfo('Congratulation!', f'Player {cur_player} the winner!', parent=window)

        for row in range(3):
            for col in range(3):
                if buttons[row][col]['text'] == '':
                    buttons[row][col]['state'] = ['disabled']
    else:
        if turns == 9:
            messagebox.showinfo('Tie!', f'Tie!', parent=window)

    cur_player = '0' if cur_player == 'X' else 'X'


for c in range(3):
    game_frame.columnconfigure(index=c, weight=1)
for r in range(3):
    game_frame.rowconfigure(index=r, weight=1)

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(game_frame, text='', font=('Arial', 30), width=10, height=10, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j) #padx=, pady=, ipadx=, ipady= , sticky='NSEW'
        row.append(btn)
    buttons.append(row)






window.mainloop()