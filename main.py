from tkinter import *
import datetime
from tkinter import ttk
import sqlite3
import random

screen = Tk()
screen.title("Hotel Management System")
screen.geometry("800x600")
screen.resizable("False","False")

#Declaring the database
#Creating the Database
# Database needs to be created once then add values after commenting this out
#creating a database
connect = sqlite3.connect('hoteldata.db')

#creating a cursor for keeping track on rows or column
cursor = connect.cursor()

#Creating the rows and columns
#cursor.execute('''CREATE TABLE hoteldata(
#    Name text,
#    ph_no integer,
#   pan_no integer,
#    Address text,
#    No_of_days integer,
#    type text,
#    amount integer,
#    roomNo integer

#)''')

#Setting the title Background
titlbg = Label(screen,bg="DarkViolet",height=6)
titlbg.grid(row=0,column=0,ipadx=700)

#setting the title 
title2 = Label(screen,text="2.5 Star Hotel",foreground="white",bg="DarkViolet",font=("Segoe Script",19),height=2)
title2.grid(row=0,column=0,padx=(40,630))

#setting the main pages


#Check In stage
def checkin():
    ch_in = Toplevel()
    ch_in.geometry("700x600")
    ch_in.title("Check_In")
    ch_in.resizable('False','False')
    ch_in.configure(bg="light goldenrod yellow")

    #setting the label name 
    name = Label(ch_in,text="Name",font=("Courier",15),bg="light goldenrod yellow")
    name.grid(row=1,column=0,pady=(48,0),padx=(110,0))
    ph_no = Label(ch_in,text="Phone Number",font=("Courier",15),bg="light goldenrod yellow")
    ph_no.grid(row=2,column=0,pady=(25,0),padx=(110,0))
    pan_no = Label(ch_in,text="Pan no",font=("Courier",15),bg="light goldenrod yellow")
    pan_no.grid(row=3,column=0,pady=(25,0),padx=(110,0))
    Address = Label(ch_in,text="Address",font=("Courier",15),bg="light goldenrod yellow")
    Address.grid(row=4,column=0,pady=(25,0),padx=(110,0))
    nod = Label(ch_in,text="No of days",font=("Courier",15),bg="light goldenrod yellow")
    nod.grid(row=5,column=0,pady=(25,0),padx=(110,0))
    roomtype = Label(ch_in,text="Room Type",font=("Courier",15),bg="light goldenrod yellow")
    roomtype.grid(row=6,column=0,pady=(25,0),padx=(110,0))

    #setting up the entrys 
    Nameentry = Entry(ch_in,width=40)
    Nameentry.grid(row=1,column=1,pady=(40,0),padx=(120,0))

    phentry = Entry(ch_in,width=40)
    phentry.grid(row=2,column=1,pady=(20,0),padx=(120,0))
    
    panEntry = Entry(ch_in,width=40)
    panEntry.grid(row=3,column=1,pady=(20,0),padx=(120,0))

    AddEntry = Entry(ch_in,width=40)
    AddEntry.grid(row=4,column=1,pady=(20,0),padx=(120,0))
    
    nodEntry = Entry(ch_in,width=40)
    nodEntry.grid(row=5,column=1,pady=(20,0),padx=(120,0))
    #combobox creation
    val = StringVar()
    val.set("Select a type")
    typeentry = ttk.Combobox(ch_in,width=38,textvariable=val)
    typeentry['values'] =("General(Non-Ac)","General(Ac)","Deluxe","Ultra Deluxe(Pool)")
    typeentry.grid(row=6,column=1,pady=(25,0),padx=(120,0))

    def save():
        global type
        global amount 
        type = val.get()
        amount = 0
        if type == "General(Non-Ac)":
            amount+=500
        elif type == "General(Ac)":
            amount+=800
        elif type == "Deluxe":
            amount+=1200
        elif type =="Ultra Deluxe(Pool)":
            amount+=2000
        
        roomno = random.randint(0,20)

        #creating a database
        connect = sqlite3.connect('hoteldata.db')

        #creating a cursor for keeping track on rows or column
        cursor = connect.cursor()

        cursor.execute("INSERT INTO hoteldata VALUES(:Name,:phno,:panno,:address,:nod,:type,:amount,:roomno)",
        {
            "Name":Nameentry.get(),
            "phno":phentry.get(),
            "panno":panEntry.get(),
            "address":AddEntry.get(),
            "nod":nodEntry.get(),
            "type":val.get(),
            "amount":amount,
            "roomno":roomno
        })
        
        # Data types in python sql are text,blob(images),integer,realno,null
        #commiting the changes done 
        connect.commit()
        #closing the database
        connect.close()

        #showing the amount and details
        #Setting the bottom
        d1 = Label(ch_in,text="Bookings done!",font=("Comic Sans Ms",15,"italic"))
        d1.grid(row=8,column=0,columnspan=2,padx=(60,0),pady=(30,0))

        
        d2 = Label(ch_in,text="Your Room Number is "+str(roomno),font=("Comic Sans Ms",15,"italic"))
        d2.grid(row=9,column=0,columnspan=2,padx=(60,0),pady=(14,0))

        d3 = Label(ch_in,text="The amount per day is: "+str(amount),font=("Comic Sans Ms",15,"italic"))
        d3.grid(row=10,column=0,columnspan=2,padx=(60,0),pady=(10,0))


        #Deleting the entry boxes
        Nameentry.delete(0,END)
        phentry.delete(0,END)
        panEntry.delete(0,END)
        AddEntry.delete(0,END)
        nodEntry.delete(0,END)
        val.set("Select a type")

    Check = Button(ch_in,text="Check-In",bg="cyan",font=("Segoe Script",12),command=save)
    Check.grid(row=7,column=0,columnspan=2,ipadx=30,ipady=10,pady=(30,0),padx=(70,0))

Checkin = Button(screen,text="Check-In",bg="BlanchedAlmond",font=("Segoe Script",15),command=checkin)
Checkin.grid(row=1,column=0,ipadx=52,ipady=10,padx=(40,630),pady=(30,10))

# Setting up the check Out stage
def check_out():
    ch_out = Toplevel()
    ch_out.geometry("500x400")
    ch_out.title("Check_Out")
    ch_out.resizable('False','False')
    ch_out.configure(bg="light goldenrod yellow")

    #setting the label name 
    name = Label(ch_out,text="Name",font=("Courier",15),bg="light goldenrod yellow")
    name.grid(row=1,column=0,pady=(50,20),padx=(70,10))
     
    room_no = Label(ch_out,text="Room No",font=("Courier",15),bg="light goldenrod yellow")
    room_no.grid(row=2,column=0,padx=(70,10))

    #Setting the labels
    Name_entry = Entry(ch_out,width=40)
    Name_entry.grid(row=1,column=1,pady=(50,20),padx=(40,10))

    room_entry = Entry(ch_out,width=40)
    room_entry.grid(row=2,column=1,padx=(40,10))

    def check():
        if Name_entry.get() =="" or room_entry.get() =="":
            L4 = Label(ch_out,text="Please fill the details before checking out!",font=("Comic Sans Ms",15,"italic"),bg="light goldenrod yellow")
            L4.grid(row=4,column=0,columnspan=3,padx=(60,0))
        elif Name_entry.get() != "" and room_entry.get() != "":
            #creating a database
            connect = sqlite3.connect('hoteldata.db')

            #creating a cursor for keeping track on rows or column
            cursor = connect.cursor()

            #Execute
            cursor.execute("SELECT * from hoteldata WHERE roomno="+room_entry.get())
            values = cursor.fetchall()
            for value in values:
                l1 = Label(ch_out,text="Thank You for staying with us!!",font=("Comic Sans Ms",13,"italic"),bg="light goldenrod yellow")
                l1.grid(row=5,column=0,columnspan=3,padx=(60,0))
                l2 = Label(ch_out,text="You have stayed for "+str(value[4])+" days",font=("Comic Sans Ms",13,"italic"),bg="light goldenrod yellow")
                l2.grid(row=6,column=0,columnspan=3,padx=(60,0))
                #Total amount = tamt
                tamt = value[4]*value[6]
                l2 = Label(ch_out,text="The total amount You need to pay is "+str(tamt),font=("Comic Sans Ms",13,"italic"),bg="light goldenrod yellow")
                l2.grid(row=7,column=0,columnspan=3,padx=(60,0))

            cursor.execute("DELETE FROM hoteldata WHERE roomno="+room_entry.get())


            #commiting the changes done 
            connect.commit()
            #closing the database
            connect.close()

            




    chout = Button(ch_out,text="Check_Out",command=check,bg="cyan",font=("Segoe Script",12))
    chout.grid(row=3,column=0,columnspan=3,ipadx=30,ipady=10,pady=(40,0),padx=(60,0))

    
Checkout = Button(screen,text="Check-Out",bg="BlanchedAlmond",font=("Segoe Script",15),command=check_out)
Checkout.grid(row=2,column=0,ipadx=47,ipady=10,padx=(40,630),pady=(30,10))

#Setting up the Guest list stage
def showGl():
    g_list = Toplevel()
    g_list.geometry("1000x500")
    g_list.title("Check_Out")
    g_list.resizable('False','False')
    g_list.configure(bg="light goldenrod yellow")

    #Setting the title Background
    titlbg = Label(g_list,bg="DarkViolet",height=4,width=150)
    titlbg.grid(row=0,column=0)

    #setting the title 
    title2 = Label(g_list,text="2.5 Star Hotel",foreground="white",bg="DarkViolet",font=("Segoe Script",15))
    title2.grid(row=0,column=0)

    tree = ttk.Treeview(g_list,selectmode="browse",height=25)
    tree.grid(row=1,column=0,padx=(0,50))
    style = ttk.Style(g_list)
    style.theme_use('clam')
    style.configure("Treeview",fieldbackground="light goldenrod yellow",foreground="black")

    tree["columns"] = ("1","2","3","4","5","6","7","8","9")
    tree["show"] = "headings"


    tree.column("1",anchor="center",width=60)
    tree.heading("1", text="Sno")

    tree.column("2",anchor="center",width=110)
    tree.heading("2",text="Name")

    tree.column("3",anchor="center",width=73)
    tree.heading("3",text="Phone No")

    tree.column("4",anchor="center",width=60)
    tree.heading("4",text="Pan No")
    
    tree.column("5",anchor="center",width=110)
    tree.heading("5",text="Address")
    
    tree.column("6",anchor="center",width=165)
    tree.heading("6",text="No of days")

    tree.column("7",anchor="center",width=150)
    tree.heading("7",text="Room Type")
    
    tree.column("8",anchor="center",width=110)
    tree.heading("8",text="amount")
    
    tree.column("9",anchor="center",width=110)
    tree.heading("9",text="Room_no")

    #creating a database
    connect = sqlite3.connect('hoteldata.db')

    #creating a cursor for keeping track on rows or column
    cursor = connect.cursor()

    #Execute
    cursor.execute("SELECT oid,* FROM hoteldata")
    records = cursor.fetchall()

    for row in records:
        tree.insert("",'end',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

    #commiting the changes done 
    connect.commit()
    #closing the database
    connect.close()








Gl = Button(screen,text="Show Guest List",bg="BlanchedAlmond",font=("Segoe Script",15),command=showGl)
Gl.grid(row=3,column=0,ipadx=22,ipady=10,padx=(40,630),pady=(30,10))

def exit():
    screen.destroy()



exit = Button(screen,text="Exit",bg="BlanchedAlmond",font=("Segoe Script",15),command=exit)
exit.grid(row=4,column=0,ipadx=40,ipady=10,padx=(40,630),pady=(30,10))

#commiting the changes done 
connect.commit()
#closing the database
connect.close()

screen.mainloop()