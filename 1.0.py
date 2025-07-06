import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(screen.get())))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry screen
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(row_frame, text=btn, font="Arial 18", height=2, width=5)
        button.pack(side=tk.LEFT, expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", click)

# Start the app
root.mainloop()

   
