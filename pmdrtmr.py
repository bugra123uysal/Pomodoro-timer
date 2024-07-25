from time import strftime
import time
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
def bşlll():
    time_over=int(gır.get())*60
    count(time_over)
    
    

def count(time_over):
    if time_over >0:
        mins,secs=divmod(time_over,60)
        timeformer='{:02d}:{:02d}'.format(mins,secs)
        work.config(text=timeformer)
        work.after(1000,lambda:count(time_over-1) )
       
  
    else:
        work.config(text="süre doldu")
        

""" süre çalışma """


work=tk.Label(yer, bd=2, relief="solid")
work.place(x=10, y=100 , height=130, width=200)


""" mola """
mlo=tk.Label(yer, bd=2, relief="solid")
mlo.place(x=390, y=100 , height=130, width=200)
""" süreyi gir """



"""süreyi  başlat buttonu """
bşltbtn=tk.Button(yer, text="başlat", command=bşlll)
bşltbtn.place(x=230 , y=330 , height=40, width=140)
""" süre gir """
gır=tk.Entry(yer,)
gır.place(x=100,y=1, height=20, width=140)
yer.mainloop()


 

