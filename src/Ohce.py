class Ohce:
    def __init__(self, langue, periode_journee):
        self.__periode_journee = periode_journee
        self.__langue = langue

    def __bien_dit(self):
        return self.__langue.bien_dit()

    def __bonjour(self):
        return self.__langue.dire_bonjour(self.__periode_journee)

    def __au_revoir(self):
        return "Au revoir"

    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return self.__bonjour() \
               + miroir \
               + (self.__bien_dit() if miroir == palindrome else "") \
               + self.__au_revoir()
