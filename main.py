import customtkinter
from PIL import Image


customtkinter.set_appearance_mode('light')


applogin = customtkinter.CTk()

applogin.title('Login')
#applogin.iconbitmap('img/IconImage.ico')

applogin.geometry("800x600")
applogin.resizable(False, False)


imageframe = customtkinter.CTkFrame(applogin, width=400, height=600)
imageframe.grid(row=0, column=0)

loginframe = customtkinter.CTkFrame(applogin, width=400, height=600, fg_color='#D27D3F')
loginframe.grid(row=0, column=1, sticky="nsew")

applogin.grid_columnconfigure(1, weight=1)

imagelogin = Image.open('img/ImageFrame.png')

ctk_image = customtkinter.CTkImage(light_image=imagelogin, dark_image=imagelogin, size=(400, 600))

bg_imageframe = customtkinter.CTkLabel(imageframe, image=ctk_image, text='')

bg_imageframe.place(relx=0, rely=0, relwidth=1, relheight=1)


loginframe.grid_columnconfigure(0, weight=1)

emailentry = customtkinter.CTkEntry(loginframe, placeholder_text='email')
passwordentry = customtkinter.CTkEntry(loginframe, placeholder_text='senha')
loginbutton = customtkinter.CTkButton(loginframe, text='Login', fg_color='#FFEEDF', text_color='#D27D3F')
cadastrobutton = customtkinter.CTkButton(loginframe, text='Cadastrar', fg_color='transparent')


emailentry.grid(row=0, column=0, padx=20, pady=(200, 10))
passwordentry.grid(row=1, column=0, padx=20, pady=10)
loginbutton.grid(row=2, column=0, padx=20, pady=20)
cadastrobutton.grid(row=3, column=0, padx=20, pady=0)

loginframe.grid_columnconfigure(0, weight=1)


applogin.eval('tk::PlaceWindow . center')


applogin.mainloop()