import customtkinter as ctk


class Botao(ctk.CTkButton):
    
    def __init__(self, **args):
        super().__init__(self, **args)
        self.frame = frame # type: ignore
        self.text = text # type: ignore
        self.width = width # type: ignore
        self.heigth = height # type: ignore
        self.font = font # type: ignore

