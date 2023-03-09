import tkinter as tk

# Create a new window
window = tk.Tk()
window.title("Results")

# Create a Text widget
text = tk.Text(window)

# Open the results file and read its contents
with open("C:\\Users\\natan\\Desktop\\python_tests\\results.txt", "r") as file:
    contents = file.read()

# Insert the contents of the file into the Text widget
text.insert(tk.END, contents)

# Pack the Text widget into the window and show it
text.pack()
window.mainloop()
