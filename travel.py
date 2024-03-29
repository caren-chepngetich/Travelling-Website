from tkinter import*
root = Tk()
root . geometry("500*300")

Label(root, text = "Python Registration form",font ="ar 15 bold").grid(row=0,column=)
name = label(root, text="Name")
phone = label(root, text="Phone")
gender = label(root, text="Gender")
emergency = label(root, text="Emergency")
mode of payment = label(root, text="mode of payment")
name.grid(row=1,colum=2)
phone.grid(row=2,colum=2)
gender.grid(row=3,colum=2)
emergency.grid(row=4,colum=2)
mode of payment.grid(row=5,colum=2)

root.mainloop()