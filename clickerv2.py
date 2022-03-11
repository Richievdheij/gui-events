import tkinter

background = "gray"
window = tkinter.Tk()
window.title("Clicker")
window.geometry("450x300")
window.configure(bg="gray") 


# When the mouse hovers over the window
def mouse_enter(_):
    window.configure(bg="yellow")


# When the mouse leaves the window
def mouse_leave(_):
    window.configure(bg=background)

global button_with_num # Button with the number that changes

# Change the number when the user clicks on 'up' or 'down'
def change_num(text):
    button_with_num['text'] += 1 if text == "up" else -1 # Change number

    # Change the window background
    if button_with_num['text'] < 0:
        window.configure(bg="red")
    elif button_with_num['text'] > 0:
        window.configure(bg="green")
    else:
        window.configure(bg="gray")


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
            
            text = "up"    
            button['text'] = text

            button['command'] = lambda para=text: change_num(para) # Function to change the number

        # If its the second button
        elif button_num == 2:
            window.configure(bg="yellow")
            # Use the button with the number for the global variable
            global button_with_num 
            button_with_num = button

            button['text'] = 0
        
        # If its the third button
        else:
            
            text = "down"
            button['text'] = text

            button['command'] = lambda para=text: change_num(para) # Function to change the number


        button.pack() # Add the button to the window

def bindings():
    window.bind('<Enter>', mouse_enter)
    window.bind('<Leave>', mouse_leave)

# If the code starts
if __name__ == "__main__":
    make_buttons() # Makes the 3 buttons
    bindings()
    
    window.mainloop()