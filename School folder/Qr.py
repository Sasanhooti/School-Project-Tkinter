
   
def Qr():

   import pyqrcode
   import customtkinter
   import tkinter as tk
    
   
   my_w = tk.Tk()
   my_w.geometry("410x400")  # Size of the window 
   my_w.title("QrCode")  # Adding a title
   my_w.iconbitmap(bitmap = 'Icons\icon.ico')
   e1=customtkinter.CTkEntry(my_w,font=customtkinter.CTkFont(22),width=250)
   e1.grid(row=0,column=0,padx=10,pady=10)
   b1=customtkinter.CTkButton(my_w,font=customtkinter.CTkFont(22),text='Generate QR code',width=50,
       command=lambda:my_generate())
   b1.grid(row=0,column=1,padx=5,pady=10)
   
   l1=customtkinter.CTkLabel(my_w,text='QR to display here')
   l1.grid(row=1,column=0,columnspan=2)
   def my_generate():
       global my_img
       my_qr = pyqrcode.create(e1.get()) 
       #my_qr.svg('G:\\My Drive\\testing\\my_qr.svg', scale=8)#save svg
       my_qr.png('QrCode\QrCode.png', scale=6, 
           module_color=[0, 0, 0, 128], background=[0xff, 0xcc, 0xcc])
       my_qr.show() # display qr code image  in console 
       my_qr = my_qr.xbm(scale=10)
       my_img=tk.BitmapImage(data=my_qr)
       l1.config(image=my_img) # Show the qr code in Label 
   my_w.mainloop()  
   
Qr()