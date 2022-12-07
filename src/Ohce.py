class Ohce:
    def __init__(self, maniere_de_dire_bonjour):
        self.__maniereDeDireBonjour = maniere_de_dire_bonjour

    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return self.__maniereDeDireBonjour.dire_bonjour() \
               + miroir \
               + ("Bien dit" if miroir == palindrome else "") \
               + "Au revoir"
