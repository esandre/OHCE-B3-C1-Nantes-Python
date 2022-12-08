class Ohce:
    def __init__(self, langue, periode_journee):
        self.__periode_journee = periode_journee
        self.__langue = langue

    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return self.__langue.dire_bonjour(self.__periode_journee) \
               + miroir \
               + ("Bien dit" if miroir == palindrome else "") \
               + "Au revoir"
