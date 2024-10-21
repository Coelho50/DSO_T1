class OpcoesException(Exception):
    def __init__(self):
        super().__init__("nao foram passadas as opcoes do usuario")