from tkinter import *

root = Tk()

#func

#Information_setting variables
bgcolor6 = 'lightskyblue2'
menuColor6 ='white'
logo6 = PhotoImage(file='..//logo//200by100.png')
icon6 = PhotoImage('..//logo//venus_icon.ico')
dashboard_icon6 = PhotoImage(file='..//btn_img//dashbd.png')
sub6 = PhotoImage(file='..//btn_img//sub.png')
setting6 = PhotoImage(file='..//btn_img//setting.png')
acct6 = PhotoImage(file='..//btn_img//money.png')
bar6 = PhotoImage(file='..//btn_img//drink.png')
gym6 = PhotoImage(file='..//btn_img//gym.png')
hr6 = PhotoImage(file='..//btn_img//hr.png')
bed6 = PhotoImage(file='..//btn_img//bed.png')
spoon6 = PhotoImage(file='..//btn_img//spoon.png')
store6 = PhotoImage(file='..//btn_img//store.png')
round6 = PhotoImage(file='..//btn_img//dot.png')
plus6 = PhotoImage(file='..//btn_img//plus.png')





root.geometry('1270x685')
root.minsize(width=1270, height=685)
root.title('Venus')
root.iconbitmap(icon6)
root.config(bg=bgcolor6)


#Menu
menuFrame6 = Frame(root, bg=menuColor6)
menuFrame6.grid(row=0, column=0)


logoLabel6 = Label(menuFrame6, image=logo6, bg=menuColor6, compound='left')
logoLabel6.grid(row=0, column=0, pady=20)

mainNavLabel6 = Label(menuFrame6, text='MAIN NAVIGATION', bg=menuColor6, fg='gray', font=('arial', 12, ), width=25)
mainNavLabel6.grid(row=1, column=0, sticky='w', pady=10)

dashboardButton6 = Button(menuFrame6, text='Dashboard', font=('arial', 15, ), bd=0,
                         image= dashboard_icon6,
                         compound='left',
                         bg=menuColor6,
                         pady=15,
                         padx=20,
                         activebackground=menuColor6)
dashboardButton6.grid(row=2, column=0, sticky='w')

#space
space6= Label(menuFrame6, bg=menuColor6).grid(row=3, column=0, pady=10)
#---------------------------

acctLabel6 = Label(menuFrame6, text='Account & Settings', bg=menuColor6, fg='gray', font=('arial', 12, ),
                  pady=15,
                  padx=20,
                  )
acctLabel6.grid(row=4, column=0, sticky='w')

subButton6 = Button(menuFrame6, text='Subscription History', font=('arial', 15, ), bd=0,
                         image= sub6,
                         compound='left',
                         bg=menuColor6,
                         pady=2,
                         padx=20,
                        activebackground=menuColor6,
                   )
subButton6.grid(row=5, column=0, sticky='w')

newsubButton6 = Button(menuFrame6, text='New Subscription', font=('arial', 15, ), bd=0,
                         image= plus6,
                         compound='left',
                         bg=menuColor6,
                         pady=15,
                        padx=20,
                        activebackground=menuColor6,)
newsubButton6.grid(row=6, column=0, sticky='w')



settingLabel6 = Label(menuFrame6, text='Settings', font=('arial', 12, ), bd=0,
                         compound='left',
                         bg=menuColor6,
                         pady=15,
                         padx=20,
                       fg='gray')
settingLabel6.grid(row=7, column=0, sticky='w')

propertyInformationButton6 = Button(menuFrame6, text='Property Information', font=('arial', 15, ), bd=0,
                         image= round6,
                         compound='left',
                         bg=menuColor6,
                         pady=2,
                         padx=20,
                        activebackground=menuColor6,
                   )
propertyInformationButton6.grid(row=8, column=0, sticky='w')

taxesButton6 = Button(menuFrame6, text='Taxes', font=('arial', 15, ), bd=0,
                         image= round6,
                         compound='left',
                         bg=menuColor6,
                         pady=2,
                         padx=20,
                        activebackground=menuColor6,
                   )
taxesButton6.grid(row=9, column=0, sticky='w')

logoutButton6 = Button(menuFrame6, text='Logout', font=('arial', 15, ), bd=0,
                         compound='left',
                         bg='red',
                        fg= 'white',
                         pady=5,
                         padx=15,
                        activebackground='red',
                   )
logoutButton6.grid(row=10, column=0, pady= 50)






#space
space6 = Label(menuFrame6, bg=menuColor6).grid(row=11, column=0, pady=200
                                   )
#---------------------------


#Item Dashboard MainFrame

itemsFrame6 = Frame(root, bg= bgcolor6)
itemsFrame6.grid(row=0, column=1, padx=20, pady=10, sticky='n')

taxLabel6= Label(itemsFrame6, text='Information', font=('Arial', 20, 'bold'), bg=bgcolor6 )
taxLabel6.grid(row=0, column=0, pady= 20, sticky='w')

#info
addressLabel6 = Label(itemsFrame6, text='Address',
                     font=('arial', 12,),
                     bg=bgcolor6)
addressLabel6.grid(row=1, column=0, sticky='w', pady=0, padx=5)

addressEntry6 = Entry(itemsFrame6, font=('arial', 20), bd=5)
addressEntry6.grid(row=2, column=0, pady=5, padx=5)


phoneLabel6 = Label(itemsFrame6, text='Phone',
                     font=('arial', 12,),
                     bg=bgcolor6)
phoneLabel6.grid(row=1, column=1, sticky='w', pady=0, padx=5)

phoneEntry6 = Entry(itemsFrame6, font=('arial', 20), bd=5)
phoneEntry6.grid(row=2, column=1, pady=5, padx=5)


websiteLabel6 = Label(itemsFrame6, text='Website',
                     font=('arial', 12,),
                     bg=bgcolor6)
websiteLabel6.grid(row=1, column=2, sticky='w', pady=0, padx=5)

websiteEntry6 = Entry(itemsFrame6, font=('arial', 20), bd=5)
websiteEntry6.grid(row=2, column=2, pady=5, padx=5)

savebutton6 = Button(itemsFrame6, text='Save',
                    font=('arial', 15),
                    bg='blue',
                    fg='white',
                    activebackground='blue')
savebutton6.grid(row=3, column=0, pady=20, padx=5, sticky='w')














root.mainloop()