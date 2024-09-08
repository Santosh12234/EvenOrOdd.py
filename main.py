from tkinter import *
root=Tk()
root.title("Even or Odd")
root.geometry("300x300")
root.resizable(False,False)
root.config(bg="pink")

entry_1 = Entry(root,width=19,borderwidth=0, font =("candra",19))
entry_1.place(x=15,y=150,height=40)

button_1 = Button(root,width=11,height=0,bg="red",fg="black",text="Exit",font=("bold",15),command=lambda:exit(0))
button_1.place(x=15,y=197)

def check_num():
    if int(entry_1.get()) % 2 == 0:
        text1 = "EVEN"
    elif int(entry_1.get()) % 2 != 0:
        text1 = "ODD"
    else:
        text1 = "Error"
    label_1.config(text=text1)

button_2 = Button(root,width=11,height=0,bg="light green",fg="black",text="Check",font=("bold",15),command=lambda:check_num())
button_2.place(x=152,y=197)

label_1 = Label(root,width = 15,height = 2,font=("candra",25),bg="pink")
label_1.place(x=5,y=60)


root.mainloop()