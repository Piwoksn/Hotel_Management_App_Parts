from tkinter import *

root = Tk()
#variables
bgcolor2 = 'cornsilk2'
logo2 = PhotoImage(file='logo//plain_logo.png')
icon2 = PhotoImage('logo//venus_icon.ico')

root.geometry('1270x685')
root.minsize(width=900, height=600)
root.title('Venus')
root.iconbitmap(icon2)
root.config(bg=bgcolor2)

logoLabel2 = Label(root, image=logo2, bg=bgcolor2)
logoLabel2.pack(pady=10, fill=X)

frame2 =Frame(root, bg='white')
frame2.pack()

labelFrame2 = LabelFrame(frame2, text='Create Your Account', bg='white', font=('arial', 10))
labelFrame2.pack(pady=10, padx=10)

hotelNameLabel2 =Label(labelFrame2, text='Hotel Name', font=('times new roman', 15),
                  bg='white')
hotelNameLabel2.grid(row=0, column=0, padx=10, sticky='w')

hotelNameEntry2 = Entry(labelFrame2, font=('arial', 20, 'bold'), bd=6,)
hotelNameEntry2.grid(row=1, column=0, pady=10, padx=10)


phoneNumberLabel2 =Label(labelFrame2, text='Phone Number', font=('times new roman', 15),
                  bg='white')
phoneNumberLabel2.grid(row=2, column=0, padx=10, sticky='w')

phoneNumberEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6,)
phoneNumberEntry2.grid(row=3, column=0, pady=10, padx=10)


passwordLabel2 =Label(labelFrame2, text='Password', font=('times new roman', 15),
                  bg='white')
passwordLabel2.grid(row=4, column=0, padx=10, sticky='w')

passwordEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6,)
passwordEntry2.grid(row=5, column=0, pady=10, padx=10)


contactPersonLabel2 =Label(labelFrame2, text='Contact Person', font=('times new roman', 15),
                  bg='white')
contactPersonLabel2.grid(row=0, column=1, padx=10, sticky='w')

contactPersonEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6,)
contactPersonEntry2.grid(row=1, column=1, pady=10, padx=10)


emailLabel2 =Label(labelFrame2, text='Email', font=('times new roman', 15),
                  bg='white')
emailLabel2.grid(row=2, column=1, padx=10, sticky='w')

emailEntry2 = Entry(labelFrame2, font=('arial', 20), bd=6,)
emailEntry2.grid(row=3, column=1, pady=10, padx=10)


noOfRoomsLabel2 =Label(labelFrame2, text='Number of Rooms', font=('times new roman', 15),
                  bg='white')
noOfRoomsLabel2.grid(row=4, column=1, padx=10, sticky='w')

noOfRoomsEntry2 = Entry(labelFrame2, font=('arial', 20, 'bold'), bd=6,)
noOfRoomsEntry2.grid(row=5, column=1, pady=10, padx=10)


createAccountButton2 = Button(labelFrame2, text='Create Account',
                             font=('times new roman', 15),
                             bg='blue',
                             fg='white',
                             width=50,
                             activebackground='blue')
createAccountButton2.grid(row=6, columnspan= 2, pady=10)



loginButton2 = Button(frame2, text = 'Have an account? Go to login!',
                        font=('times new roman', 15, 'bold'),
                        bd=0)
loginButton2.pack(fill=X)





root.mainloop()