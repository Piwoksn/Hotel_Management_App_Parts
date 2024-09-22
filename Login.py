from tkinter import *

root = Tk()
#func

#variables
bgcolor1 = 'cornsilk2'
logo1 = PhotoImage(file='logo//plain_logo.png')
icon1 = PhotoImage('logo//venus_icon.ico')

root.geometry('1270x685')
root.minsize(width=900, height=600)
root.title('Venus')
root.iconbitmap(icon1)
root.config(bg=bgcolor1)

frame1 = Frame(root, bg=bgcolor1)
frame1.pack(fill=X)

iconLabel1 = Label(frame1,
              bg=bgcolor1,
              image= logo1)
iconLabel1.pack(pady=10)

loginframe1 = Frame(root,
                   bg= 'white')
loginframe1.pack(anchor='center')

loginLabel1 = LabelFrame(loginframe1, text='Login', font=('arial', 10),
                        bg= 'white',
                        )
loginLabel1.pack(fill=X, pady= 10, padx=10)

emailLabel1 =Label(loginLabel1, text='Email', font=('times new roman', 15),
                  bg='white')
emailLabel1.grid(row=0, column=0, padx=100, sticky='w')

emailEntry1 = Entry(loginLabel1, font=('arial', 20), bd=6, width= 25)
emailEntry1.grid(row=1, column=0, pady=10, padx=100)


passwordLabel1 =Label(loginLabel1, text='Password', font=('times new roman', 15),
                  bg='white')
passwordLabel1.grid(row=2, column=0,padx=100, sticky='w')

passwordEntry1 = Entry(loginLabel1, font=('arial', 20), bd=6, width= 25)
passwordEntry1.grid(row=3, column=0,pady=10, padx=100)


check1 = Checkbutton(loginLabel1, text='Remember Password',
                    font=('times new roman', 15),
                    bg='white',
                    activebackground='white'
                    )
check1.grid(row=4, column=0, sticky='w', padx=100, pady=10)

forgotpwdButton1 = Button(loginLabel1, text = 'Forgot Password?',
                        font=('times new roman', 15, 'bold'),
                        bd=0,
                        bg='white',
                        fg='DodgerBlue4',
                        activebackground='white')
forgotpwdButton1.grid(row=5, column=0, sticky='w', padx=100, pady=10)



loginButton1 = Button(loginLabel1, text='Login',
                     font=('times new roman', 15),
                     bg='blue',
                     fg='white',
                     activebackground='blue')
loginButton1.grid(row=6, column=0, pady=10)


registerButton1 = Button(loginframe1, text = 'Need an account? Sign up!',
                        font=('times new roman', 15, 'bold'),
                        bd=0,
                        )
registerButton1.pack(fill=X)



root.mainloop()