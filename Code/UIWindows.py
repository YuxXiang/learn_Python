import tkinter

root=tkinter.Tk()
root.title('Good Day')
root.minsize(300,300)
label = tkinter.Label(root,text='今天天气不错!',fg='green')
label.place(width=300, height=300)

root.mainloop()