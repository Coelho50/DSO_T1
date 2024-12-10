class RemoverJogadorLogadoException(Exception):
    def __init__(self):
        super().__init__("Removendo cadastro do jogador logado e encerrando sessão")