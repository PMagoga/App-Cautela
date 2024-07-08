import customtkinter as ctk
from PIL import Image
from pathlib import Path

# path para as imagens
ROOT_PATH = Path(__file__).parent

     
class MeuFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)             
   

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        # criação da janela principal
        self.geometry('1100x600+350+50')
        self.title('Cautela da Subtenência')
        self.resizable(False, False)
        self.tela_inicial()
           
    # função para o início
    def tela_inicial(self):
        # criação dos frames dos menus iniciais
        self.frame_esq = MeuFrame(master=self, width=200, height=600, fg_color='#fcf2d7')
        self.frame_esq.pack(side='left', padx=2, pady=25)
        
        # imagem da tela principal de menus
        self.minha_imagem = ctk.CTkImage(light_image=Image.open(ROOT_PATH / 'novogeppard.png'), 
                                    dark_image=Image.open(ROOT_PATH / 'novogeppard.png'), size=(900, 600))
        self.image_label = ctk.CTkLabel(master=self, text='', image=self.minha_imagem)
        self.image_label.pack(side='left', padx=1, pady=1)

        # fonte dos botões
        btn_font = ctk.CTkFont(family='Helvitica', size=26, weight='bold')
        
        # botões dos menus principal
        textos = ['Cautela', 'Devolução', 'Cadastro de Militar', 'Cadastro de Item']
        for texto in textos:        
            self.button = ctk.CTkButton(master=self.frame_esq,
                                            text=texto,
                                            width=45, height=45,
                                            corner_radius=40,
                                            font=btn_font,
                                            text_color='black',
                                            hover_color='#42ed5c',
                                            command=lambda t=texto: self.valor_button(t))
            self.button.pack(padx=10, pady=10)                   
    
    # valor dos botões de todos os menus
    def valor_button(self, texto):
        texto_button = str({texto})
        if texto_button == "{'Cautela'}":
            self.cautelar()
    
    
    # função para apagar todos os frames existentes e limpar a tela    
    def apaga_tela(self):
        self.frame_esq.pack_forget()
        self.image_label.pack_forget()
        self.minha_imagem.pack_forget()
        
    
    def botoes_cautela_pressed(self, t):
        if t == 'HOME':
            self.apaga_tela()
            self.tela_inicial()
        
        elif t == 'Oficiais':
            self.apaga_tela()
            self.menu_cautelar()                      
            
        elif t == 'ST/Sgt':
            self.apaga_tela()
            self.menu_cautelar()
        elif t == 'Cb/Sd EP':
            self.apaga_tela()
            self.menu_cautelar()
            
        
                   
    def cautelar(self):
        self.frame_esq.pack_forget()
        self.image_label.pack_forget()
        self.menu_cautelar()
        
    def menu_cautelar(self):   
        
        # criação dos frames dos menus iniciais
        self.frame_esq = MeuFrame(master=self, width=200, height=600, fg_color='#fcf2d7')
        self.frame_esq.pack(side='left', padx=2, pady=25)
        
        # imagem da tela principal de menus
        self.minha_imagem = MeuFrame(master=self, width=900, height=600, fg_color='green')
        self.minha_imagem.pack(side='left', padx=2, pady=2)
        
        self.image_label = ctk.CTkLabel(master=self.minha_imagem, text='olá')
        self.image_label.pack(side='left', padx=1, pady=1)
        
        # fonte dos botões
        btn_font = ctk.CTkFont(family='Helvitica', size=26, weight='bold')
        
        # botões
        textos = ['HOME', 'Oficiais', 'ST/Sgt', 'Cb/Sd EP', 'Sd EV']
        for texto in textos:        
            self.button = ctk.CTkButton(master=self.frame_esq,
                                            text=texto,
                                            width=45, height=45,
                                            corner_radius=40,
                                            font=btn_font,
                                            text_color='black',
                                            hover_color='#42ed5c',
                                            command=lambda t=texto: self.botoes_cautela_pressed(t))
            self.button.pack(padx=10, pady=10)
           
        
    
if __name__=="__main__":
    app = App()
    app.mainloop()

