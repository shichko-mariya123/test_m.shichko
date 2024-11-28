from oop_task.tests.conftest import parametrize_shapes


@parametrize_shapes()
def test_shape_initialization(test_data, shape_key, shape_class):
    data = test_data[shape_key]
    shape = shape_class(**data["params"])
    for key, value in data["params"].items():
        assert getattr(shape, key) == value
    assert shape.color is None


@parametrize_shapes()
def test_shape_set_color(test_data, shape_key, shape_class):
    data = test_data[shape_key]
    shape = shape_class(**data["params"])
    shape.set_color(data["color"])
    assert shape.color == data["color"]


@parametrize_shapes()
def test_shape_draw(test_data, shape_key, shape_class, capfd):
    data = test_data[shape_key]
    shape = shape_class(**data["params"])
    shape.set_color(data["color"])
    shape.draw()
    captured = capfd.readouterr()
    assert data["expected_message"] in captured.out
