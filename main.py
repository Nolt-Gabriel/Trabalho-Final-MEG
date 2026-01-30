import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser


customtkinter.set_appearance_mode('light')


cor_primaria = '#D27D3F'
cor_secundaria = '#BD5F1C'
cor_terciaria = '#FFCAA4'
cor_background = '#FFEEDF'
cor_decorativo = '#46B223'


def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2
    
    janela.geometry(f'{largura}x{altura}+{x}+{y}')


def receber_largura(janela):
    largura_tela = janela.winfo_screenwidth()
    print(largura_tela)
    return largura_tela


def receber_altura(janela):
    altura_tela = janela.winfo_screenheight()
    print(altura_tela)
    return altura_tela


def abrir_login():

    applogin = customtkinter.CTk()
    applogin.title('Login')

    applogin.iconbitmap('img/IconImage.ico')

    applogin.geometry('800x600')
    centralizar_janela(applogin, 800, 600)
    applogin.resizable(False, False)


    imageframe = customtkinter.CTkFrame(applogin, width=400, height=600)
    imageframe.grid(row=0, column=0)

    loginframe = customtkinter.CTkFrame(applogin, width=400, height=600, fg_color=cor_primaria)
    loginframe.grid(row=0, column=1, sticky='nsew')

    applogin.grid_columnconfigure(1, weight=1)

    imagelogin = Image.open('img/ImageFrame.png')

    ctk_image = customtkinter.CTkImage(light_image=imagelogin, dark_image=imagelogin, size=(400, 600))

    bg_imageframe = customtkinter.CTkLabel(imageframe, image=ctk_image, text='')

    bg_imageframe.place(relx=0, rely=0, relwidth=1, relheight=1)


    loginframe.grid_columnconfigure(0, weight=1)

    emailentry = customtkinter.CTkEntry(loginframe, placeholder_text='email', text_color=cor_primaria, border_color=cor_secundaria)
    passwordentry = customtkinter.CTkEntry(loginframe, placeholder_text='senha', text_color=cor_primaria, border_color=cor_secundaria)
    loginbutton = customtkinter.CTkButton(loginframe, text='Logar', fg_color=cor_background, text_color=cor_primaria, hover_color=cor_terciaria, command=lambda: abrir_home(applogin))
    cadastrobutton = customtkinter.CTkButton(loginframe, text='Cadastrar', fg_color='transparent', hover_color=cor_secundaria, command=lambda: abrir_cadastro(applogin))

    emailentry.grid(row=0, column=0, padx=20, pady=(200, 10))
    passwordentry.grid(row=1, column=0, padx=20, pady=10)
    loginbutton.grid(row=2, column=0, padx=20, pady=20)
    cadastrobutton.grid(row=3, column=0, padx=20, pady=0)


    applogin.mainloop()


def abrir_cadastro(login):

    appcadastro = customtkinter.CTkToplevel(login)
    appcadastro.title('Cadastro')

    appcadastro.geometry('800x600')
    centralizar_janela(appcadastro, 800, 600)
    appcadastro.resizable(False, False)

    cadastroframe = customtkinter.CTkScrollableFrame(appcadastro, width=400, height=580, fg_color=cor_primaria, scrollbar_button_color=cor_background, scrollbar_button_hover_color=cor_background)
    cadastroframe.grid(row=0, column=0, sticky='nsew')

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
    
    nomeentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='nome', text_color=cor_primaria, border_color=cor_secundaria)
    dataentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='dd/mm/aaaa', text_color=cor_primaria, border_color=cor_secundaria)
    cpfentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='cpf', text_color=cor_primaria, border_color=cor_secundaria)
    telefoneentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='(99) 99999-9999', text_color=cor_primaria, border_color=cor_secundaria)
    emailentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='email', text_color=cor_primaria, border_color=cor_secundaria)
    passwordentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='senha', text_color=cor_primaria, border_color=cor_secundaria)
    cepentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='cep', text_color=cor_primaria, border_color=cor_secundaria)
    ruaentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='rua', text_color=cor_primaria, border_color=cor_secundaria)
    bairroentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='bairro', text_color=cor_primaria, border_color=cor_secundaria)
    ndcasaentry = customtkinter.CTkEntry(cadastroframe, placeholder_text='número da casa', text_color=cor_primaria, border_color=cor_secundaria)
    combobox = customtkinter.CTkComboBox(cadastroframe, values=['Deficiência Física', 'Deficiência Auditiva', 'Deficiência Visual', 'Deficiência Intelectual', 'Deficiência Múltipla', 'Deficiência Psicossocial', 'TEA'], text_color=cor_primaria, border_color=cor_secundaria, dropdown_fg_color=cor_background, dropdown_text_color=cor_secundaria, dropdown_hover_color=cor_terciaria)
    check1 = customtkinter.CTkCheckBox(cadastroframe, text='Feminino', variable=var_fem, onvalue=True, offvalue=False, text_color='white', fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox(var_fem))
    check2 = customtkinter.CTkCheckBox(cadastroframe, text='Masculino', variable=var_masc, onvalue=True, offvalue=False, text_color='white', fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox(var_masc))
    check3 = customtkinter.CTkCheckBox(cadastroframe, text='Outro', variable=var_ocultar, onvalue=True, offvalue=False, text_color='white', fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox(var_ocultar))


    def salvar_cadastro():
        nome = nomeentry.get().strip()
        data_nascimento = dataentry.get().strip()
        cpf = cpfentry.get().strip()
        telefone = telefoneentry.get().strip()
        email = emailentry.get().strip()
        senha = passwordentry.get().strip()
        cep = cepentry.get().strip()
        rua = ruaentry.get().strip()
        bairro = bairroentry.get().strip()
        numero_casa = ndcasaentry.get().strip()
        deficiencia = combobox.get()
        sexo = 'Feminino' if var_fem.get() else 'Masculino' if var_masc.get() else 'Oculto' if var_ocultar.get() else ''

        if not (nome and data_nascimento and cpf and telefone and email and senha and cep and rua and bairro and numero_casa and deficiencia and sexo):
            messagebox.showerror('Erro', 'É necessário preencher todos os campos.')
            return

        dados = {
            'nome': nomeentry.get(),
            'data_nascimento': dataentry.get(),
            'cpf': cpfentry.get(),
            'telefone': telefoneentry.get(),
            'email': emailentry.get(),
            'senha': passwordentry.get(),
            'cep': cepentry.get(),
            'rua': ruaentry.get(),
            'bairro': bairroentry.get(),
            'numero_casa': ndcasaentry.get(),
            'deficiencia': combobox.get(),
            'sexo': 'Feminino' if var_fem.get() else 'Masculino' if var_masc.get() else 'Oculto'
        }
        print(dados)
        appcadastro.destroy()
        login.deiconify()

    cadastrobutton = customtkinter.CTkButton(cadastroframe, text='Cadastrar', fg_color=cor_background, text_color=cor_primaria, hover_color=cor_terciaria, command=salvar_cadastro)
    loginbutton = customtkinter.CTkButton(cadastroframe, text='Logar', fg_color='transparent', hover_color=cor_secundaria, command=lambda: (appcadastro.destroy(),login.deiconify()))


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
    cadastrobutton.grid(row=14, column=0, padx=20, pady=(20, 20))
    loginbutton.grid(row=15, column=0, padx=20, pady=(0, 50))


    login.withdraw()

    appcadastro.protocol(
        'WM_DELETE_WINDOW',
        lambda: (appcadastro.destroy(), login.deiconify())
    )


def abrir_home(login):

    apphome = customtkinter.CTkToplevel(login)
    apphome.title('AcesSol')

    apphome.geometry(f'{receber_largura(apphome)}x{receber_altura(apphome)}')
    apphome.state('zoomed')

    largura = receber_largura(apphome)
    altura = receber_altura(apphome)   

    apphome.grid_columnconfigure(0, weight=1) 
    apphome.grid_rowconfigure(1, weight=1)

    headerframe = customtkinter.CTkFrame(apphome, width=largura, height=altura/10, fg_color=cor_primaria, corner_radius=0)
    headerframe.grid(row=0, column=0, sticky='ew')

    mainframe = customtkinter.CTkScrollableFrame(apphome, fg_color=cor_background, corner_radius=0, scrollbar_button_color=cor_background, scrollbar_button_hover_color=cor_background)
    mainframe.grid(row=1, column=0, sticky='nsew')

    mainframe.grid_rowconfigure(0, weight=1)
    mainframe.grid_columnconfigure(0, weight=1)

    telas = {}

    def mostrar(nome):
        for frame in telas.values():
            frame.grid_remove()
        telas[nome].grid(sticky='nsew')

    for nome in ['Inicio', 'Sobre', 'Blog', 'Empregos', 'Cursos']:
        frame = customtkinter.CTkFrame(
            mainframe,
            fg_color=cor_background,
            corner_radius=0
        )
        frame.grid(row=0, column=0, sticky='nsew')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        telas[nome] = frame

    mostrar('Inicio')
    

    headerframe.grid_columnconfigure(0, weight=1)

    imageframe = customtkinter.CTkFrame(headerframe, 200, 50)
    imageframe.grid(row=0, column=0, padx=20, pady=20, sticky='w')

    imageheader = Image.open('img/logo.png')

    ctk_image = customtkinter.CTkImage(light_image=imageheader, dark_image=imageheader, size=(200, 50))

    bg_imageframe = customtkinter.CTkLabel(imageframe, image=ctk_image, text='', fg_color=cor_primaria)

    bg_imageframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    buttoninicio = customtkinter.CTkButton(headerframe, text='Inicio', fg_color='transparent', width=largura/15, hover_color=cor_secundaria, font=('Inter', 17, 'bold'), command=lambda: mostrar('Inicio'))
    buttoninicio.grid(row=0, column=1, padx=10, pady=20)
    buttonsobre = customtkinter.CTkButton(headerframe, text='Sobre', fg_color='transparent', width=largura/15, hover_color=cor_secundaria, font=('Inter', 17, 'bold'), command=lambda: mostrar('Sobre'))
    buttonsobre.grid(row=0, column=2, padx=10, pady=20)
    buttonblog = customtkinter.CTkButton(headerframe, text='Blog', fg_color='transparent', width=largura/15, hover_color=cor_secundaria, font=('Inter', 17, 'bold'), command=lambda: mostrar('Blog'))
    buttonblog.grid(row=0, column=3, padx=10, pady=20)
    buttonemprego = customtkinter.CTkButton(headerframe, text='Empregos', fg_color='transparent', width=largura/15, hover_color=cor_secundaria, font=('Inter', 17, 'bold'), command=lambda: mostrar('Empregos'))
    buttonemprego.grid(row=0, column=4, padx=10, pady=20)
    buttonemprego = customtkinter.CTkButton(headerframe, text='Cursos', fg_color='transparent', width=largura/15, hover_color=cor_secundaria, font=('Inter', 17, 'bold'), command=lambda: mostrar('Cursos'))
    buttonemprego.grid(row=0, column=5, padx=10, pady=20)
    buttonsair = customtkinter.CTkButton(headerframe, text='[ >', fg_color='transparent', width=largura/15, hover_color=cor_primaria, font=('Inter', 17, 'bold'), command=lambda: (apphome.destroy(),login.deiconify()))
    buttonsair.grid(row=0, column=6, padx=10, pady=20)

    textframe = customtkinter.CTkFrame(telas['Inicio'], fg_color='transparent', height=altura/2)
    textframe.grid(row=0, column=0, padx=(80 ,20), pady=(40, 20), sticky='nsew')

    imageframe = customtkinter.CTkFrame(telas['Inicio'], fg_color='transparent', height=altura/1.3)
    imageframe.grid(row=0, column=1, padx=0, pady=0, sticky='nse')

    imageinicio = Image.open('img/ImageFrame3.png')

    ctk_image = customtkinter.CTkImage(light_image=imageinicio, dark_image=imageinicio, size=(largura//2, altura//1.3))

    bg_imageframe = customtkinter.CTkLabel(imageframe, image=ctk_image, text='', fg_color=cor_primaria)

    bg_imageframe.grid(row=0, column=0, sticky='nsew')

    titletext1 = customtkinter.CTkLabel(textframe, text='Acessibilidade e', text_color=cor_primaria, font=('Inter', 44, 'bold'))
    titletext1.grid(row=0, column=0, pady=(80, 0), sticky='w', padx=20)
    titletext2 = customtkinter.CTkLabel(textframe, text='solidariedade para todos', text_color=cor_primaria, font=('Inter', 44, 'bold'))
    titletext2.grid(row=1, column=0, sticky='w', padx=20)

    iniciotext1 = customtkinter.CTkLabel(textframe, text='Nosso objetivo é trazer mais inclusão a pessoas que normalmente são ', text_color=cor_primaria, font=('Inter', 14))
    iniciotext1.grid(row=3, column=0, pady=(20, 0), sticky='w', padx=20)
    iniciotext2 = customtkinter.CTkLabel(textframe, text='esquecidas, aqui vocês podem melhorar seu currículo com cursos', text_color=cor_primaria, font=('Inter', 14))
    iniciotext2.grid(row=4, column=0, sticky='w', padx=20)   
    iniciotext3 = customtkinter.CTkLabel(textframe, text='profissionalizantes e de qualidade que implementam suas habilidades e os', text_color=cor_primaria, font=('Inter', 14))
    iniciotext3.grid(row=5, column=0, sticky='w', padx=20)
    iniciotext4 = customtkinter.CTkLabel(textframe, text='ajudam a ingressar no mercado de trabalho, além de encontrar vagas de', text_color=cor_primaria, font=('Inter', 14))
    iniciotext4.grid(row=6, column=0, sticky='w', padx=20)
    iniciotext5 = customtkinter.CTkLabel(textframe, text='emprego onde se sentirem mais confortáveis e incluídos', text_color=cor_primaria, font=('Inter', 14))
    iniciotext5.grid(row=7, column=0, pady=(0, 40),sticky='w', padx=20)

    buttontext = customtkinter.CTkButton(textframe, text='Perfil', fg_color='transparent', border_width=1, border_color=cor_primaria, text_color=cor_primaria, hover_color=cor_terciaria, font=('Inter', 17, 'bold'))
    buttontext.grid(row=8, column=0, sticky='w', padx=20)

    telas['Inicio'].grid_columnconfigure(0, weight=1)
    telas['Inicio'].grid_columnconfigure(1, weight=1)
    telas['Inicio'].grid_rowconfigure(0, weight=1)

    centerframe = customtkinter.CTkFrame(telas['Sobre'], fg_color='transparent', width=largura)
    centerframe.grid(row=0, column=0, padx=50)

    imageframe = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    imageframe.grid(row=6, column=0, sticky='nsew', columnspan=2)

    centerframe.grid_columnconfigure(0, weight=1)

    imagesobre = Image.open('img/girassolzinho.png')

    ctk_image = customtkinter.CTkImage(light_image=imagesobre, dark_image=imagesobre, size=(largura/4, altura/3))

    bg_imageframe = customtkinter.CTkLabel(imageframe, image=ctk_image, text='', fg_color='transparent')

    bg_imageframe.grid(row=0, column=0, sticky='nsew', padx=(largura/3.4, 0), pady=50)

    titletext1 = customtkinter.CTkLabel(centerframe, text='Conheça o AcesSol', text_color=cor_primaria, font=('Inter', 44, 'bold'))
    titletext1.grid(row=0, column=0, pady=(40, 40), columnspan=3)

    sobretext1 = customtkinter.CTkLabel(centerframe, text='AcesSol é um projeto criado pelos alunos do 2º ano de Informática e do 2º ano de Comércio do IFRN Campus Natal-Zona Norte', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext1.grid(row=1, column=0, columnspan=3)
    sobretext2 = customtkinter.CTkLabel(centerframe, text='com orientação da Docente Marjorie Ramos. Neste projeto, buscamos ajudar a contruir uma cidade mais acessível e solidaria', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext2.grid(row=2, column=0, columnspan=3)
    sobretext3 = customtkinter.CTkLabel(centerframe, text='para todos, aqui todos PCDs poderão ser devidamente incluídos na sociedade. Com uma aba Cursos e Empregos, nós', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext3.grid(row=3, column=0, columnspan=3)
    sobretext4 = customtkinter.CTkLabel(centerframe, text='disponibilizamos formas de vocês ingressarem no mercado de trabalho, tanto disponibilizando vagas, quanto aumentando o', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext4.grid(row=4, column=0, columnspan=3)
    sobretext5 = customtkinter.CTkLabel(centerframe, text='nível de conhecimento dos participantes com cursos profissionalizantes que os ajudam a ter mais chances de arrumar um emprego', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext5.grid(row=5, column=0, columnspan=3)

    titletext2 = customtkinter.CTkLabel(centerframe, text='Nossos Pilares', text_color=cor_primaria, font=('Inter', 30, 'bold'))
    titletext2.grid(row=7, column=0, pady=(40, 40), columnspan=3)
    titletext3 = customtkinter.CTkLabel(centerframe, text='Solidariedade', text_color=cor_decorativo, font=('Inter', 24, 'bold'))
    titletext3.grid(row=8, column=0, pady=80)
    titletext4 = customtkinter.CTkLabel(centerframe, text='Acessibilidade', text_color=cor_decorativo, font=('Inter', 24, 'bold'))
    titletext4.grid(row=9, column=2, pady=80)
    titletext5 = customtkinter.CTkLabel(centerframe, text='Inclusão', text_color=cor_decorativo, font=('Inter', 24, 'bold'))
    titletext5.grid(row=10, column=0, pady=80)

    textframe1 = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    textframe1.grid(row=8, column=1, columnspan=1)
    textframe2 = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    textframe2.grid(row=9, column=0, columnspan=2)
    textframe3 = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    textframe3.grid(row=10, column=1, columnspan=1)

    sobretext6 = customtkinter.CTkLabel(textframe1, text='Sabemos que em diversos momentos Pessoas Com Deficiência passam por dificuldades, seja com', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext6.grid(row=1, column=1, padx=0)
    sobretext7 = customtkinter.CTkLabel(textframe1, text='relação ao preconceito ou simplesmente pela falta de oportunidade imposta a eles, por esse motivo,', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext7.grid(row=2, column=1, padx=0)
    sobretext8 = customtkinter.CTkLabel(textframe1, text='buscamos ajudar o máximo de pessoas com o auxílio de cursos e vagas de emprego exclusivas', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext8.grid(row=3, column=1, padx=0)

    sobretext9 = customtkinter.CTkLabel(textframe2, text='Resolvemos então criar um projeto gratuito e acessível para todos, um local onde todos podem', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext9.grid(row=1, column=0, padx=0)
    sobretext10 = customtkinter.CTkLabel(textframe2, text='refletir e aprender sobre algo novo e que possivelmente o ajudará a conquistar o tão sonhado', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext10.grid(row=2, column=0, padx=0)
    sobretext11 = customtkinter.CTkLabel(textframe2, text='emprego ou até mesmo unicamente pelo conhecimento', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext11.grid(row=3, column=0, padx=0)

    sobretext12 = customtkinter.CTkLabel(textframe3, text='Muitas vezes a exclusão de Pessoas Com Deficiência causa consequências seferas, muitas pessoas se reclusam', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext12.grid(row=1, column=1, padx=0)
    sobretext13 = customtkinter.CTkLabel(textframe3, text='com medo dos constrangimentos e da frustração de se sentirem invisíveis, entretanto, nosso objetivo e desmistificar', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext13.grid(row=2, column=1, padx=0)
    sobretext14 = customtkinter.CTkLabel(textframe3, text='tudo isso trazendo um ambiente mais amigável e inclusivo para que essas pessoas não se sintam excluídas', text_color=cor_primaria, font=('Inter', 17), justify='center', wraplength=largura/1.4)
    sobretext14.grid(row=3, column=1, padx=0)


    telas['Sobre'].grid_columnconfigure(0, weight=1)
    telas['Sobre'].grid_columnconfigure(1, weight=1)
    telas['Sobre'].grid_rowconfigure(0, weight=1)


    centerframe = customtkinter.CTkScrollableFrame(telas['Blog'], orientation='horizontal', scrollbar_button_color=cor_primaria, scrollbar_button_hover_color=cor_secundaria, width=largura, height=altura/2, fg_color='transparent')
    centerframe.grid(row=0, column=0, pady=(altura/6, 0))

    blogframe1 = customtkinter.CTkFrame(centerframe, fg_color='white', border_color=cor_terciaria, border_width=2, width=largura/3, height=altura/2, corner_radius=15)
    blogframe1.grid(row=0, column=0, padx=altura/7)
    blogframe2 = customtkinter.CTkFrame(centerframe, fg_color='white', border_color=cor_terciaria, border_width=2, width=largura/3, height=altura/2, corner_radius=15)
    blogframe2.grid(row=0, column=1, padx=altura/7)
    blogframe3 = customtkinter.CTkFrame(centerframe, fg_color='white', border_color=cor_terciaria, border_width=2, width=largura/3, height=altura/2, corner_radius=15)
    blogframe3.grid(row=0, column=2, padx=altura/7)
    blogframe4 = customtkinter.CTkFrame(centerframe, fg_color='white', border_color=cor_terciaria, border_width=2, width=largura/3, height=altura/2, corner_radius=15)
    blogframe4.grid(row=0, column=3, padx=altura/7)
    blogframe5 = customtkinter.CTkFrame(centerframe, fg_color='white', border_color=cor_terciaria, border_width=2, width=largura/3, height=altura/2, corner_radius=15)
    blogframe5.grid(row=0, column=4, padx=altura/7)
    blogframe6 = customtkinter.CTkFrame(centerframe, fg_color='white', border_color=cor_terciaria, border_width=2, width=largura/3, height=altura/2, corner_radius=15)
    blogframe6.grid(row=0, column=5, padx=altura/7)


    blogframe1.grid_propagate(False)
    blogframe2.grid_propagate(False)
    blogframe3.grid_propagate(False)
    blogframe4.grid_propagate(False)
    blogframe5.grid_propagate(False)
    blogframe6.grid_propagate(False)

    blogframe1.grid_rowconfigure(0, weight=1)
    blogframe1.grid_columnconfigure(0, weight=1)
    blogframe2.grid_rowconfigure(0, weight=1)
    blogframe2.grid_columnconfigure(0, weight=1)
    blogframe3.grid_rowconfigure(0, weight=1)
    blogframe3.grid_columnconfigure(0, weight=1)
    blogframe4.grid_rowconfigure(0, weight=1)
    blogframe4.grid_columnconfigure(0, weight=1)
    blogframe5.grid_rowconfigure(0, weight=1)
    blogframe5.grid_columnconfigure(0, weight=1)
    blogframe6.grid_rowconfigure(0, weight=1)
    blogframe6.grid_columnconfigure(0, weight=1)


    imageframe1 = customtkinter.CTkFrame(blogframe1, fg_color='transparent', corner_radius=15)
    imageframe1.grid(row=0, column=0, sticky='we', padx=15, pady=15)
    imageframe2 = customtkinter.CTkFrame(blogframe2, fg_color='transparent', corner_radius=15)
    imageframe2.grid(row=0, column=0, sticky='we', padx=15, pady=15)
    imageframe3 = customtkinter.CTkFrame(blogframe3, fg_color='transparent', corner_radius=15)
    imageframe3.grid(row=0, column=0, sticky='we', padx=15, pady=15)
    imageframe4 = customtkinter.CTkFrame(blogframe4, fg_color='transparent', corner_radius=15)
    imageframe4.grid(row=0, column=0, sticky='we', padx=15, pady=15)
    imageframe5 = customtkinter.CTkFrame(blogframe5, fg_color='transparent', corner_radius=15)
    imageframe5.grid(row=0, column=0, sticky='we', padx=15, pady=15)
    imageframe6 = customtkinter.CTkFrame(blogframe6, fg_color='transparent', corner_radius=15)
    imageframe6.grid(row=0, column=0, sticky='we', padx=15, pady=15)


    imageframe1.grid_propagate(False)
    imageframe2.grid_propagate(False)
    imageframe3.grid_propagate(False)
    imageframe4.grid_propagate(False)
    imageframe5.grid_propagate(False)
    imageframe6.grid_propagate(False)


    imageblog1 = Image.open('img/blogimage1.png')

    ctk_image = customtkinter.CTkImage(light_image=imageblog1, dark_image=imageblog1, size=(int(largura/3), int(altura/4)))

    bg_imageframe = customtkinter.CTkLabel(imageframe1, image=ctk_image, text='', fg_color='transparent')

    bg_imageframe.grid(row=0, column=0, sticky='we')

    imageblog2 = Image.open('img/blogimage2.png')

    ctk_image = customtkinter.CTkImage(light_image=imageblog2, dark_image=imageblog2, size=(int(largura/3), int(altura/4)))

    bg_imageframe = customtkinter.CTkLabel(imageframe2, image=ctk_image, text='', fg_color='transparent')

    bg_imageframe.grid(row=0, column=0, sticky='we')

    imageblog3 = Image.open('img/blogimage3.png')

    ctk_image = customtkinter.CTkImage(light_image=imageblog3, dark_image=imageblog3, size=(int(largura/3), int(altura/4)))

    bg_imageframe = customtkinter.CTkLabel(imageframe3, image=ctk_image, text='', fg_color='transparent')

    bg_imageframe.grid(row=0, column=0, sticky='we')

    imageblog4 = Image.open('img/blogimage4.png')

    ctk_image = customtkinter.CTkImage(light_image=imageblog4, dark_image=imageblog4, size=(int(largura/3), int(altura/4)))

    bg_imageframe = customtkinter.CTkLabel(imageframe4, image=ctk_image, text='', fg_color='transparent')

    bg_imageframe.grid(row=0, column=0, sticky='we')

    imageblog5 = Image.open('img/blogimage5.png')

    ctk_image = customtkinter.CTkImage(light_image=imageblog5, dark_image=imageblog5, size=(int(largura/3), int(altura/4)))

    bg_imageframe = customtkinter.CTkLabel(imageframe5, image=ctk_image, text='', fg_color='transparent')

    bg_imageframe.grid(row=0, column=0, sticky='we')

    imageblog6 = Image.open('img/blogimage6.png')

    ctk_image = customtkinter.CTkImage(light_image=imageblog6, dark_image=imageblog6, size=(int(largura/3), int(altura/4)))

    bg_imageframe = customtkinter.CTkLabel(imageframe6, image=ctk_image, text='', fg_color='transparent')

    bg_imageframe.grid(row=0, column=0, sticky='we')


    datetext1 = customtkinter.CTkLabel(blogframe1, text='23/01/26', text_color=cor_primaria, font=('Inter', 17))
    datetext1.grid(row=1, column=0, sticky='w', padx=15)
    datetext2 = customtkinter.CTkLabel(blogframe2, text='23/01/26', text_color=cor_primaria, font=('Inter', 17))
    datetext2.grid(row=1, column=0, sticky='w', padx=15)
    datetext3 = customtkinter.CTkLabel(blogframe3, text='23/01/26', text_color=cor_primaria, font=('Inter', 17))
    datetext3.grid(row=1, column=0, sticky='w', padx=15)
    datetext4 = customtkinter.CTkLabel(blogframe4, text='23/01/26', text_color=cor_primaria, font=('Inter', 17))
    datetext4.grid(row=1, column=0, sticky='w', padx=15)
    datetext5 = customtkinter.CTkLabel(blogframe5, text='23/01/26', text_color=cor_primaria, font=('Inter', 17))
    datetext5.grid(row=1, column=0, sticky='w', padx=15)
    datetext6 = customtkinter.CTkLabel(blogframe6, text='23/01/26', text_color=cor_primaria, font=('Inter', 17))
    datetext6.grid(row=1, column=0, sticky='w', padx=15)

    newtext1 = customtkinter.CTkLabel(blogframe1, text='20 filmes com a inclusão de pessoas com deficiência', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    newtext1.grid(row=2, column=0, sticky='w', padx=15)
    newtext2 = customtkinter.CTkLabel(blogframe2, text='O que é o capacitismo e como combate-lo', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    newtext2.grid(row=2, column=0, sticky='w', padx=15)
    newtext3 = customtkinter.CTkLabel(blogframe3, text='Lista completa de tipos de deficiência', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    newtext3.grid(row=2, column=0, sticky='w', padx=15)
    newtext4 = customtkinter.CTkLabel(blogframe4, text='11 direitos de PCDs garantidos pela lei', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    newtext4.grid(row=2, column=0, sticky='w', padx=15)
    newtext5 = customtkinter.CTkLabel(blogframe5, text='O que significa PCD e quem se enquadra como um?', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    newtext5.grid(row=2, column=0, sticky='w', padx=15)
    newtext6 = customtkinter.CTkLabel(blogframe6, text='5 PCDs que entraram para a história', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    newtext6.grid(row=2, column=0, sticky='w', padx=15)

    desctext1 = customtkinter.CTkLabel(blogframe1, wraplength=int(largura/3.2), text='Conheça 20 filmes que pregam a inclusão através da participação de PCDs.', text_color=cor_primaria, font=('Inter', 15))
    desctext1.grid(row=3, column=0, sticky='w', padx=15)
    desctext2 = customtkinter.CTkLabel(blogframe2, wraplength=int(largura/3.2), text='O que é o capacitismo e como combate-lo? Descubra clicando no link abaixo!', text_color=cor_primaria, font=('Inter', 15))
    desctext2.grid(row=3, column=0, sticky='w', padx=15)
    desctext3 = customtkinter.CTkLabel(blogframe3, wraplength=int(largura/3.2), text='Quais são os tipos de deficiêcia que existem? Veja a lista completa', text_color=cor_primaria, font=('Inter', 15))
    desctext3.grid(row=3, column=0, sticky='w', padx=15)
    desctext4 = customtkinter.CTkLabel(blogframe4, wraplength=int(largura/3.2), text='Conheça 11 direitos garantidos as Pessoas Com Deficiências que você deve conhecer', text_color=cor_primaria, font=('Inter', 15))
    desctext4.grid(row=3, column=0, sticky='w', padx=15)
    desctext5 = customtkinter.CTkLabel(blogframe5, wraplength=int(largura/3.2), text='Entenda o que significa a sigla PCD e quem se enquadra nela', text_color=cor_primaria, font=('Inter', 15))
    desctext5.grid(row=3, column=0, sticky='w', padx=15)
    desctext6 = customtkinter.CTkLabel(blogframe6, wraplength=int(largura/3.2), text='Conheça 5 PCDs que superaram os desafios e se tornaram simbolos de superação', text_color=cor_primaria, font=('Inter', 15))
    desctext6.grid(row=3, column=0, sticky='w', padx=15)

    buttonblog1 = customtkinter.CTkButton(blogframe1, text='Acessar', text_color='white', hover_color=cor_primaria, fg_color=cor_decorativo, command=lambda: webbrowser.open_new_tab('https://freedom.ind.br/20-filmes-inclusao-pessoas-com-deficiencia/'))
    buttonblog1.grid(row=4, column=0, sticky='we', padx=15, pady=(10 ,30))
    buttonblog2 = customtkinter.CTkButton(blogframe2, text='Acessar', text_color='white', hover_color=cor_primaria, fg_color=cor_decorativo, command=lambda: webbrowser.open_new_tab('https://www.gov.br/mdh/pt-br/assuntos/noticias/2024/janeiro/capacitismo-o-que-e-como-combater-e-por-que-e-tao-importante-falar-sobre-o-tema'))
    buttonblog2.grid(row=4, column=0, sticky='we', padx=15, pady=(10 ,30))
    buttonblog3 = customtkinter.CTkButton(blogframe3, text='Acessar', text_color='white', hover_color=cor_primaria, fg_color=cor_decorativo,  command=lambda: webbrowser.open_new_tab('https://cidesp.com.br/artigo/quais-sao-os-tipos-de-deficiencia/'))
    buttonblog3.grid(row=4, column=0, sticky='we', padx=15, pady=(10 ,30))
    buttonblog4 = customtkinter.CTkButton(blogframe4, text='Acessar', text_color='white', hover_color=cor_primaria, fg_color=cor_decorativo,  command=lambda: webbrowser.open_new_tab('https://www.deficienteciente.com.br/11-direitos-da-pcd-reconhecidos-por-lei-que-voce-precisa-conhecer.html'))
    buttonblog4.grid(row=4, column=0, sticky='we', padx=15, pady=(10 ,30))
    buttonblog5 = customtkinter.CTkButton(blogframe5, text='Acessar', text_color='white', hover_color=cor_primaria, fg_color=cor_decorativo,  command=lambda: webbrowser.open_new_tab('https://www.terra.com.br/nos/pcd-o-que-significa-e-quem-se-enquadra,8757a445a54c5cd46cb4d5e02579e177dauonkwa.html'))
    buttonblog5.grid(row=4, column=0, sticky='we', padx=15, pady=(10 ,30))
    buttonblog6 = customtkinter.CTkButton(blogframe6, text='Acessar', text_color='white', hover_color=cor_primaria, fg_color=cor_decorativo,  command=lambda: webbrowser.open_new_tab('https://freedom.ind.br/5-pcds-que-mudaram-a-historia-conquista-e-transformacao/'))
    buttonblog6.grid(row=4, column=0, sticky='we', padx=15, pady=(10 ,30))


    telas['Blog'].grid_columnconfigure(0, weight=1)
    telas['Blog'].grid_columnconfigure(1, weight=1)
    telas['Blog'].grid_rowconfigure(0, weight=1)


    centerframe = customtkinter.CTkFrame(telas['Empregos'], width=largura, height=altura, fg_color='transparent')
    centerframe.grid(row=0, column=0, pady=(altura/6, 0))

    filtroframe = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    filtroframe.grid(row=0, column=0)

    vagaframe = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    vagaframe.grid(row=0, column=1, padx=(largura/5, 0))


    var_prec = customtkinter.BooleanVar(value=False)
    var_remt = customtkinter.BooleanVar(value=False)
    var_hybd = customtkinter.BooleanVar(value=False)

    var_fund = customtkinter.BooleanVar(value=False)
    var_medi = customtkinter.BooleanVar(value=False)
    var_supe = customtkinter.BooleanVar(value=False)
    var_grad = customtkinter.BooleanVar(value=False)
    var_mest = customtkinter.BooleanVar(value=False)
    var_dout = customtkinter.BooleanVar(value=False)

    var_ad = customtkinter.BooleanVar(value=False)
    var_cv = customtkinter.BooleanVar(value=False)
    var_ed = customtkinter.BooleanVar(value=False)
    var_fn = customtkinter.BooleanVar(value=False)
    var_tr = customtkinter.BooleanVar(value=False)
    var_if = customtkinter.BooleanVar(value=False)
    var_sd = customtkinter.BooleanVar(value=False)
    var_cc = customtkinter.BooleanVar(value=False)
    var_rh = customtkinter.BooleanVar(value=False)
    var_sg = customtkinter.BooleanVar(value=False)
    var_eh = customtkinter.BooleanVar(value=False)
    var_jr = customtkinter.BooleanVar(value=False)
    var_ot = customtkinter.BooleanVar(value=False)


    def selecionar_checkbox1(selected):
        var_prec.set(False)
        var_remt.set(False)
        var_hybd.set(False)
        apphome.after(10, lambda: selected.set(True))

    def selecionar_checkbox2(selected):
        var_fund.set(False)
        var_medi.set(False)
        var_supe.set(False)
        var_grad.set(False)
        var_mest.set(False)
        var_dout.set(False)
        apphome.after(10, lambda: selected.set(True))

    def selecionar_checkbox3(selected):
        var_ad.set(False)
        var_cv.set(False)
        var_ed.set(False)
        var_fn.set(False)
        var_tr.set(False)
        var_if.set(False)
        var_sd.set(False)
        var_cc.set(False)
        var_rh.set(False)
        var_sg.set(False)
        var_eh.set(False)
        var_jr.set(False)
        var_ot.set(False)
        apphome.after(10, lambda: selected.set(True))


    labelregion = customtkinter.CTkLabel(filtroframe, text='Região Administrativa', text_color=cor_primaria, font=('Inter', 15))
    labelregion.grid(row=0, column=0, sticky='w', padx=20, pady=(20, 0))

    combobox = customtkinter.CTkComboBox(filtroframe, values=['Zona Norte', 'Zona Leste', 'Zona Sul', 'Zona Oeste'], fg_color=cor_background, border_color=cor_primaria)
    combobox.grid(row=1, column=0, sticky='w', padx=20)

    buttonbusca = customtkinter.CTkButton(filtroframe, text='Buscar', fg_color=cor_decorativo, hover_color=cor_primaria, text_color='white')
    buttonbusca.grid(row=2, column=0, sticky='w', padx=20, pady=20)

    labelfiltro = customtkinter.CTkLabel(filtroframe, text='Filtros', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    labelfiltro.grid(row=3, column=0, sticky='w', padx=20)

    checkfiltro1 = customtkinter.CTkLabel(filtroframe, text='LOCAL DE TRABALHO', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    checkfiltro1.grid(row=4, column=0, sticky='w', padx=20)

    check1 = customtkinter.CTkCheckBox(filtroframe, text='Presencial', variable=var_prec, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox1(var_prec))
    check2 = customtkinter.CTkCheckBox(filtroframe, text='Remoto', variable=var_remt, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox1(var_remt))
    check3 = customtkinter.CTkCheckBox(filtroframe, text='Híbrido', variable=var_hybd, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox1(var_hybd))

    check1.grid(row=5, column=0, sticky='w', padx=20, pady=5)
    check2.grid(row=6, column=0, sticky='w', padx=20, pady=5)
    check3.grid(row=7, column=0, sticky='w', padx=20, pady=5)

    checkfiltro2 = customtkinter.CTkLabel(filtroframe, text='ESCOLARIDADE', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    checkfiltro2.grid(row=8, column=0, sticky='w', padx=20)

    check4 = customtkinter.CTkCheckBox(filtroframe, text='Fundamental', variable=var_fund, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox2(var_fund))
    check5 = customtkinter.CTkCheckBox(filtroframe, text='Médio', variable=var_medi, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox2(var_medi))
    check6 = customtkinter.CTkCheckBox(filtroframe, text='Superior', variable=var_supe, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox2(var_supe))
    check7 = customtkinter.CTkCheckBox(filtroframe, text='Pós Graduação', variable=var_grad, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox2(var_grad))
    check8 = customtkinter.CTkCheckBox(filtroframe, text='Mestrado', variable=var_mest, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox2(var_mest))
    check9 = customtkinter.CTkCheckBox(filtroframe, text='Doutorado', variable=var_dout, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox2(var_dout))

    check4.grid(row=9, column=0, sticky='w', padx=20, pady=5)
    check5.grid(row=10, column=0, sticky='w', padx=20, pady=5)
    check6.grid(row=11, column=0, sticky='w', padx=20, pady=5)
    check7.grid(row=12, column=0, sticky='w', padx=20, pady=5)
    check8.grid(row=13, column=0, sticky='w', padx=20, pady=5)
    check9.grid(row=14, column=0, sticky='w', padx=20, pady=5)

    checkfiltro3 = customtkinter.CTkLabel(filtroframe, text='SETOR', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    checkfiltro3.grid(row=15, column=0, sticky='w', padx=20)

    check10 = customtkinter.CTkCheckBox(filtroframe, text='Administração', variable=var_ad, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_ad))
    check11 = customtkinter.CTkCheckBox(filtroframe, text='Comércio e Vendas', variable=var_cv, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_cv))
    check12 = customtkinter.CTkCheckBox(filtroframe, text='Educação', variable=var_ed, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_ed))
    check13 = customtkinter.CTkCheckBox(filtroframe, text='Financias', variable=var_fn, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_fn))
    check14 = customtkinter.CTkCheckBox(filtroframe, text='Turismo', variable=var_tr, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_tr))
    check15 = customtkinter.CTkCheckBox(filtroframe, text='Informática', variable=var_if, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_if))
    check16 = customtkinter.CTkCheckBox(filtroframe, text='Saúde', variable=var_sd, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_sd))
    check17 = customtkinter.CTkCheckBox(filtroframe, text='Comunicação', variable=var_cc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_cc))
    check18 = customtkinter.CTkCheckBox(filtroframe, text='Recursos Humanos', variable=var_rh, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_rh))
    check19 = customtkinter.CTkCheckBox(filtroframe, text='Serviços Gerais', variable=var_sg, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_sg))
    check20 = customtkinter.CTkCheckBox(filtroframe, text='Engenharia', variable=var_eh, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_eh))
    check21 = customtkinter.CTkCheckBox(filtroframe, text='Jurídico', variable=var_jr, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_jr))
    check22 = customtkinter.CTkCheckBox(filtroframe, text='Outros', variable=var_ot, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox3(var_ot))


    check10.grid(row=16, column=0, sticky='w', padx=20, pady=5)
    check11.grid(row=17, column=0, sticky='w', padx=20, pady=5)
    check12.grid(row=18, column=0, sticky='w', padx=20, pady=5)
    check13.grid(row=19, column=0, sticky='w', padx=20, pady=5)
    check14.grid(row=20, column=0, sticky='w', padx=20, pady=5)
    check15.grid(row=21, column=0, sticky='w', padx=20, pady=5)
    check16.grid(row=22, column=0, sticky='w', padx=20, pady=5)
    check17.grid(row=23, column=0, sticky='w', padx=20, pady=5)
    check18.grid(row=24, column=0, sticky='w', padx=20, pady=5)
    check19.grid(row=25, column=0, sticky='w', padx=20, pady=5)
    check20.grid(row=26, column=0, sticky='w', padx=20, pady=5)
    check21.grid(row=27, column=0, sticky='w', padx=20, pady=5)
    check22.grid(row=28, column=0, sticky='w', padx=20, pady=5)

    vaga1 = customtkinter.CTkFrame(vagaframe, fg_color='white', border_color='gray', border_width=1)
    vaga1.grid(row=0, column=0, sticky='we', padx=15, pady=15)
    vaga2 = customtkinter.CTkFrame(vagaframe, fg_color='white', border_color='gray', border_width=1)
    vaga2.grid(row=1, column=0, sticky='we', padx=15, pady=15)
    vaga3 = customtkinter.CTkFrame(vagaframe, fg_color='white', border_color='gray', border_width=1)
    vaga3.grid(row=2, column=0, sticky='we', padx=15, pady=15)

    titletextv1 = customtkinter.CTkLabel(vaga1, text='Vaga de Desenvolvedor', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    titletextv2 = customtkinter.CTkLabel(vaga2, text='Vaga de Marketing Digital', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    titletextv3 = customtkinter.CTkLabel(vaga3, text='Vaga de Assistente de Vendas', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    titletextv1.grid(row=1, column=1, sticky='w', padx=10, pady=10)
    titletextv2.grid(row=1, column=1, sticky='w', padx=10, pady=10)
    titletextv3.grid(row=1, column=1, sticky='w', padx=10, pady=10)

    empresatextv1 = customtkinter.CTkLabel(vaga1, text='Empresa: TechNova', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    empresatextv2 = customtkinter.CTkLabel(vaga2, text='Empresa: Lumina Creativa', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    empresatextv3 = customtkinter.CTkLabel(vaga3, text='Empresa: TrendShop', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    empresatextv1.grid(row=2, column=1, sticky='w', padx=10, pady=10)
    empresatextv2.grid(row=2, column=1, sticky='w', padx=10, pady=10)
    empresatextv3.grid(row=2, column=1, sticky='w', padx=10, pady=10)

    bairrotextv1 = customtkinter.CTkLabel(vaga1, text='Bairro: Lagoa Azul', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    bairrotextv2 = customtkinter.CTkLabel(vaga2, text='Bairro: Potengi', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    bairrotextv3 = customtkinter.CTkLabel(vaga3, text='Bairro: Nossa Senhora da Apresentação', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    bairrotextv1.grid(row=3, column=1, sticky='w', padx=10, pady=10)
    bairrotextv2.grid(row=3, column=1, sticky='w', padx=10, pady=10)
    bairrotextv3.grid(row=3, column=1, sticky='w', padx=10, pady=10)

    salartextv1 = customtkinter.CTkLabel(vaga1, text='Salário: R$ 4.500', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    salartextv2 = customtkinter.CTkLabel(vaga2, text='Salário: R$ 3.800', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    salartextv3 = customtkinter.CTkLabel(vaga3, text='Salário: R$ 2.300', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    salartextv1.grid(row=4, column=1, sticky='w', padx=10, pady=10)
    salartextv2.grid(row=4, column=1, sticky='w', padx=10, pady=10)
    salartextv3.grid(row=4, column=1, sticky='w', padx=10, pady=10)

    localtextv1 = customtkinter.CTkLabel(vaga1, text='Local: Homeoffice', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    localtextv2 = customtkinter.CTkLabel(vaga2, text='Local: Híbrido', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    localtextv3 = customtkinter.CTkLabel(vaga3, text='Local: Presencial', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    localtextv1.grid(row=5, column=1, sticky='w', padx=10, pady=10)
    localtextv2.grid(row=5, column=1, sticky='w', padx=10, pady=10)
    localtextv3.grid(row=5, column=1, sticky='w', padx=10, pady=10)

    buttonemprego1 = customtkinter.CTkButton(vaga1, text='Candidatar-se', text_color='white', fg_color=cor_decorativo, hover_color=cor_primaria)
    buttonemprego2 = customtkinter.CTkButton(vaga2, text='Candidatar-se', text_color='white', fg_color=cor_decorativo, hover_color=cor_primaria)
    buttonemprego3 = customtkinter.CTkButton(vaga3, text='Candidatar-se', text_color='white', fg_color=cor_decorativo, hover_color=cor_primaria)
    buttonemprego1.grid(row=6, column=1, sticky='w', padx=10, pady=15)
    buttonemprego2.grid(row=6, column=1, sticky='w', padx=10, pady=15)
    buttonemprego3.grid(row=6, column=1, sticky='w', padx=10, pady=15)




    telas['Empregos'].grid_columnconfigure(0, weight=1)
    telas['Empregos'].grid_columnconfigure(1, weight=1)
    telas['Empregos'].grid_rowconfigure(0, weight=1)

    centerframe = customtkinter.CTkFrame(telas['Cursos'], width=largura, height=altura, fg_color='transparent')
    centerframe.grid(row=0, column=0, pady=(altura/6, 0))

    filtroframe = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    filtroframe.grid(row=0, column=0)

    vagaframe = customtkinter.CTkFrame(centerframe, fg_color='transparent')
    vagaframe.grid(row=0, column=1, padx=(largura/5, 0))


    var_precc = customtkinter.BooleanVar(value=False)
    var_remtc = customtkinter.BooleanVar(value=False)
    var_hybdc = customtkinter.BooleanVar(value=False)

    var_fundc = customtkinter.BooleanVar(value=False)
    var_medic = customtkinter.BooleanVar(value=False)
    var_supec = customtkinter.BooleanVar(value=False)
    var_gradc = customtkinter.BooleanVar(value=False)
    var_mestc = customtkinter.BooleanVar(value=False)
    var_doutc = customtkinter.BooleanVar(value=False)

    var_adc = customtkinter.BooleanVar(value=False)
    var_cvc = customtkinter.BooleanVar(value=False)
    var_edc = customtkinter.BooleanVar(value=False)
    var_fnc = customtkinter.BooleanVar(value=False)
    var_trc = customtkinter.BooleanVar(value=False)
    var_ifc = customtkinter.BooleanVar(value=False)
    var_sdc = customtkinter.BooleanVar(value=False)
    var_ccc = customtkinter.BooleanVar(value=False)
    var_rhc = customtkinter.BooleanVar(value=False)
    var_sgc = customtkinter.BooleanVar(value=False)
    var_ehc = customtkinter.BooleanVar(value=False)
    var_jrc = customtkinter.BooleanVar(value=False)
    var_otc = customtkinter.BooleanVar(value=False)


    def selecionar_checkbox4(selected):
        var_precc.set(False)
        var_remtc.set(False)
        var_hybdc.set(False)
        apphome.after(10, lambda: selected.set(True))

    def selecionar_checkbox5(selected):
        var_fundc.set(False)
        var_medic.set(False)
        var_supec.set(False)
        var_gradc.set(False)
        var_mestc.set(False)
        var_doutc.set(False)
        apphome.after(10, lambda: selected.set(True))

    def selecionar_checkbox6(selected):
        var_adc.set(False)
        var_cvc.set(False)
        var_edc.set(False)
        var_fnc.set(False)
        var_trc.set(False)
        var_ifc.set(False)
        var_sdc.set(False)
        var_ccc.set(False)
        var_rhc.set(False)
        var_sgc.set(False)
        var_ehc.set(False)
        var_jrc.set(False)
        var_otc.set(False)
        apphome.after(10, lambda: selected.set(True))


    labelregion = customtkinter.CTkLabel(filtroframe, text='Região Administrativa', text_color=cor_primaria, font=('Inter', 15))
    labelregion.grid(row=0, column=0, sticky='w', padx=20, pady=(20, 0))

    combobox = customtkinter.CTkComboBox(filtroframe, values=['Zona Norte', 'Zona Leste', 'Zona Sul', 'Zona Oeste'], fg_color=cor_background, border_color=cor_primaria)
    combobox.grid(row=1, column=0, sticky='w', padx=20)

    buttonbusca = customtkinter.CTkButton(filtroframe, text='Buscar', fg_color=cor_decorativo, hover_color=cor_primaria, text_color='white')
    buttonbusca.grid(row=2, column=0, sticky='w', padx=20, pady=20)

    labelfiltro = customtkinter.CTkLabel(filtroframe, text='Filtros', text_color=cor_primaria, font=('Inter', 17, 'bold'))
    labelfiltro.grid(row=3, column=0, sticky='w', padx=20)

    checkfiltro1 = customtkinter.CTkLabel(filtroframe, text='MODALIDADE DE ENSINO', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    checkfiltro1.grid(row=4, column=0, sticky='w', padx=20)

    check1 = customtkinter.CTkCheckBox(filtroframe, text='Presencial', variable=var_precc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox4(var_precc))
    check2 = customtkinter.CTkCheckBox(filtroframe, text='Remoto', variable=var_remtc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox4(var_remtc))
    check3 = customtkinter.CTkCheckBox(filtroframe, text='Híbrido', variable=var_hybdc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox4(var_hybdc))

    check1.grid(row=5, column=0, sticky='w', padx=20, pady=5)
    check2.grid(row=6, column=0, sticky='w', padx=20, pady=5)
    check3.grid(row=7, column=0, sticky='w', padx=20, pady=5)

    checkfiltro2 = customtkinter.CTkLabel(filtroframe, text='ESCOLARIDADE', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    checkfiltro2.grid(row=8, column=0, sticky='w', padx=20)

    check4 = customtkinter.CTkCheckBox(filtroframe, text='Fundamental', variable=var_fundc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox5(var_fundc))
    check5 = customtkinter.CTkCheckBox(filtroframe, text='Médio', variable=var_medic, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox5(var_medic))
    check6 = customtkinter.CTkCheckBox(filtroframe, text='Superior', variable=var_supec, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox5(var_supec))
    check7 = customtkinter.CTkCheckBox(filtroframe, text='Pós Graduação', variable=var_gradc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox5(var_gradc))
    check8 = customtkinter.CTkCheckBox(filtroframe, text='Mestrado', variable=var_mestc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox5(var_mestc))
    check9 = customtkinter.CTkCheckBox(filtroframe, text='Doutorado', variable=var_doutc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox5(var_doutc))

    check4.grid(row=9, column=0, sticky='w', padx=20, pady=5)
    check5.grid(row=10, column=0, sticky='w', padx=20, pady=5)
    check6.grid(row=11, column=0, sticky='w', padx=20, pady=5)
    check7.grid(row=12, column=0, sticky='w', padx=20, pady=5)
    check8.grid(row=13, column=0, sticky='w', padx=20, pady=5)
    check9.grid(row=14, column=0, sticky='w', padx=20, pady=5)

    checkfiltro3 = customtkinter.CTkLabel(filtroframe, text='SETOR', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    checkfiltro3.grid(row=15, column=0, sticky='w', padx=20)

    check10 = customtkinter.CTkCheckBox(filtroframe, text='Administração', variable=var_adc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_adc))
    check11 = customtkinter.CTkCheckBox(filtroframe, text='Comércio e Vendas', variable=var_cvc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_cvc))
    check12 = customtkinter.CTkCheckBox(filtroframe, text='Educação', variable=var_edc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_edc))
    check13 = customtkinter.CTkCheckBox(filtroframe, text='Financias', variable=var_fnc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_fnc))
    check14 = customtkinter.CTkCheckBox(filtroframe, text='Turismo', variable=var_trc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_trc))
    check15 = customtkinter.CTkCheckBox(filtroframe, text='Informática', variable=var_ifc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_ifc))
    check16 = customtkinter.CTkCheckBox(filtroframe, text='Saúde', variable=var_sdc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_sdc))
    check17 = customtkinter.CTkCheckBox(filtroframe, text='Comunicação', variable=var_ccc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_ccc))
    check18 = customtkinter.CTkCheckBox(filtroframe, text='Recursos Humanos', variable=var_rhc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_rhc))
    check19 = customtkinter.CTkCheckBox(filtroframe, text='Serviços Gerais', variable=var_sgc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_sgc))
    check20 = customtkinter.CTkCheckBox(filtroframe, text='Engenharia', variable=var_ehc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_ehc))
    check21 = customtkinter.CTkCheckBox(filtroframe, text='Jurídico', variable=var_jrc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_jrc))
    check22 = customtkinter.CTkCheckBox(filtroframe, text='Outros', variable=var_otc, onvalue=True, offvalue=False, text_color=cor_primaria, fg_color=cor_secundaria, hover_color=cor_terciaria, border_color=cor_secundaria, command=lambda: selecionar_checkbox6(var_otc))


    check10.grid(row=16, column=0, sticky='w', padx=20, pady=5)
    check11.grid(row=17, column=0, sticky='w', padx=20, pady=5)
    check12.grid(row=18, column=0, sticky='w', padx=20, pady=5)
    check13.grid(row=19, column=0, sticky='w', padx=20, pady=5)
    check14.grid(row=20, column=0, sticky='w', padx=20, pady=5)
    check15.grid(row=21, column=0, sticky='w', padx=20, pady=5)
    check16.grid(row=22, column=0, sticky='w', padx=20, pady=5)
    check17.grid(row=23, column=0, sticky='w', padx=20, pady=5)
    check18.grid(row=24, column=0, sticky='w', padx=20, pady=5)
    check19.grid(row=25, column=0, sticky='w', padx=20, pady=5)
    check20.grid(row=26, column=0, sticky='w', padx=20, pady=5)
    check21.grid(row=27, column=0, sticky='w', padx=20, pady=5)
    check22.grid(row=28, column=0, sticky='w', padx=20, pady=5)

    vaga1 = customtkinter.CTkFrame(vagaframe, fg_color='white', border_color='gray', border_width=1)
    vaga1.grid(row=0, column=0, sticky='we', padx=15, pady=15)
    vaga2 = customtkinter.CTkFrame(vagaframe, fg_color='white', border_color='gray', border_width=1)
    vaga2.grid(row=1, column=0, sticky='we', padx=15, pady=15)
    vaga3 = customtkinter.CTkFrame(vagaframe, fg_color='white', border_color='gray', border_width=1)
    vaga3.grid(row=2, column=0, sticky='we', padx=15, pady=15)

    titletextv1 = customtkinter.CTkLabel(vaga1, text='Curso de Desenvolvedor Web', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    titletextv2 = customtkinter.CTkLabel(vaga2, text='Curso de Turismo', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    titletextv3 = customtkinter.CTkLabel(vaga3, text='Curso de Operador de Caixa', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    titletextv1.grid(row=1, column=1, sticky='w', padx=10, pady=10)
    titletextv2.grid(row=1, column=1, sticky='w', padx=10, pady=10)
    titletextv3.grid(row=1, column=1, sticky='w', padx=10, pady=10)

    empresatextv1 = customtkinter.CTkLabel(vaga1, text='Empresa: TechNova', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    empresatextv2 = customtkinter.CTkLabel(vaga2, text='Empresa: Lumina Creativa', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    empresatextv3 = customtkinter.CTkLabel(vaga3, text='Empresa: TrendShop', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    empresatextv1.grid(row=2, column=1, sticky='w', padx=10, pady=10)
    empresatextv2.grid(row=2, column=1, sticky='w', padx=10, pady=10)
    empresatextv3.grid(row=2, column=1, sticky='w', padx=10, pady=10)

    bairrotextv1 = customtkinter.CTkLabel(vaga1, text='Bairro: Lagoa Azul', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    bairrotextv2 = customtkinter.CTkLabel(vaga2, text='Bairro: Potengi', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    bairrotextv3 = customtkinter.CTkLabel(vaga3, text='Bairro: Nossa Senhora da Apresentação', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    bairrotextv1.grid(row=3, column=1, sticky='w', padx=10, pady=10)
    bairrotextv2.grid(row=3, column=1, sticky='w', padx=10, pady=10)
    bairrotextv3.grid(row=3, column=1, sticky='w', padx=10, pady=10)

    duratextv1 = customtkinter.CTkLabel(vaga1, text='Duração: 120h', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    duratextv2 = customtkinter.CTkLabel(vaga2, text='Duração: 80h', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    duratextv3 = customtkinter.CTkLabel(vaga3, text='Duração: 60h', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    duratextv1.grid(row=4, column=1, sticky='w', padx=10, pady=10)
    duratextv2.grid(row=4, column=1, sticky='w', padx=10, pady=10)
    duratextv3.grid(row=4, column=1, sticky='w', padx=10, pady=10)

    localtextv1 = customtkinter.CTkLabel(vaga1, text='Modalidade: Remoto', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    localtextv2 = customtkinter.CTkLabel(vaga2, text='Modalidade: Híbrido', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    localtextv3 = customtkinter.CTkLabel(vaga3, text='Modalidade: Presencial', text_color=cor_primaria, font=('Inter', 15, 'bold'))
    localtextv1.grid(row=5, column=1, sticky='w', padx=10, pady=10)
    localtextv2.grid(row=5, column=1, sticky='w', padx=10, pady=10)
    localtextv3.grid(row=5, column=1, sticky='w', padx=10, pady=10)

    buttoncurso1 = customtkinter.CTkButton(vaga1, text='Inscrever-se', text_color='white', fg_color=cor_decorativo, hover_color=cor_primaria)
    buttoncurso2 = customtkinter.CTkButton(vaga2, text='Inscrever-se', text_color='white', fg_color=cor_decorativo, hover_color=cor_primaria)
    buttoncurso3 = customtkinter.CTkButton(vaga3, text='Inscrever-se', text_color='white', fg_color=cor_decorativo, hover_color=cor_primaria)
    buttoncurso1.grid(row=6, column=1, sticky='w', padx=10, pady=15)
    buttoncurso2.grid(row=6, column=1, sticky='w', padx=10, pady=15)
    buttoncurso3.grid(row=6, column=1, sticky='w', padx=10, pady=15)


    telas['Cursos'].grid_columnconfigure(0, weight=1)
    telas['Cursos'].grid_columnconfigure(1, weight=1)
    telas['Cursos'].grid_rowconfigure(0, weight=1)


    login.withdraw()

    apphome.protocol(
        'WM_DELETE_WINDOW',
        lambda: (apphome.destroy(), login.deiconify())
    )

abrir_login()