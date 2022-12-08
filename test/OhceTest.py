import unittest

from Langues.Constantes import Constantes
from Langues.LangueAnglaise import LangueAnglaise
from Langues.LangueFrancaise import LangueFrancaise
from PeriodeDeLaJournee import PeriodeDeLaJournee
from utilities.OhceBuilder import OhceBuilder


class OhceTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        # QUAND on saisit une chaîne
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome(chaine)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaine[::-1], resultat)

    def test_palindrome(self):
        palindrome = "radar"

        # QUAND on saisit un palindrome
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome(palindrome)

        # ALORS celui-ci est renvoyé
        self.assertIn(palindrome, resultat)

        # ET 'Bien dit' est renvoyé ensuite
        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn("Bien dit", resultat_apres_palindrome)

    def test_non_palindrome(self):
        # QUAND on saisit une chaîne n'étant pas un palindrome
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome("toto")

        # ALORS 'Bien dit' n'apparaît pas
        self.assertNotIn("Bien dit", resultat)

    def test_bonjour_gb_default(self):
        self.__test_bonjour(LangueAnglaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Anglais.HELLO)

    def test_bonjour_gb_soir(self):
        self.__test_bonjour(LangueAnglaise(), PeriodeDeLaJournee.SOIR, Constantes.Anglais.GOOD_EVENING)

    def test_bonjour_fr_default(self):
        self.__test_bonjour(LangueFrancaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Francais.BONJOUR)

    def __test_bonjour(self, langue, periode_journee, attendu):
        # ETANT DONNE un utilisateur disant bonjour d'une certaine manière
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
