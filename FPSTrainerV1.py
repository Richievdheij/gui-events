import tkinter
from unittest import skip

background = "gray"
window = tkinter.Tk() # Makes the window
window.title("Clicker") # Window title
window.configure(bg=background) # Window background color
window.geometry("750x500")

pressButtons = ["Press W", "Press A", "Press S", "Press D", "Spacebar", "One-Click", "Double-Click", "Triple-Click"] # pressButtons the user needs to press


def make_startButton():
    startButton = tkinter.Button(window, font=("arial",70, 'bold'), width=20)
    startButton.configure(text="START GAME")

    startButton.pack(
        fill='both',
        expand=True,
        pady=20,
        padx=20
    )

pressButton = 0
if pressButton == "Press W":
    pressButtonPress = "<w>"
elif pressButton == "Press A":
    pressButtonPress = "<a>"
elif pressButton == "Press S":
    pressButtonPress = "<s>"
elif pressButton == "Press D":
    pressButtonPress = "<d>"
elif pressButton == "Spacebar":
    pressButtonPress = "<space>"
elif pressButton == "One-Click":
    pressButtonPress = "<Button-1>"
elif pressButton == "Double-Click":
    pressButtonPress = "<Double-Button-1>"
elif pressButton == "Triple-Click":
    pressButtonPress = "<Triple-Button-1>"














# If the code starts
if __name__ == "__main__":
    make_startButton()

    window.mainloop() # Open the window