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
            [LangueAnglaise(), PeriodeDeLaJournee.MATIN, Constantes.Anglais.GOOD_MORNING],
            [LangueAnglaise(), PeriodeDeLaJournee.APRES_MIDI, Constantes.Anglais.GOOD_AFTERNOON],
            [LangueAnglaise(), PeriodeDeLaJournee.SOIR, Constantes.Anglais.GOOD_EVENING],
            [LangueAnglaise(), PeriodeDeLaJournee.NUIT, Constantes.Anglais.GOOD_NIGHT],
            [LangueFrancaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Francais.BONJOUR],
            [LangueFrancaise(), PeriodeDeLaJournee.MATIN, Constantes.Francais.BONJOUR],
            [LangueFrancaise(), PeriodeDeLaJournee.APRES_MIDI, Constantes.Francais.BONJOUR],
            [LangueFrancaise(), PeriodeDeLaJournee.SOIR, Constantes.Francais.BONSOIR],
            [LangueFrancaise(), PeriodeDeLaJournee.NUIT, Constantes.Francais.BONSOIR],
        ],
        lambda _, __, args:
            "test ETANT DONNE un utilisateur parlant la langue %s \n"
            "ET que la période de la journée est %s \n"
            "QUAND on saisit une chaîne \n"
            "ALORS la salutation %s est envoyée avant toute réponse"
            %(str(type(args.args[0]).__name__), str(type(args.args[1]).__name__), args.args[2])
    )
    def test_bonjour(self, langue, periode_journee, attendu):
        ohce = OhceBuilder()\
            .ayant_pour_langue(langue)\
            .ayant_pour_période_de_la_journée(periode_journee)\
            .build()

        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.parameterized.expand(
        [
            [LangueFrancaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Francais.AU_REVOIR],
        ],
        lambda _, __, args:
        "test ETANT DONNE un utilisateur parlant la langue %s \n"
        "ET que la période de la journée est %s \n"
        "QUAND on saisit une chaîne \n"
        "ALORS la salutation %s est envoyée à la fin"
        % (str(type(args.args[0]).__name__), str(type(args.args[1]).__name__), args.args[2])
    )
    def test_au_revoir(self, langue, periode_journee, salutation):
        ohce = OhceBuilder()\
            .ayant_pour_langue(langue)\
            .ayant_pour_période_de_la_journée(periode_journee)\
            .build()

        resultat = ohce.palindrome("test")

        self.assertEqual(salutation, resultat[-len(salutation):])


if __name__ == '__main__':
    unittest.main()
