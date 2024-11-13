from tkinter import *

root = Tk()
root.title('Inches to Centimeters')
root.geometry('400x300')

lbl = Label(root, text="Convert Inches to Centimeters", fg="white", bg="#80db1f", height=2, width=300)
lbl.pack(pady=10)

inch_lbl = Label(root, text="Enter in Inches", bg="#80db1f")
inch_lbl.pack()

inch_entry = Entry(root, width=20)
inch_entry.pack(pady=5)

def convert():
    text_box.delete(1.0, END)
    
    inches = float(inch_entry.get())
    
    centimeters = inches * 2.54
    
    text_box.insert(END, "Here is your result!!:\n")
    
    text_box.insert(END, f"{inches} inches = {centimeters} centimeters\n")

text_box = Text(root, height=4, width=40, wrap=WORD)
text_box.pack(pady=10)

btn = Button(root, text="Convert!", command=convert, height=1, bg="#80db1f", fg='white')
btn.pack(pady=5)

root.mainloop()