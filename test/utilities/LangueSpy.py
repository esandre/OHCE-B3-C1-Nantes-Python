from utilities.LangueStub import LangueStub


class LangueSpy(LangueStub):
    def __init__(self):
        super().__init__()
        self.nombre_appels_a_bien_dit = 0

    def bien_dit(self):
        self.nombre_appels_a_bien_dit += 1
        return super().bien_dit()