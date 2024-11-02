class PartyNotFoundException(Exception):
    def __init__(self):
        super().__init__("Party não encontrado!")