import unittest
from Quiz import QuizInput, MathOperator, QuizCalc


class TestMathGame(unittest.TestCase):

    def test_QuizInput(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = QuizInput(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)


    def test_MathOperator(self):
        # Test if MathOperator returns one of the expected operators
        for _ in range(1000):  # Test a large number of random values
            operator = MathOperator()

            self.assertIn(operator, ['+', '-', '*'])

    def test_QuizCalc(self):
        # Test if QuizCalc returns the correct question and answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = QuizCalc(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
