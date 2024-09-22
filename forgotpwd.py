from tkinter import *

root = Tk()
#func

#variables
bgcolor4 = 'cornsilk2'
logo4 = PhotoImage(file='logo//plain_logo.png')
icon4 = PhotoImage('logo//venus_icon.ico')

root.geometry('1270x685')
root.minsize(width=900, height=600)
root.title('Venus')
root.iconbitmap(icon4)
root.config(bg=bgcolor4)

frame14 = Frame(root, bg=bgcolor4)
frame14.pack(fill=X)

iconLabel4 = Label(frame14,
              bg=bgcolor4,
              image= logo4)
iconLabel4.pack(pady=10)

loginframe4 = Frame(root,
                   bg= 'white')
loginframe4.pack(anchor='center')

loginLabel4 = LabelFrame(loginframe4, text='Forgot Password', font=('arial', 10),
                        bg= 'white',
                        )
loginLabel4.pack(fill=X, pady= 10, padx=10)

emailLabel4 =Label(loginLabel4, text='Email', font=('times new roman', 15),
                  bg='white')
emailLabel4.grid(row=0, column=0, padx=100, sticky='w')

emailEntry4 = Entry(loginLabel4, font=('arial', 20), bd=6, width= 25)
emailEntry4.grid(row=1, column=0, pady=10, padx=100)


loginButton4 = Button(loginLabel4, text='Request Password Reset',
                     font=('times new roman', 15),
                     bg='blue',
                     fg='white',
                     activebackground='blue')
loginButton4.grid(row=6, column=0, pady=10)


registerButton4 = Button(loginframe4, text = 'back to login',
                        font=('times new roman', 15, 'bold'),
                        bd=0,
                        )
registerButton4.pack(fill=X)



root.mainloop()