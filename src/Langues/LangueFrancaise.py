from Langues.Constantes import Constantes
from PeriodeDeLaJournee import PeriodeDeLaJournee


class LangueFrancaise:

    def dire_bonjour(self, periode_journee):
        return Constantes.Francais.BONSOIR \
            if periode_journee in (PeriodeDeLaJournee.SOIR, PeriodeDeLaJournee.NUIT)\
            else Constantes.Francais.BONJOUR

    def bien_dit(self):
        return Constantes.Francais.BIEN_DIT