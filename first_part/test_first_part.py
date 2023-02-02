from first_part.src import *
import unittest

test1_output = "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n11\nThree\n13\n14\nThreeFive\n16\n17\nThree\n19\nFive\nThree\n22\n23\nThree\nFive\n26\nThree\n28\n29\nThreeFive\n31\n32\nThree\n34\nFive\nThree\n37\n38\nThree\nFive\n41\nThree\n43\n44\nThreeFive\n46\n47\nThree\n49\nFive\nThree\n52\n53\nThree\nFive\n56\nThree\n58\n59\nThreeFive\n61\n62\nThree\n64\nFive\nThree\n67\n68\nThree\nFive\n71\nThree\n73\n74\nThreeFive\n76\n77\nThree\n79\nFive\nThree\n82\n83\nThree\nFive\n86\nThree\n88\n89\nThreeFive\n91\n92\nThree\n94\nFive\nThree\n97\n98\nThree\nFive\n"

def test_first_exercise(capsys):
    exercise_one()
    captured = capsys.readouterr()
    assert captured.out == test1_output

class TestCalculateAndColurful(unittest.TestCase):
    def test_calculate_case1(self):
        result = 5
        self.assertEqual(result,calculate(['4', '3', '-2']))
        result = 9
        self.assertEqual(result, calculate(['nothing', 3, '8', 2, '1']))

    def test_calculate_case2(self):
        result = False
        self.assertEqual(result,calculate(453))
        self.assertEqual(result,calculate('54'))

    def test_is_colorful(self):
        self.assertTrue(is_colorful(263))
        self.assertFalse(is_colorful(236))
        self.assertFalse(is_colorful(2532))


if __name__ == '__main__':
    unittest.main()