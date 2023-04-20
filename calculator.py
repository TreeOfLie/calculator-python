import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display for the calculator
        self.display = tk.Entry(master, width=30, font=("Helvetica", 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Create the buttons for the calculator
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]

        # Create a dictionary to store the button positions
        button_positions = {}
        button_positions["7"] = (1, 0)
        button_positions["8"] = (1, 1)
        button_positions["9"] = (1, 2)
        button_positions["/"] = (1, 3)
        button_positions["4"] = (2, 0)
        button_positions["5"] = (2, 1)
        button_positions["6"] = (2, 2)
        button_positions["*"] = (2, 3)
        button_positions["1"] = (3, 0)
        button_positions["2"] = (3, 1)
        button_positions["3"] = (3, 2)
        button_positions["-"] = (3, 3)
        button_positions["0"] = (4, 0)
        button_positions["."] = (4, 1)
        button_positions["C"] = (4, 2)
        button_positions["+"] = (4, 3)

        # Create the buttons using a loop
        for button_text in buttons:
            row, col = button_positions.get(button_text)
            button = tk.Button(master, text=button_text, width=5, height=2, font=("Helvetica", 16),
                               command=lambda text=button_text: self.add_to_display(text))
            button.grid(row=row, column=col)

    def add_to_display(self, text):
        # Clear the display if the "C" button is pressed
        if text == "C":
            self.display.delete(0, tk.END)
        # Evaluate the expression if the "=" button is pressed
        elif text == "=":
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        # Otherwise, add the button text to the display
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current_text + text)


# Create the main window and start the event loop
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
