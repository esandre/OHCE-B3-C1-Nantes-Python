import unittest

from utilities.OhceBuilder import OhceBuilder


class PalindromeTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()