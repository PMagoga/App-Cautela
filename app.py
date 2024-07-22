from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from pathlib import Path
from datetime import date
import sqlite3


# path para as imagens
ROOT_PATH = Path(__file__).parent

# cores do aplicativo
frames_colors = '#dbf78d'
labels_color = '#898a86'
buttons_color = '#c0c199'
buttons_hover = '#adae87'


class Conexao:
    def __init__(self):
        # conectando ao banco de dados caso não exista
        self.conn = sqlite3.connect('cautela_subtenencia.db')

    def tabela_itens(self):
        cursor = self.conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS itens(\
                            id INTEGER PRIMARY KEY,\
                            nome_item TEXT NOT NULL,\
                            descricao TEXT NOT NULL)')
        self.conn.commit()

    def cadastra_item(self, item, descricao):
        cursor = self.conn.cursor()
        try:
            cursor.execute('''INSERT INTO itens(nome_item, descricao) VALUES(?, ?)''', (item, descricao))
            self.conn.commit()
            messagebox.showinfo('Cadastro Item', 'Item cadastrado com sucesso')
        except:
            messagebox.showinfo('Cadastro Item', 'Item não cadastrado')


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
        self.frame_esq = MeuFrame(master=self, width=200, height=600, fg_color=frames_colors)
        self.frame_esq.pack(side='left', padx=2, pady=25)
        
        # imagem da tela principal de menus
        self.minha_imagem = ctk.CTkImage(light_image=Image.open(ROOT_PATH / 'novogeppard.png'), 
                                    dark_image=Image.open(ROOT_PATH / 'novogeppard.png'), size=(900, 600))
        self.image_label = ctk.CTkLabel(master=self, text='', image=self.minha_imagem)
        self.image_label.pack(side='left', padx=1, pady=1)

        # fonte dos botões
        btn_font = ctk.CTkFont(family='Helvitica', size=26, weight='bold')
        
        # botões dos menus principal
        textos = ['Cautelar', 'Devolução', 'Cadastro de Militar', 'Cadastro de Item']
        for texto in textos:        
            self.button = ctk.CTkButton(master=self.frame_esq,
                                            text=texto,
                                            width=45, height=45,
                                            corner_radius=40,
                                            font=btn_font,
                                            text_color='black',
                                            hover_color=buttons_hover,
                                            command=lambda t=texto: self.valor_button(t))
            self.button.pack(padx=10, pady=10)                   
    
    # valor dos botões de todos os menus
    def valor_button(self, texto):
        texto_button = str({texto})
        if texto_button == "{'Cautelar'}":
            self.cautelar()
        elif texto_button == "{'Cadastro de Militar'}":
            self.cadastro_militar()
        elif texto_button == "{'Cadastro de Item'}":
            self.cadastro_item()
      
    # função para apagar todos os frames existentes e limpar a tela    
    def apaga_tela(self):
        self.frame_esq.pack_forget()
        self.minha_imagem.pack_forget()        
    
    # botões da tela inicial pressionados
    def botoes_cautela_pressed(self, t):
        if t == 'HOME':
            self.apaga_tela()
            self.tela_inicial()
            self.geometry('1100x600+350+50')
        
        elif t == 'Oficiais':
            self.cautela_of()
            self.cautela_final()                      
            
        elif t == 'ST/Sgt':
            self.cautela_st_sgt()
            self.cautela_final() 
            
        elif t == 'Cb/Sd EP':
            self.cautela_cb_sd()
            self.cautela_final()
            
        else:
            self.cautela_ev()
            self.cautela_final()
    
    # frames da cautela comuns a todos
    def cautela_final(self):
        # fonte
        font_geral = ctk.CTkFont(family='Helvetica', size=23, weight='bold')
        font_opcoes = ctk.CTkFont(family='Helvetica', size=16, weight='bold')
        
        # label da indicação da data
        self.label_data = ctk.CTkLabel(master=self.frame_1, 
                                        text='Data', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.label_data.grid(row=0, column=4, padx=10, pady=25)
        
        # verificação da data atual
        data_atual = date.today()
        data_atual = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
        
        self.label_data_hoje = ctk.CTkLabel(master=self.frame_1, 
                                        text = data_atual, 
                                        font = font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.label_data_hoje.grid(row=0, column=5, padx=5, pady=25)
        
        # label da indicação de observações necessárias
        self.label_obs = ctk.CTkLabel(master=self.frame_2,
                                      text='Observações',
                                      font=font_geral,
                                      fg_color=labels_color,
                                      text_color='black',
                                      corner_radius=40)
        self.label_obs.grid(row=0, column=0, columnspan=2, padx=5, pady=15)
               
        self.label_entry = ctk.CTkTextbox(master=self.frame_2,
                                      font=('Helvetica', 16),
                                      fg_color='#9ca69c',
                                      text_color='black',
                                      corner_radius=10,
                                      scrollbar_button_color='#051df5',
                                      scrollbar_button_hover_color='red',
                                      wrap='word',
                                      width=450, height=100)
        self.label_entry.grid(row=0, column=2, columnspan=4, padx=5, pady=15)        
        
        # indicação da senha
        self.label_senha = ctk.CTkLabel(master=self.frame_3,
                                      text= 'Senha',
                                      font=font_geral,
                                      fg_color=labels_color,
                                      text_color='black',
                                      corner_radius=40)
        self.label_senha.grid(row=0, column=0, columnspan=2, padx=5, pady=25)
               
        self.entry_senha = ctk.CTkEntry(master=self.frame_3,
                                      font=('Helvetica', 16),
                                      fg_color='#9ca69c',
                                      text_color='black',
                                      corner_radius=10,
                                      show='*',
                                      width=200, height=20)
        self.entry_senha.grid(row=0, column=3, padx=5, pady=25)
    
    # somente oficiais     
    def cautela_of(self):
        # fonte
        font_geral = ctk.CTkFont(family='Helvetica', size=23, weight='bold')
        font_opcoes = ctk.CTkFont(family='Helvetica', size=16, weight='bold')       
                
        # indicação do posto
        self.image_label = ctk.CTkLabel(master=self.frame_1, 
                                        text='Posto', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.image_label.grid(row=0, column=0, padx=10, pady=25)
        
        self.opcao_posto = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['Major', 'Capitão', '1° Tenente', '2° Tenente'],
                                             font=font_opcoes,
                                             text_color='Black')
        self.opcao_posto.grid(row=0, column=1, padx=5, pady=5)
        
        # indicação do nome
        self.label_nome = ctk.CTkLabel(master=self.frame_1, 
                                        text='Nome', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.label_nome.grid(row=0, column=2, padx=10, pady=25)
        
        self.opcao_nome = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['Major', 'Capitão', '1° Tenente', '2° Tenente'],
                                             font=font_opcoes,
                                             text_color='black')
        self.opcao_nome.grid(row=0, column=3, padx=5, pady=5)
    
    # somente st/sgt
    def cautela_st_sgt(self):
        # fonte
        font_geral = ctk.CTkFont(family='Helvetica', size=23, weight='bold')
        font_opcoes = ctk.CTkFont(family='Helvetica', size=16, weight='bold')       
                
        # indicação do posto
        self.image_label = ctk.CTkLabel(master=self.frame_1, 
                                        text='Grad', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.image_label.grid(row=0, column=0, padx=10, pady=25)
        
        self.opcao_posto = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['ST', '1º Sgt', '2º Sgt', '3º Sgt'],
                                             font=font_opcoes,
                                             text_color='Black')
        self.opcao_posto.grid(row=0, column=1, padx=5, pady=5)
        
        # indicação do nome
        self.label_nome = ctk.CTkLabel(master=self.frame_1, 
                                        text='Nome', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.label_nome.grid(row=0, column=2, padx=10, pady=25)
        
        self.opcao_nome = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['Major', 'Capitão', '1° Tenente', '2° Tenente'],
                                             font=font_opcoes,
                                             text_color='black')
        self.opcao_nome.grid(row=0, column=3, padx=5, pady=5)
    
    # somente cb/sd        
    def cautela_cb_sd(self):
        # fonte
        font_geral = ctk.CTkFont(family='Helvetica', size=23, weight='bold')
        font_opcoes = ctk.CTkFont(family='Helvetica', size=16, weight='bold')       
                
        # indicação do posto
        self.image_label = ctk.CTkLabel(master=self.frame_1, 
                                        text='Grad', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.image_label.grid(row=0, column=0, padx=10, pady=25)
        
        self.opcao_posto = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['Cb', 'Sd'],
                                             font=font_opcoes,
                                             text_color='Black')
        self.opcao_posto.grid(row=0, column=1, padx=5, pady=5)
        
        # indicação do nome
        self.label_nome = ctk.CTkLabel(master=self.frame_1, 
                                        text='Nome', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.label_nome.grid(row=0, column=2, padx=10, pady=25)
        
        self.opcao_nome = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['Major', 'Capitão', '1° Tenente', '2° Tenente'],
                                             font=font_opcoes,
                                             text_color='black')
        self.opcao_nome.grid(row=0, column=3, padx=5, pady=5)
    
    # somente soldados efetivos variável    
    def cautela_ev(self):
        # fonte
        font_geral = ctk.CTkFont(family='Helvetica', size=23, weight='bold')
        font_opcoes = ctk.CTkFont(family='Helvetica', size=16, weight='bold')       
                
        # indicação do posto
        self.image_label = ctk.CTkLabel(master=self.frame_1, 
                                        text='Sd EV Nr', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.image_label.grid(row=0, column=0, padx=10, pady=25)
        
        self.opcao_posto = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['Nr'],
                                             font=font_opcoes,
                                             text_color='Black')
        self.opcao_posto.grid(row=0, column=1, padx=5, pady=5)
        
        # indicação do nome
        self.label_nome = ctk.CTkLabel(master=self.frame_1, 
                                        text='Nome', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.label_nome.grid(row=0, column=2, padx=10, pady=25)
        
        self.opcao_nome = ctk.CTkOptionMenu(master=self.frame_1,
                                             values=['Major', 'Capitão', '1° Tenente', '2° Tenente'],
                                             font=font_opcoes,
                                             text_color='black')
        self.opcao_nome.grid(row=0, column=3, padx=5, pady=5)
    
    # caso botão cautela seja pressionado    
    def cautelar(self):
        self.frame_esq.pack_forget()
        self.image_label.pack_forget()
        self.geometry('1100x400+350+50')
        # criação dos frames dos menus iniciais
        self.frame_esq = MeuFrame(master=self, width=200, height=400, fg_color=frames_colors)
        self.frame_esq.pack(side='left', padx=2, pady=25)
        
        # fonte dos botões
        btn_font = ctk.CTkFont(family='Helvetica', size=26, weight='bold')
        
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
        
        # imagem da tela principal de menus
        self.minha_imagem = MeuFrame(master=self, width=1000, height=600, fg_color=frames_colors)
        self.minha_imagem.pack(side='left', padx=25, pady=25)
        
        # frames da tela
        self.frame_1 = MeuFrame(master=self.minha_imagem, width=1000, height=200, fg_color=frames_colors)
        self.frame_1.pack(padx=15, pady=2)
        self.frame_2 = MeuFrame(master=self.minha_imagem, width=1000, height=200, fg_color=frames_colors)
        self.frame_2.pack(padx=15, pady=2)
        self.frame_3 = MeuFrame(master=self.minha_imagem, width=1000, height=200, fg_color=frames_colors)
        self.frame_3.pack(padx=15, pady=2)
        
    # cadastro de militares
    def cadastro_militar(self):
        self.frame_esq.pack_forget()
        self.image_label.pack_forget()
        self.geometry('1100x400+350+50')
        
        def voltar():
            self.frame.pack_forget()
            self.tela_inicial()
            self.geometry('1100x600+350+50')
        # fonte
        font_geral = ctk.CTkFont(family='Helvetica', size=23, weight='bold')
        font_opcoes = ctk.CTkFont(family='Helvetica', size=16, weight='bold')
        
        # criação dos frames
        self.frame = MeuFrame(master=self, width=1100, height=400, fg_color=frames_colors)
        self.frame.pack(side='left', padx=90, pady=2)
        
        # indicação do posto
        self.indica_posto_grad = ctk.CTkLabel(master=self.frame, 
                                        text='Posto/Grad', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.indica_posto_grad.grid(row=0, column=0, padx=10, pady=25)
        
        self.opcao_posto_grad = ctk.CTkOptionMenu(master=self.frame,
                                             values=['Major', 'Capitão', '1° Tenente', '2° Tenente', 'Subtenente',
                                                     '1º Sgt', '2º Sgt', '3º Sgt', 'Cb', 'Sd EP', 'Sd EV'],
                                             font=font_opcoes,
                                             text_color='Black')
        self.opcao_posto_grad.grid(row=0, column=1, padx=5, pady=5)
        
        self.nome = ctk.CTkLabel(master=self.frame,
                                 text='Nome/Nr',
                                 font=font_geral,
                                 fg_color=labels_color,
                                 text_color='black',
                                 corner_radius=30)
        self.nome.grid(row=0, column=2, padx=10, pady=25)
        
        self.entry_nome = ctk.CTkEntry(master=self.frame,
                                       width=400, height=15,
                                       corner_radius=30,
                                       fg_color=labels_color,
                                       placeholder_text='Nome',
                                       placeholder_text_color='red',
                                       font=font_geral)
        self.entry_nome.grid(row=0, column=3)       
               
        # fonte dos botões
        btn_font = ctk.CTkFont(family='Helvetica', size=26, weight='bold')
        
        self.botao_voltar = ctk.CTkButton(master=self.frame,
                                     text='Voltar',
                                     width=45, height=45,
                                     corner_radius=40,
                                     font=btn_font,
                                     text_color='black',
                                     hover_color=buttons_hover,
                                     command=voltar)
        self.botao_voltar.grid(row=1, column=1, padx=15, pady=15)
        
        self.botao_cadastrar = ctk.CTkButton(master=self.frame,
                                     text='Cadastrar',
                                     width=45, height=45,
                                     corner_radius=40,
                                     font=btn_font,
                                     text_color='black',
                                     hover_color=buttons_hover)
        self.botao_cadastrar.grid(row=1, column=3, padx=15, pady=15)
        
    # cadastro de item
    def cadastro_item(self):

        self.frame_esq.pack_forget()
        self.image_label.pack_forget()
        self.geometry('1100x400+350+50')


        def voltar():
            self.frame.pack_forget()
            self.tela_inicial()
            self.geometry('1100x600+350+50')
        # fonte
        font_geral = ctk.CTkFont(family='Helvetica', size=23, weight='bold')
        font_opcoes = ctk.CTkFont(family='Helvetica', size=16, weight='bold')
        
        # criação dos frames
        self.frame = MeuFrame(master=self, width=1100, height=400, fg_color=frames_colors)
        self.frame.pack(side='left', padx=40, pady=2)
        
        # indicação do item
        self.indica_item = ctk.CTkLabel(master=self.frame, 
                                        text='Item', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.indica_item.grid(row=0, column=0, padx=10, pady=25)
        
        self.entry_nome = ctk.CTkEntry(master=self.frame,
                                       width=300, height=15,
                                       corner_radius=30,
                                       fg_color=labels_color,
                                       placeholder_text='Item',
                                       placeholder_text_color='red',
                                       font=font_geral)
        self.entry_nome.grid(row=0, column=1, columnspan=2, padx=5, pady=25)
              
        # indicação descrição
        self.label_descricao = ctk.CTkLabel(master=self.frame,
                                        text='Descrição', 
                                        font=font_geral,
                                        fg_color=labels_color,
                                        text_color='black',
                                        corner_radius=40)
        self.label_descricao.grid(row=0, column=3, padx=2, pady=25)
        
        self.entry_descricao = ctk.CTkTextbox(master=self.frame,
                                       width=400, height=150,
                                       corner_radius=20,
                                       fg_color=labels_color,
                                       font=('Helvetica', 16),
                                       wrap='word',
                                       scrollbar_button_color='#051df5',
                                       scrollbar_button_hover_color='red')
        self.entry_descricao.grid(row=0, column=4, columnspan=4, padx=2, pady=15, ipady=1)


        # fonte dos botões
        btn_font = ctk.CTkFont(family='Helvetica', size=26, weight='bold')
        
        self.botao_voltar = ctk.CTkButton(master=self.frame,
                                     text='Voltar',
                                     width=45, height=45,
                                     corner_radius=40,
                                     font=btn_font,
                                     text_color='black',
                                     hover_color=buttons_hover,
                                     command=voltar)
        self.botao_voltar.grid(row=1, column=2, padx=15, pady=15)
        
        self.botao_cadastrar = ctk.CTkButton(master=self.frame,
                                     text='Cadastrar',
                                     width=45, height=45,
                                     corner_radius=40,
                                     font=btn_font,
                                     text_color='black',
                                     hover_color=buttons_hover,
                                     command=self.cadastrar_item)
        self.botao_cadastrar.grid(row=1, column=4, padx=5, pady=15)

    def cadastrar_item(self):
        nome_item = self.entry_nome.get()
        descricao_item = self.entry_descricao.get(0.0, 'end')
        print(nome_item)
        print(descricao_item)
        cadastrar = Conexao()
        cadastrar.tabela_itens()
        cadastrar.cadastra_item(nome_item, descricao_item)


if __name__=="__main__":
    app = App()
    app.mainloop()
    

