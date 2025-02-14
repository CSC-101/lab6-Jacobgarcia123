import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        input1 = data.Book(['Patti Smith', ''], 'Just Kids')
        input2 = data.Book(['Toni Morrison', ''], 'The Bluest Eye')
        input3 = data.Book(['Rick Rubin', ''], 'The Creative Act')
        input = [input1,input2,input3]
        expected = ['Just Kids','The Bluest Eye','The Creative Act']
        actual = lab6.selection_sort_books(input)
        self.assertEqual(expected, actual)
    def test_selection_sort_books_1(self):
        input1 = data.Book(['', ''], 'x')
        input2 = data.Book(['', ''], 'a')
        input3 = data.Book(['', ''], 'd')
        input = [input1,input2,input3]
        expected = ['a','d','x']
        actual = lab6.selection_sort_books(input)
        self.assertEqual(expected, actual)



    # Part 2
    def test_swap_case_1(self):
        input = 'HeLLo wOrLd'
        expected = 'hEllO WoRlD'
        actual = lab6.swap_case(input)
        self.assertEqual(expected, actual)
    def test_swap_case_2(self):
        input = 'goodbye WORLD'
        expected = 'GOODBYE world'
        actual = lab6.swap_case(input)
        self.assertEqual(expected, actual)


    # Part 3
    def test_str_translate_1(self):
        input = 'hello world'
        input2 = 'l'
        input3 = 'x'
        expected = 'hexxo worxd'
        actual = lab6.str_translate(input,input2,input3)
        self.assertEqual(expected, actual)
    def test_str_translate_2(self):
        input = 'aaacccdadadppp'
        input2 = 'a'
        input3 = 'r'
        expected = 'rrrcccdrdrdppp'
        actual = lab6.str_translate(input,input2,input3)
        self.assertEqual(expected, actual)


    # Part 4
    def test_histogram_1(self):
        input = 'helloworld helloworld computer ok computer'
        expected = {'helloworld': 2, 'computer':2, 'ok': 1}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)
    def test_histogram_2(self):
        input = 'apple apple apple '
        expected = {'apple':3}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)






if __name__ == '__main__':
    unittest.main()
