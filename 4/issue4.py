from one_hot_encoder import fit_transform
import pytest


def test_with_assertEqual_levels():
    levels = ['Junior', 'Junior', 'Middle',  'Middle', 'Senior']
    exp_transformed_levels = [
            ('Junior',   [0, 0, 1]),
            ('Junior',   [0, 0, 1]),
            ('Middle', [0, 1, 0]),
            ('Middle',  [0, 1, 0]),
            ('Senior', [1, 0, 0])
        ]
    transformed_levels = fit_transform(levels)
    assert exp_transformed_levels == transformed_levels


def test_with_assertEqual_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert transformed_cities == exp_transformed_cities


def test_type_error_callable():
    with pytest.raises(TypeError):
        fit_transform(123)


def test_type_error_empty():
    with pytest.raises(TypeError):
        fit_transform()
