from tkinter import *

root = Tk()

#func
def add5(event):
    if addtaxEntry5.get() != '':
        alltaxList5.insert(len(alltaxList5.get(0, END)), addtaxEntry5.get()+'  --  '+ratetaxEntry5.get()+'%')
        #alltaxList.config(height=alltaxList.size())

        addtaxEntry5.delete(0, END)
        ratetaxEntry5.delete(0, END)
    else:
        pass

def delete5(event):
    for index in reversed(alltaxList5.curselection()):
        alltaxList5.delete(index)
        #alltaxList.config(height=alltaxList.size())

#Binded Keys

root.bind("<Return>", add5)
root.bind("<Delete>", delete5)

#variables
bgcolor5 = 'lightskyblue2'
menuColor5 ='white'
logo5 = PhotoImage(file='..//logo//200by100.png')
icon5 = PhotoImage('..//logo//venus_icon.ico')
dashboard_icon5 = PhotoImage(file='..//btn_img//dashbd.png')
sub5 = PhotoImage(file='..//btn_img//sub.png')
setting5 = PhotoImage(file='..//btn_img//setting.png')
acct5 = PhotoImage(file='..//btn_img//money.png')
bar5 = PhotoImage(file='..//btn_img//drink.png')
gym5 = PhotoImage(file='..//btn_img//gym.png')
hr5 = PhotoImage(file='..//btn_img//hr.png')
bed5 = PhotoImage(file='..//btn_img//bed.png')
spoon5 = PhotoImage(file='..//btn_img//spoon.png')
store5 = PhotoImage(file='..//btn_img//store.png')
round5 = PhotoImage(file='..//btn_img//dot.png')
plus5 = PhotoImage(file='..//btn_img//plus.png')





root.geometry('1270x685')
root.minsize(width=1270, height=685)
root.title('Venus')
root.iconbitmap(icon5)
root.config(bg=bgcolor5)


#Menu
menuFrame5 = Frame(root, bg=menuColor5)
menuFrame5.grid(row=0, column=0)


logoLabel5 = Label(menuFrame5, image=logo5, bg=menuColor5, compound='left')
logoLabel5.grid(row=0, column=0, pady=20)

mainNavLabel5 = Label(menuFrame5, text='MAIN NAVIGATION', bg=menuColor5, fg='gray', font=('arial', 12, ), width=25)
mainNavLabel5.grid(row=1, column=0, sticky='w', pady=10)

dashboardButton5 = Button(menuFrame5, text='Dashboard', font=('arial', 15, ), bd=0,
                         image= dashboard_icon5,
                         compound='left',
                         bg=menuColor5,
                         pady=15,
                         padx=20,
                         activebackground=menuColor5)
dashboardButton5.grid(row=2, column=0, sticky='w')

#space
space5 = Label(menuFrame5, bg=menuColor5).grid(row=3, column=0, pady=10)
#---------------------------

acctLabel5 = Label(menuFrame5, text='Account & Settings', bg=menuColor5, fg='gray', font=('arial', 12, ),
                  pady=15,
                  padx=20,
                  )
acctLabel5.grid(row=4, column=0, sticky='w')

subButton5 = Button(menuFrame5, text='Subscription History', font=('arial', 15, ), bd=0,
                         image= sub5,
                         compound='left',
                         bg=menuColor5,
                         pady=2,
                         padx=20,
                        activebackground=menuColor5,
                   )
subButton5.grid(row=5, column=0, sticky='w')

newsubButton5 = Button(menuFrame5, text='New Subscription', font=('arial', 15, ), bd=0,
                         image= plus5,
                         compound='left',
                         bg=menuColor5,
                         pady=15,
                        padx=20,
                        activebackground=menuColor5,)
newsubButton5.grid(row=6, column=0, sticky='w')



settingLabel5 = Label(menuFrame5, text='Settings', font=('arial', 12, ), bd=0,
                         compound='left',
                         bg=menuColor5,
                         pady=15,
                         padx=20,
                       fg='gray')
settingLabel5.grid(row=7, column=0, sticky='w')

propertyInformationButton5 = Button(menuFrame5, text='Property Information', font=('arial', 15, ), bd=0,
                         image= round5,
                         compound='left',
                         bg=menuColor5,
                         pady=2,
                         padx=20,
                        activebackground=menuColor5,
                   )
propertyInformationButton5.grid(row=8, column=0, sticky='w')

taxesButton5 = Button(menuFrame5, text='Taxes', font=('arial', 15, ), bd=0,
                         image= round5,
                         compound='left',
                         bg=menuColor5,
                         pady=2,
                         padx=20,
                        activebackground=menuColor5,
                   )
taxesButton5.grid(row=9, column=0, sticky='w')

logoutButton5 = Button(menuFrame5, text='Logout', font=('arial', 15, ), bd=0,
                         compound='left',
                         bg='red',
                        fg= 'white',
                         pady=5,
                         padx=15,
                        activebackground='red',
                   )
logoutButton5.grid(row=10, column=0, pady= 50)






#space
space5= Label(menuFrame5, bg=menuColor5).grid(row=11, column=0, pady=200
                                   )
#---------------------------


#Item Dashboard MainFrame

itemsFrame5 = Frame(root, bg= bgcolor5)
itemsFrame5.grid(row=0, column=1, padx=20, pady=10, sticky='n')

taxLabel5= Label(itemsFrame5, text='Taxes', font=('Arial', 20, 'bold'), bg=bgcolor5 )
taxLabel5.grid(row=0, column=0, pady= 10, sticky='w')

#alltax
alltaxLabel5 = LabelFrame(itemsFrame5, text='All Taxes', font=('times new roman', 12), bg= bgcolor5, width=100)
alltaxLabel5.grid(row=1, column=0, padx=20)

scrollbar5 =Scrollbar(alltaxLabel5, orient=VERTICAL,
                     )
scrollbar5.pack(side=RIGHT, fill=Y, pady= 10)

alltaxList5 = Listbox(alltaxLabel5, font=('arial', 15),
                     width= 50,
                     height= 20,
                     selectmode=MULTIPLE,
                     yscrollcommand=scrollbar5.set)
alltaxList5.pack(pady= 10, side=LEFT)

scrollbar5.config(command=alltaxList5.yview)


#addtax
addtaxLabel5 = LabelFrame(itemsFrame5, text='Add Tax', font=('times new roman', 12), bg= bgcolor5)
addtaxLabel5.grid(row=1, column=1, sticky= 'n')

taxnameLabel5 = Label(addtaxLabel5, text='Tax Name',bg=bgcolor5, font=('times new roman', 15,))
taxnameLabel5.grid(row=0, column= 0, sticky='w', pady=5, padx=20)

addtaxEntry5 = Entry(addtaxLabel5, font=('arial', 15), bd=5)
addtaxEntry5.grid(row=1, column=0, padx=20)

ratenameLabel5 = Label(addtaxLabel5, text='Rate (%)',bg=bgcolor5, font=('times new roman', 15,))
ratenameLabel5.grid(row=2, column= 0, sticky='w', pady=5, padx=20)

ratetaxEntry5 = Entry(addtaxLabel5, font=('arial', 15), bd=5)
ratetaxEntry5.grid(row=3, column=0, padx=20)


addbutton5 = Button(addtaxLabel5, text= 'Add Tax', font=('arial', 15),
                   bg='blue',
                   fg='white',
                   activebackground='blue',
                   command= add5)
addbutton5.grid(row=4, column=0, pady=10, padx=20,)


deletebutton5 = Button(addtaxLabel5, text= 'Delete Tax', font=('arial', 15),
                   bg='orange',
                   fg='white',
                   activebackground='orange',
                   command= delete5)
deletebutton5.grid(row=5, column=0, padx=10, pady= 10 )














root.mainloop()