import customtkinter as ctk

janela = ctk.CTk()
janela.geometry('1000x600')

def teste():
        
        buton = ctk.CTkButton(master=tab2, text='Olá')
        buton.pack(padx=20, pady=20) 

def cautelar():      
        
                    
        # criação do frame página da cautela
        frame = ctk.CTkFrame(master=janela, width=1100, height=600, fg_color="#f5f2ed")
        frame.pack()
        
                
        # menus da página de cautela
        tabview = ctk.CTkTabview(master=frame,
                                width=1100, height=600, 
                                corner_radius=30, 
                                border_color="black", 
                                border_width=1,
                                text_color='black',
                                segmented_button_fg_color='#f8faa2',
                                segmented_button_selected_hover_color='#00896F',
                                segmented_button_unselected_hover_color='#00896F',
                                command=teste,
                                )
        tabview.pack(padx=5, pady=5)    
        
        global tab1, tab2, tab3, tab4
        # itens dos menus
        tab1 = tabview.add('Home')
        tab2 = tabview.add('Oficiais')
        tab3 = tabview.add('ST/Sgt')
        tab4 = tabview.add('Cb/Sd')
        tab5 = tabview.add('Sd EV')

            
        global tabela
        tabela = tabview.get()
        
        # fonte dos botões dos índices
        font_menus = ctk.CTkFont(family='Helvetica', size=22, weight='bold')
        tabview._segmented_button.configure(font=font_menus)

        return tabela

if __name__=='__main__':
        cautelar()
        janela.mainloop()
    