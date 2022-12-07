class Ohce:
    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return "Bonjour" + miroir + ("Bien dit" if miroir == palindrome else "") + "Au revoir"
