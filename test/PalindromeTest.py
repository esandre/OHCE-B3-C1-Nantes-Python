import unittest
import parameterized.parameterized

from Langues.Constantes import Constantes
from Langues.LangueAnglaise import LangueAnglaise
from Langues.LangueFrancaise import LangueFrancaise
from utilities.OhceBuilder import OhceBuilder


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        # QUAND on saisit une chaîne
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome(chaine)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaine[::-1], resultat)

    @parameterized.parameterized.expand([
        [LangueAnglaise(), Constantes.Anglais.WELL_DONE],
        [LangueFrancaise(), Constantes.Francais.BIEN_DIT],
    ],
        lambda _, __, args:
        "test ETANT DONNE un utilisateur parlant la langue %s \n"
        "QUAND on saisit un palindrome \n"
        "ALORS %s est renvoyé ensuite"
        % (str(type(args.args[0]).__name__), args.args[1])
    )
    def test_palindrome(self, langue, bien_dit):
        palindrome = "radar"

        ohce = OhceBuilder().ayant_pour_langue(langue).build()
        resultat = ohce.palindrome(palindrome)

        self.assertIn(palindrome, resultat)

        # ET 'Bien dit' est renvoyé ensuite
        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn(bien_dit, resultat_apres_palindrome)

    @parameterized.parameterized.expand([
        [LangueAnglaise(), Constantes.Anglais.WELL_DONE],
        [LangueFrancaise(), Constantes.Francais.BIEN_DIT],
    ],
        lambda _, __, args:
        "test ETANT DONNE un utilisateur parlant la langue %s \n"
        "QUAND on saisit une chaîne n'étant pas un palindrome \n"
        "ALORS %s n'apparaît pas"
        % (str(type(args.args[0]).__name__), args.args[1])
    )
    def test_non_palindrome(self, langue, bien_dit):
        ohce = OhceBuilder().ayant_pour_langue(langue).build()

        resultat = ohce.palindrome("toto")

        self.assertNotIn(bien_dit, resultat)


if __name__ == '__main__':
    unittest.main()