import unittest
from alphaid import AlphaID

ALPHABET = 'IWKZCAF12345678'
LEN = 5

aid = AlphaID(ALPHABET, LEN)

string_id = aid.encode(2345) # WI4FA
val_id = aid.decode(string_id) # 2345

class TestAlphaID(unittest.TestCase):

  def setUp(self):
    self.aid = AlphaID(ALPHABET, LEN)

  def testEncodeShouldBeCorrect(self):
    string_id = self.aid.encode(2345)
    self.assertEqual(string_id, 'WI4FA')

  def testDecodeShouldBeCorrect(self):
    int_id = self.aid.decode('WIAFA')
    self.assertEqual(int_id, 1220)
