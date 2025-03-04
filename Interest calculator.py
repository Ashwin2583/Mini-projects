from tkinter import *

root = Tk()
root.geometry("500x450")
root.resizable(False,False)

#calculate function
def compute():
     int_p =int(p.get())
     float_r = float(r.get())
     float_t = float(t.get())
     interest = int_p*(float_r/100)*float_t
     print(interest)
     global result_msg
     result_msg = Label(root,text=interest,font=("Arial",18,"bold"),fg="purple")
     result_msg.place(x=240,y=350)
     
          

#reset function
def reset():
     global result_msg
     p.delete(0,END)
     r.delete(0,END)
     t.delete(0,END)
     result_msg.destroy()
     
          
     
#main heading
Header = Label(root,text="SIMPLE INTEREST CALCULATOR",font=("Arial",21,"bold"),fg="white",
               relief="solid",borderwidth=4,bg="black")
Header.place(x=20,y=10)
#data widgets
principle = Label(root,text="Enter principle amount:",font=("Arial",18,"bold"))
p = Entry(root,width=20)
r = Entry(root,width=20)
t = Entry(root,width=20)
rate = Label(root,text="Enter interest rate(%):",font=("Arial",18,"bold"))
time = Label(root,text="Enter time in years:",font=("Arial",18,"bold"))

principle.place(x=0,y=100)
p.place(x=274,y=106)
rate.place(x=0,y=150)
r.place(x=256,y=156)
time.place(x=0,y=200)
t.place(x=225,y=206)

#buttons
calc=Button(root,text="CALCULATE",width=10,height=2,bg="white",fg="green",command=compute)
calc.place(x=110,y=275)
res=Button(root,text="RESET",width=10,height=2,bg="white",fg="red",command=reset)
res.place(x=250,y=275)

#result
result = Label(root,text="Total interest:",font=("Arial",18,"bold"),fg="purple")
result.place(x=65,y=350)


root.mainloop()
