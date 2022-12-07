from Ohce import Ohce
from utilities.ManiereDeDireBonjourStub import ManiereDeDireBonjourStub
from utilities.maniereDeDireBonjourMock import ManiereDeDireBonjourMock


class OhceBuilder():
    def __init__(self):
        self.__maniere_de_dire_bonjour = ManiereDeDireBonjourStub()

    def build(self):
        return Ohce(self.__maniere_de_dire_bonjour)

    @staticmethod
    def default():
        return OhceBuilder().build()

    def ayant_pour_maniere_de_dire_bonjour(self, maniere_de_dire_bonjour):
        self.__maniere_de_dire_bonjour = ManiereDeDireBonjourMock(maniere_de_dire_bonjour)
        return self