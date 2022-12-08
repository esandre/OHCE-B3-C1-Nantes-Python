from Langues.Constantes import Constantes
from PeriodeDeLaJournee import PeriodeDeLaJournee


class LangueAnglaise:

    def dire_bonjour(self, periode_journee):
        return Constantes.Anglais.GOOD_EVENING \
            if periode_journee == PeriodeDeLaJournee.SOIR \
            else Constantes.Anglais.HELLO
