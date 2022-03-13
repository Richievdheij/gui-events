import tkinter

background = "gray"
previous_button = None # Text of the previous pressed button
button_with_num = None # Button with the number that changes


window = tkinter.Tk() # Makes the window
window.title("Clicker") # Window title
window.configure(bg=background) # Window background color


# When the mouse hovers over the window
def mouse_enter(_):
    window.configure(bg="yellow")


# When the mouse leaves the window
def mouse_leave(_):
    window.configure(bg=background)


# When the users double clicks on the button with the number
def double_num_change(_):
    if previous_button == "up":
        button_with_num['text'] *= 3
    
    elif previous_button == "down":
        button_with_num['text'] //= 3


# Change the number when the user clicks on 'up' or 'down'
def change_num(text):
    global background
    global previous_button


    # Change the bindings to a string
    if text != "up" and text != "down" and type(text) is not int:
        text = text.keysym.lower()


    if text == "up" or text == "plus":
        button_with_num['text'] += 1
    else:
        button_with_num['text'] -= 1


    # Change the window background
    if button_with_num['text'] < 0:
        background = "red"


        window.configure(bg=background)
    elif button_with_num['text'] > 0:
        background = "green"

        window.configure(bg=background)
    else:
        background = "gray"

        window.configure(bg=background)


    previous_button = text


# Make the 3 buttons
def make_buttons():
    for button_num in range(1, 4):
        button = tkinter.Button(window, font=("arial", 10, 'bold'), width=20)

        button.pack(
            fill='both',
            expand=True,
            pady=20,
            padx=20
        )

        # If its the first button
        if button_num == 1: 
            # Button text
            text = "up"    
            button['text'] = text

            button['command'] = lambda para=text: change_num(para) # Function to change the number

        # If its the second button
        elif button_num == 2:
            # Use the button with the number for the global variable
            global button_with_num 
            button_with_num = button

            button['text'] = 0 # Button text
        
        # If its the third button
        else:
            # Button text
            text = "down"
            button['text'] = text

            button['command'] = lambda para=text: change_num(para) # Function to change the number

        button.pack() # Add the button to the window


def bindings():
    window.bind('<Enter>', mouse_enter)
    window.bind('<Leave>', mouse_leave)
    button_with_num.bind('<Double-Button-1>', double_num_change)
    window.bind("+", change_num)
    window.bind("<Up>", change_num)
    window.bind("-", change_num)
    window.bind("<Down>", change_num)
    window.bind("<space>", double_num_change)



# If the code starts
if __name__ == "__main__":
    make_buttons() # Makes the 3 buttons
    bindings() # Add the bindings

    window.mainloop() # Open the window