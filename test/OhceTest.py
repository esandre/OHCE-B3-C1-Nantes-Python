import unittest

from utilities.OhceBuilder import OhceBuilder


class OhceTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaîne = "toto"

        # QUAND on saisit une chaîne
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome(chaîne)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaîne[::-1], resultat)

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

    def test_bonjour_gb(self):
        self.__test_bonjour("Hello")

    def test_bonjour_fr(self):
        self.__test_bonjour("Bonjour")

    def __test_bonjour(self, maniere_de_dire_bonjour):
        # ETANT DONNE un utilisateur disant bonjour d'une certaine manière
        ohce = OhceBuilder()\
            .ayant_pour_maniere_de_dire_bonjour(maniere_de_dire_bonjour)\
            .build()

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("test")

        # ALORS "Hello" est envoyé avant toute réponse
        self.assertEqual(maniere_de_dire_bonjour, resultat[0:len(maniere_de_dire_bonjour)])

    def test_au_revoir(self):
        # QUAND on saisit une chaîne
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome("test")

        # ALORS "Au revoir" est envoyé a la fin
        au_revoir = "Au revoir"
        self.assertEqual(au_revoir, resultat[-len(au_revoir):])


if __name__ == '__main__':
    unittest.main()
