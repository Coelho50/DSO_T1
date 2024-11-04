class BatalhaNotFoundException(Exception):
    def __init__(self):
        super().__init__("Batalha não encontrada!")