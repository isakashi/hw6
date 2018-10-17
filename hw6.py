import re
import unittest

def sumNums(fileName):
    f = open(fileName, 'r')
    file = f.readlines()
    file.close

    sum = 0

    one = re.findall(r'1', file)
    two = re.findall(r'2', file)
    three = re.findall(r'3', file)
    four = re.findall(r'4', file)
    five = re.findall(r'5', file)
    six = re.findall(r'6', file)
    seven = re.findall(r'7', file)
    eight = re.findall(r'8', file)
    nine = re.findall(r'9', file)



def countWord(fileName, word):
    
    count = 0

    while fileName:
        if word.upper() in fileName.upper():
            if 


def listURLs(fileName):
    pass



class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
