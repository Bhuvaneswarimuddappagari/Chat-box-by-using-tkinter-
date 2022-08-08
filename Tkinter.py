from tkinter import*
root=Tk()
def send():
    send=e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot=>hi")
    elif (e.get()=="hi"):
        txt.insert(END,"\n"+"       hello")
    elif(e.get()=="how are you?"):
        txt.insert(END,"\n"+"       fine and you")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"       okay")
    elif(e.get()=="what are you doing?"):
        txt.insert(END,"\n"+"       i am studing")
    elif(e.get()=="how is your studies?"):
        txt.insert(END,"\n"+"       good and you")
    elif(e.get()=="my studies also good"):
        txt.insert(END,"\n"+"       okey bye")
    else:
        txt.insert(END,"\n"+"       nice to hear")
    e.delete(0,END)
txt=Text(root,height=30,width=65)
txt.grid(row=0,column=0)
e=Entry(root,width=100)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)

root.title("CHATBOX")
root.configure(bg="pink")


root.mainloop()