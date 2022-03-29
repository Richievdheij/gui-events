from curses import window
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion

pressButtons = ["Press W", "Press A", "Press S", "Press D", "Spacebar", "One-Click", "Double-Click", "Triple-Click"] # Buttons the user needs to press



class App(tk.Tk):
    def __init__(window):
        super().__init__()

        window.title('Simple FPS Trainer V1')
        window.geometry('750x500')

        # Launch button
        launch_button = ttk.Button(
            window, 
            text='LAUNCH GAME', 
            command=window.confirm
        )
        launch_button.pack(
            expand=True,
            padx=20,
            pady=20
        )

        # Launch label
        launch_label = ttk.Label(
            window, 
            text='WELCOME TO SIMPLE FPS TRAINER V.1', 
            font=(("arial",30, 'bold'))
        )
        launch_label.pack(
            fill='both',
            padx=0,
            pady=0
        )
    def confirm(window):
        answer = askyesno(title='Confirmation start game',
                          message="Press 'Yes' to start the game. Timer will start after confirmation")
        if answer:
            window.destroy()
            game()

def game():
    window = tk.Tk() # Makes the window
    window.title("Simple FPS Trainer V1") # Window title
    window.geometry("750x500")

    startButton1 = tk.Label(
        window, 
        font=("arial",15,))

    startButton1.configure(
        text="Remaining time:")

    startButton1.pack(
        fill='both',
        pady=0,
        padx=20
    )

    startButton2 = tk.Label(
        window, 
        font=("arial",15,))

    startButton2.configure(
        text="Start game")

    startButton2.pack(
        pady=0,
        padx=0
    )

def timer():
    return





if __name__ == "__main__":
    app = App()
    app.mainloop()
