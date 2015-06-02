ALPHABET = 'abcdfghjklmnpqrstvwxyz0123456789ABCDFGHJKLMNPQRSTVWXYZ'

class AlphaID:
    def __init__(self, alphabet=ALPHABET, max_length=6):
        self.ALPHABET = alphabet
        self.BASE = len(alphabet)
        self.MAXLEN = max_length
        self.PAD = max_length - 1
        self.BEGINVAL = self.BASE ** self.PAD

    def encode(self, n):
        s = ""
        root = n + self.BEGINVAL
        while root > 0:
            unit = root % self.BASE
            root = root // self.BASE
            s = self.ALPHABET[unit] + s
        return s

    def decode(self, s):
        val = 0
        for c in s:
            val = val * self.BASE + self.ALPHABET.index(c)
        return val - self.BEGINVAL
