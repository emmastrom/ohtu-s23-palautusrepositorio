class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = [0]

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._historia.append(self._arvo)

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._historia.append(self._arvo)

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def kumoa(self):
        a = len(self._historia)-2
        if a >= 0:
            self._arvo = self._historia[a]
            self._historia.pop()

    def arvo(self):
        return self._arvo
