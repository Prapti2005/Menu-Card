from tkinter import *
def add_order():

    Menu = {"Sandwich":60,"Tea":15,"Pasta":100,"Cake":250}
    Total = 0

    Sandwich_qty = int(sd_ent.get() or 0)
    Tea_qty = int(tea_ent.get() or 0)
    Pasta_qty = int(pasta_ent.get() or 0)
    Cake_qty = int(cake_ent.get() or 0)

    Total += Sandwich_qty * Menu["Sandwich"]
    Total += Tea_qty * Menu["Tea"]
    Total += Pasta_qty * Menu["Pasta"]
    Total += Cake_qty * Menu["Cake"]

    dis_lbl.config(text=f"Total:Rs:{Total}")

window = Tk()
window.geometry("600x600")
window.title("Food Menu")

title_lbl = Label(window, text="Order Tour Food",bd=12,relief=GROOVE,bg="teal",fg="white",font=("calibri",30,"bold"))
title_lbl.pack(fill=X)

frame = LabelFrame(window,bd=10,text="Food Details",font=("calibri",25,"bold"),relief="groove",fg="white",bg="teal")
frame.pack(pady=20)

sd_lal = Label(frame,text="Sandwich",bg="teal",fg="white",font=("calibri",20,"bold"))
sd_lal.grid(row=0,column=0,padx=20,pady=5)
sd_ent=Entry(frame,width=15,font="Arial 15",bd=15,relief="sunken")
sd_ent.grid(row=0,column=1,padx=35,pady=5)

tea_lal = Label(frame,text="Tea",bg="teal",fg="white",font=("calibri",20,"bold"))
tea_lal.grid(row=1,column=0,padx=20,pady=5)
tea_ent=Entry(frame,width=15,font="Arial 15",bd=15,relief="sunken")
tea_ent.grid(row=1,column=1,padx=35,pady=5)

pasta_lal = Label(frame,text="Pasta",bg="teal",fg="white",font=("calibri",20,"bold"))
pasta_lal.grid(row=2,column=0,padx=20,pady=5)
pasta_ent=Entry(frame,width=15,font="Arial 15",bd=15,relief="sunken")
pasta_ent.grid(row=2,column=1,padx=35,pady=5)

cake_lal = Label(frame,text="Cake",bg="teal",fg="white",font=("calibri",20,"bold"))
cake_lal.grid(row=3,column=0,padx=20,pady=5)
cake_ent=Entry(frame,width=15,font="Arial 15",bd=15,relief="sunken")
cake_ent.grid(row=3,column=1,padx=35,pady=5)

submit_but = Button(window,text="Submit",width=15,bd=15,fg="white",bg="red",activebackground="red",command= add_order)
submit_but.pack(side="bottom",pady=20)

dis_lbl= Label(window,bg="teal",fg="white",font="Arial 15")
dis_lbl.pack(padx=35,pady=5)

window.mainloop()



    
    