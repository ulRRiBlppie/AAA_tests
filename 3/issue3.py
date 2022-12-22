from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):

    def test_with_assertEqual_1(self):
        levels = ['Junior', 'Junior', 'Middle',  'Middle', 'Senior']
        exp_transformed_levels = [
            ('Junior',   [0, 0, 1]),
            ('Junior',   [0, 0, 1]),
            ('Middle', [0, 1, 0]),
            ('Middle',  [0, 1, 0]),
            ('Senior', [1, 0, 0])
        ]
        transformed_levels = fit_transform(levels)
        self.assertEqual(transformed_levels, exp_transformed_levels)

    def test_with_assertEqual_2(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_with_assertIn(self):
        """Test 3 with assertIn"""
        elements = ['fire', 'quit']
        exp_transformed_elements = [
            ('fire', [0, 1]),
            ('quit',  [1, 0]),
        ]
        transformed_elements = fit_transform(elements)
        self.assertIn(exp_transformed_elements[0], (transformed_elements[0], ))
        self.assertIn(exp_transformed_elements[1], (transformed_elements[1], ))

    def test_exception(self):
        """ Test not itarable object """
        with self.assertRaises(TypeError):
            fit_transform(123)


if __name__ == '__main__':
    unittest.main()
