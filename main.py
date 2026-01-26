import customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode('light')


def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2
    
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def abrir_login():

    applogin = customtkinter.CTk()
    applogin.title('Login')

    applogin.iconbitmap("img/IconImage.ico")

    applogin.geometry("800x600")
    centralizar_janela(applogin, 800, 600)
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

    emailentry = customtkinter.CTkEntry(loginframe, placeholder_text='email', text_color='#D27D3F', border_color='#BD5F1C')
    passwordentry = customtkinter.CTkEntry(loginframe, placeholder_text='senha', text_color='#D27D3F', border_color='#BD5F1C')
    loginbutton = customtkinter.CTkButton(loginframe, text='Login', fg_color='#FFEEDF', text_color='#D27D3F', hover_color='#FFCAA4')
    cadastrobutton = customtkinter.CTkButton(loginframe, text='Cadastrar', fg_color='transparent', hover_color='#BD5F1C', command=lambda: abrir_cadastro(applogin))

    emailentry.grid(row=0, column=0, padx=20, pady=(200, 10))
    passwordentry.grid(row=1, column=0, padx=20, pady=10)
    loginbutton.grid(row=2, column=0, padx=20, pady=20)
    cadastrobutton.grid(row=3, column=0, padx=20, pady=0)


    applogin.mainloop()


def abrir_cadastro(login):

    appcadastro = customtkinter.CTkToplevel(login)
    appcadastro.title('Cadastro')

    appcadastro.geometry("800x600")
    centralizar_janela(appcadastro, 800, 600)
    appcadastro.resizable(False, False)

    cadastroframe = customtkinter.CTkScrollableFrame(appcadastro, width=400, height=580, fg_color='#D27D3F', scrollbar_button_color='#FFEEDF', scrollbar_button_hover_color='#FFEEDF')
    cadastroframe.grid(row=0, column=0, sticky="nsew")

    imageframe = customtkinter.CTkFrame(appcadastro, width=400, height=600)
    imageframe.grid(row=0, column=1)

    appcadastro.grid_columnconfigure(1, weight=1)

    imagecadastro = Image.open('img/ImageFrame2.png')

    ctk_image = customtkinter.CTkImage(light_image=imagecadastro, dark_image=imagecadastro, size=(400, 600))

    bg_imageframe = customtkinter.CTkLabel(imageframe, image=ctk_image, text='')

    bg_imageframe.place(relx=0, rely=0, relwidth=1, relheight=1)


    cadastroframe.grid_columnconfigure(0, weight=1)


    var_fem = customtkinter.BooleanVar(value=False)
    var_masc = customtkinter.BooleanVar(value=False)
    var_ocultar = customtkinter.BooleanVar(value=False)

    def selecionar_checkbox(selected):
        var_fem.set(False)
        var_masc.set(False)
        var_ocultar.set(False)
        appcadastro.after(10, lambda: selected.set(True))
    
    nomeentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='nome', text_color='#D27D3F', border_color='#BD5F1C')
    dataentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='dd/mm/aaaa', text_color='#D27D3F', border_color='#BD5F1C')
    cpfentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='cpf', text_color='#D27D3F', border_color='#BD5F1C')
    telefoneentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='(99) 99999-9999', text_color='#D27D3F', border_color='#BD5F1C')
    emailentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='email', text_color='#D27D3F', border_color='#BD5F1C')
    passwordentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='senha', text_color='#D27D3F', border_color='#BD5F1C')
    cepentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='cep', text_color='#D27D3F', border_color='#BD5F1C')
    ruaentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='rua', text_color='#D27D3F', border_color='#BD5F1C')
    bairroentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='bairro', text_color='#D27D3F', border_color='#BD5F1C')
    ndcasaentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='número da casa', text_color='#D27D3F', border_color='#BD5F1C')
    combobox = customtkinter.CTkComboBox(cadastroframe, values=["Deficiência Física", "Deficiência Auditiva", "Deficiência Visual", "Deficiência Intelectual", "Deficiência Múltipla", "Deficiência Psicossocial", "TEA"], text_color='#D27D3F', border_color='#BD5F1C', dropdown_fg_color='#FFEEDF', dropdown_text_color='#BD5F1C', dropdown_hover_color='#FFCAA4')
    check1 = customtkinter.CTkCheckBox(cadastroframe, text="Feminino", variable=var_fem, onvalue=True, offvalue=False, text_color='white', fg_color='#BD5F1C', hover_color='#FFCAA4', border_color='#BD5F1C', command=lambda: selecionar_checkbox(var_fem))
    check2 = customtkinter.CTkCheckBox(cadastroframe, text="Masculino", variable=var_masc, onvalue=True, offvalue=False, text_color='white', fg_color='#BD5F1C', hover_color='#FFCAA4', border_color='#BD5F1C', command=lambda: selecionar_checkbox(var_masc))
    check3 = customtkinter.CTkCheckBox(cadastroframe, text="Ocultar", variable=var_ocultar, onvalue=True, offvalue=False, text_color='white', fg_color='#BD5F1C', hover_color='#FFCAA4', border_color='#BD5F1C', command=lambda: selecionar_checkbox(var_ocultar))
    cadastrobutton = customtkinter.CTkButton(cadastroframe, text='Cadastrar', fg_color='#FFEEDF', text_color='#D27D3F', hover_color='#FFCAA4', command=lambda: (appcadastro.destroy(), login.deiconify()))


    nomeentry.grid(row=0, column=0, padx=20, pady=(50, 10))
    dataentry.grid(row=1, column=0, padx=20, pady=10)
    cpfentry.grid(row=2, column=0, padx=20, pady=10)
    telefoneentry.grid(row=3, column=0, padx=20, pady=10)
    emailentry.grid(row=4, column=0, padx=20, pady=10)
    passwordentry.grid(row=5, column=0, padx=20, pady=10)
    cepentry.grid(row=6, column=0, padx=20, pady=10)
    ruaentry.grid(row=7, column=0, padx=20, pady=10)
    bairroentry.grid(row=8, column=0, padx=20, pady=10)
    ndcasaentry.grid(row=9, column=0, padx=20, pady=10)
    combobox.grid(row=10, column=0, padx=20, pady=10)
    check1.grid(row=11, column=0, padx=20, pady=5,)
    check2.grid(row=12, column=0, padx=20, pady=5,)
    check3.grid(row=13, column=0, padx=20, pady=5,)
    cadastrobutton.grid(row=14, column=0, padx=20, pady=(20, 50))


    login.withdraw()

    appcadastro.protocol(
        "WM_DELETE_WINDOW",
        lambda: (appcadastro.destroy(), login.deiconify())
    )

abrir_login()