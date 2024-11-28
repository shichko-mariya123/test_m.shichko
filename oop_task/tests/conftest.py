import pytest

from oop_task.engine.shapes.circle import Circle
from oop_task.engine.shapes.rectangle import Rectangle
from oop_task.engine.shapes.triangle import Triangle
from oop_task.utils.json_util import load_data_from_json


@pytest.fixture
def test_data():
    return load_data_from_json("test_data.json")


def parametrize_shapes():
    parameters = [
        ("circle", Circle),
        ("rectangle", Rectangle),
        ("triangle", Triangle)
    ]
    def decorator(test_func):
        return pytest.mark.parametrize("shape_key, shape_class", parameters)(test_func)
    return decorator
