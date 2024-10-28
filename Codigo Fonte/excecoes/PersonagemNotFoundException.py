class PersonagemNotFoundException(Exception):
    def __init__(self):
        super().__init__("Personagem não encontrado!")