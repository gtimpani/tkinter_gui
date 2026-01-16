import tkinter as tk

def f_print():
    text = "Hello, World!"
    text_output = tk.Label(w, text=text, fg="red", font=("Helvetica",16))
    text_output.grid(row=0, column=1)

w = tk.Tk()

w.geometry("600x600")
w.title("Hello, Tkinter user!")

#w.resizable(False, False)
#w.configure(background="white")

btn = tk.Button(text="OK",command=f_print)

btn.grid(row=0,column=0)

if __name__ == "__main__":
    w.mainloop()
