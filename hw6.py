import re
import unittest

def sumNums(fileName):
    
    f = open(fileName, 'r')
    line = f.readline()

    numbers = []
    
    while line:

        number_count = re.findall(r"[0-9]+", line)

        numbers.extend(number_count)

        line = f.readline()

    
    add = 0
    for num in numbers:
        add += int(num)

    f.close()
    return add

def countWord(fileName, word):
    
    f = open(fileName, 'r')
    line = f.readline()

    count = 0
    
    while line:
        lowerFile = line.lower()

        word_accurance = re.findall(r"\b" + word + r"\b", lowerFile)

        count += len(word_accurance)

        line = f.readline()

    f.close()

    return count


def listURLs(fileName):
    
    f = open(fileName, 'r')
    line = f.readline()

    linkList = []

    while line:

        link = re.findall(r"\bwww.[a-z0-9]+.[a-z].[a-z0-9]+.\b", line)

        linkList += link

        line = f.readline()

    f.close()

    print(linkList)

    return linkList


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
