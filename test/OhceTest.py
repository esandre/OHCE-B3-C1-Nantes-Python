import unittest

import parameterized as parameterized

from Ohce import Ohce


class OhceTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaîne = "toto"

        # QUAND on saisit une chaîne
        ohce = Ohce()
        resultat = ohce.palindrome(chaîne)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaîne[::-1], resultat)

    def test_palindrome(self):
        palindrome = "radar"

        # QUAND on saisit un palindrome
        ohce = Ohce()
        resultat = ohce.palindrome(palindrome)

        # ALORS celui-ci est renvoyé
        self.assertIn(palindrome, resultat)

        # ET 'Bien dit' est renvoyé ensuite
        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn("Bien dit", resultat_apres_palindrome)

    def test_non_palindrome(self):
        # QUAND on saisit une chaîne n'étant pas un palindrome
        ohce = Ohce()
        resultat = ohce.palindrome("toto")

        # ALORS 'Bien dit' n'apparaît pas
        self.assertNotIn("Bien dit", resultat)

    def test_bonjour(self):
        # QUAND on saisit une chaîne
        ohce = Ohce()
        resultat = ohce.palindrome("test")

        # ALORS "Bonjour" est envoyé avant toute réponse
        bonjour = "Bonjour"
        self.assertEqual(bonjour, resultat[0:len(bonjour)])

    def test_au_revoir(self):
        # QUAND on saisit une chaîne
        ohce = Ohce()
        resultat = ohce.palindrome("test")

        # ALORS "Au revoir" est envoyé a la fin
        au_revoir = "Au revoir"
        self.assertEqual(au_revoir, resultat[-len(au_revoir):])


if __name__ == '__main__':
    unittest.main()
