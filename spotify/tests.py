import unittest
from best_before import BestBefore


class TestBestBefore(unittest.TestCase):

    def test_little_endian(self):
        bb = BestBefore('30/09/2001')
        self.assertEqual('2001-09-30', bb.compute())

    def test_medium_endian(self):
        bb = BestBefore('09/30/2001')
        self.assertEqual('2001-09-30', bb.compute())

    def test_little_and_medium(self):
        bb = BestBefore('01/02/2001')
        self.assertEqual('2001-01-02', bb.compute())

    def test_illegal_date(self):
        bb = BestBefore('31/9/1973')
        self.assertEqual('31/9/1973 is illegal', bb.compute())

    def test_guess_single_year_number(self):
        bb = BestBefore('09/30/0')
        self.assertEqual('2000-09-30', bb.compute())

    def test_guess_double_year_number(self):
        bb = BestBefore('09/30/00')
        self.assertEqual('2000-09-30', bb.compute())

    def test_guess_whole_year_number(self):
        bb = BestBefore('09/30/2000')
        self.assertEqual('2000-09-30', bb.compute())

if __name__ == '__main__':
    unittest.main()
