import tkinter as tk
from tkinter import font
from tkinter.messagebox import askyesno, askquestion

pressButtons = ["Press W", "Press A", "Press S", "Press D", "Spacebar", "One-Click", "Double-Click", "Triple-Click"] # Buttons the user needs to press
points = 0

class App(tk.Tk):
    def __init__(window):
        super().__init__()

        window.configure(background='gray') # Window background color
        window.title('Simple FPS Trainer V1') # Window title
        window.geometry('750x500') # Window size

        # Launch button
        launch_button = tk.Button( # Makes the button
            window,
            text='LAUNCH GAME',
            font=("arial",20,'bold'),
            command=window.confirm # Makes the command pop-up window button
        )

        launch_button.pack(
            fill='both',
            expand=True,
            padx=20,
            pady=20, 
        )

        # Launch label
        launch_label = tk.Label( # Makes the label
            window,
            background='gray',
            text='WELCOME TO SIMPLE FPS TRAINER V.1', 
            font=("arial",20,'bold')
        )

        launch_label.pack(
            padx=0,
            pady=0
        )

    def confirm(window):
        answer = askyesno(title='Confirmation start game',
                          message="Press 'Yes' to start the game.")
        if answer:
            window.destroy()
            startgame()

def startgame():
    window = tk.Tk() # Makes the window
    window.title("Simple FPS Trainer V1") # Window title
    window.geometry("750x500") # Window size

    startButton1 = tk.Label( # Makes the label
        window, 
        font=("arial",15,))

    startButton1.configure( # Adjust the label
        text="Remaining time:") 

    startButton1.grid(
        fill='both',
        pady=0,
        padx=0
    )

    startButton2 = tk.Label( # Makes the label
        window, 
        font=("arial",15,))

    startButton2.configure(
        text="Points: {points}") 

    startButton2.grid(
        fill='both',
        pady=0,
        padx=0
    )

    startButton3 = tk.Button( # Makes the button
        window, 
        font=("arial",15,))

    startButton3.configure(
        text="Start game")

    startButton3.grid(
        expand=True,
        pady=0,
        padx=0,
    )

def game():
    return










if __name__ == "__main__":
    app = App()
    app.mainloop()
