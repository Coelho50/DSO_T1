class GrupoCheioException(Exception):
    def __init__(self):
        super().__init__("Valor excede o máximo de 4 personagens na party")