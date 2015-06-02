from alphaid import AlphaID

ALPHABET = 'IWKZCAF12345678'
LEN = 5

aid = AlphaID(ALPHABET, LEN)

string_id = aid.encode(2345) # WI4FA
val_id = aid.decode(string_id) # 2345
