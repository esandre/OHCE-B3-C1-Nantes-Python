from Ohce import Ohce
from PeriodeDeLaJournee import PeriodeDeLaJournee
from utilities.LangueStub import LangueStub


class OhceBuilder():
    def __init__(self):
        self.__langue = LangueStub()
        self.__periode_journee = PeriodeDeLaJournee.DEFAULT

    def build(self):
        return Ohce(self.__langue, self.__periode_journee)

    @staticmethod
    def default():
        return OhceBuilder().build()

    def ayant_pour_langue(self, langue):
        self.__langue = langue
        return self

    def ayant_pour_période_de_la_journée(self, periode_journee):
        self.__periode_journee = periode_journee
        return self
    