import customtkinter as ctk
from PIL import Image
from pathlib import Path
from cautela import cautelar


    
ROOT_PATH = Path(__file__).parent

def janela_inicial():

    # frame dos botões de menus iniciais
    frame_esq = ctk.CTkFrame(master=janela, width=200, height=600)
    frame_esq.pack(side='left', padx=2, pady=2)

    # fonte dos botões
    btn_font = ctk.CTkFont(family='Arial', size= 26, weight='bold')



    # imagem da tela principal de menus
    minha_imagem = ctk.CTkImage(light_image=Image.open(ROOT_PATH / 'novogeppard.png'), 
                                dark_image=Image.open(ROOT_PATH / 'novogeppard.png'), size=(870, 600))
    image_label = ctk.CTkLabel(master=janela, text='', image=minha_imagem)
    image_label.pack(side='left', padx=1, pady=1)

    # botões dos menus
    # botão de cautela
    button = ctk.CTkButton(master=frame_esq,
                        text="Cautela", 
                        width=55, height=45, 
                        corner_radius=40,
                        font=btn_font,
                        text_color='black',
                        hover_color="#42ed5c",
                        command=cautelar)
    button.pack(padx=10, pady=10)

    # botão devolução
    button = ctk.CTkButton(master=frame_esq, 
                        text="Devolução", 
                        width=55, height=45, 
                        corner_radius=40,
                        font=btn_font,
                        text_color='black',
                        hover_color="#42ed5c")
    button.pack(padx=10, pady=10)

    # botão de cadastro de militar
    button = ctk.CTkButton(master=frame_esq, 
                        text="Cadastrar Militar",
                        width=55, height=45, 
                        corner_radius=40,
                        font=btn_font,
                        text_color='black',
                        hover_color="#42ed5c")
    button.pack(padx=10, pady=10)

    # botão de cadastro de item
    button = ctk.CTkButton(master=frame_esq, 
                        text="Cadastrar Item", 
                        width=55, height=45, 
                        corner_radius=40,
                        font=btn_font,
                        text_color='black',
                        hover_color="#42ed5c")
    button.pack(padx=10, pady=10)