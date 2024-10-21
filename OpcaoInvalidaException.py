class OpcaoInvalidaException(Exception):
    def __init__(self):
        super().__init__("opcao fora do intervalo")