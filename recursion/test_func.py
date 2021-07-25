import unittest
from func import getNthFib, sum, reverseOrder, duplicateZero
from smallestval import smallestVal

class TestFibonaci(unittest.TestCase):
    
    def test_getNthFib(self):
        self.assertEqual(getNthFib(2), 1)
        self.assertEqual(getNthFib(6), 5)


    def test_sum(self):
        self.assertEqual(sum(2), 3)
        self.assertEqual(sum(6), 21)    

    
    def test_reverseOrder(self):
        self.assertEqual(reverseOrder("hello"), "olleh")
        self.assertEqual(reverseOrder("nischal"), "lahcsin")
        self.assertEqual(reverseOrder("nischal rana"), "anar lahcsin")

    def test_duplicateZero(self):
        self.assertEqual(duplicateZero([1,0,2,3,0,4,5,0]), [1,0,0,2,3,0,0,4])
        self.assertEqual(duplicateZero([1,0,2,0,3,4]), [1,0,0,2,0,0])
        self.assertEqual(duplicateZero([1,2,3]), [1,2,3])


    def test_smallestVal(self):
        self.assertEqual(smallestVal([1, 4, 45, 6, -50, 10, 2]), -50) 
          


if __name__ == '__main__':
    unittest.main()

