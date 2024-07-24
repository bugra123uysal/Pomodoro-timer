from time import strftime
import tkinter as tk




yer=tk.Tk()
yer.geometry("600x700")
""" saat """
sath=tk.Label(yer,)
sath.place(x=525 , y=10 )

def nowtime():
    watch=strftime('%H:%M:%S %p')
    sath.config(text=watch)
    sath.after(1000, nowtime)

nowtime()

""" süre çalışma """


workk=tk.Label(yer, bd=2, relief="solid")
workk.place(x=10, y=100 , height=130, width=200)


""" mola """
mlo=tk.Label(yer, bd=2, relief="solid")
mlo.place(x=390, y=100 , height=130, width=200)

"""süreyi  başlat buttonu """

bşltbtn=tk.Button(yer, text="başlat")
bşltbtn.place(x=230 , y=330 , height=40, width=140)

yer.mainloop()


 

