from time import strftime
import tkinter as tk




yer=tk.Tk()
yer.geometry("600x700")
""" saat """
def nowtime():
    """ güncel saat """
    watch=strftime('%H:%M:%S %p')
    süre.config(text=watch)
    süre.after(1000,nowtime)
   
sgır=tk.Entry(yer, text="")
sgır.place(x=10 , y=50)

     




def start():
   try:
      count=int(sgır.get())
      countdown(count)
      
       

   except ValueError:    
      gerisyn["text"]="sayı giriniz"
       
  
""" süreyi başlatma butonu """
başlat=tk.Button(yer,text="başlat" , command=start )
başlat.place(relx=0.5,rely=0.5)

""" güncel saat  """
süre=tk.Label(yer,)
süre.place(relx=0.92 , rely=0.02 , anchor="center")
""" geri sayım yeri """
gerisyn=tk.Label(yer,)
gerisyn.place(relx=0.7, rely=0.7, height=30, width=120)
""" süre belirtin 
girsüre=tk.Entry(yer,text="" )
girsüre.place(relx=0.3 , rely=0.5, height=30 , width=130)
"""



   
     

 
""" geri sayım """
def countdown(count):
  gerisyn["text"]=count

  if count>0:
     yer.after(1000,countdown  ,count-1)

  else:
     gerisyn["text"]="süreniz doldu"

nowtime()

yer.mainloop()


 

