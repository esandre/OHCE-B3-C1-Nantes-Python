import parameterized.parameterized
import unittest

from Langues.Constantes import Constantes
from Langues.LangueAnglaise import LangueAnglaise
from Langues.LangueFrancaise import LangueFrancaise
from PeriodeDeLaJournee import PeriodeDeLaJournee
from utilities.OhceBuilder import OhceBuilder


class SalutationsTest(unittest.TestCase):
    @parameterized.parameterized.expand(
        [
            [LangueAnglaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Anglais.HELLO],
            [LangueAnglaise(), PeriodeDeLaJournee.SOIR, Constantes.Anglais.GOOD_EVENING],
            [LangueFrancaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Francais.BONJOUR],
        ],
        lambda _, __, args:
            "test ETANT DONNE un utilisateur disant bonjour dans une langue %s \n"
            "ET que la période de la journée est %s \n"
            "QUAND on saisit une chaîne \n"
            "ALORS la salutation %s est envoyée avant toute réponse"
            %(str(type(args.args[0]).__name__), str(type(args.args[1]).__name__), args.args[2])
    )
    def test_bonjour(self, langue, periode_journee, attendu):
        # ETANT DONNE un utilisateur disant bonjour dans une langue <langue>
        # ET que la période de la journée est <periode_journee>
        ohce = OhceBuilder()\
            .ayant_pour_langue(langue)\
            .ayant_pour_période_de_la_journée(periode_journee)\
            .build()

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("test")

        # ALORS la salutation susmentionnée est envoyé avant toute réponse
        self.assertEqual(attendu, resultat[0:len(attendu)])

    def test_au_revoir(self):
        # QUAND on saisit une chaîne
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome("test")

        # ALORS "Au revoir" est envoyé a la fin
        au_revoir = "Au revoir"
        self.assertEqual(au_revoir, resultat[-len(au_revoir):])


if __name__ == '__main__':
    unittest.main()
