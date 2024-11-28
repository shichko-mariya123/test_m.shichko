import pytest

from oop_task.engine.engine2d import Engine2D
from oop_task.tests.conftest import parametrize_shapes


@pytest.mark.parametrize("color", ["red", "blue", "green", "yellow"])
def test_engine_set_color(color):
    engine = Engine2D()
    engine.set_color(color)
    assert engine.current_color == color


@parametrize_shapes()
def test_engine_add_shape(test_data, shape_key, shape_class):
    engine = Engine2D()
    data = test_data[shape_key]
    shape = shape_class(**data["params"])
    engine.add_shape(shape)
    assert len(engine.canvas) == 1
    assert engine.canvas[0] == shape
    assert shape.color == "black"


@parametrize_shapes()
def test_engine_draw_output(test_data, shape_key, shape_class, capfd):
    engine = Engine2D()
    data = test_data[shape_key]
    engine.set_color(data["color"])
    shape = shape_class(**data["params"])
    shape.set_color(data["color"])
    engine.add_shape(shape)
    engine.draw()
    captured = capfd.readouterr()
    assert data["expected_message"] in captured.out


@parametrize_shapes()
def test_engine_draw(test_data, shape_key, shape_class, capfd):
    engine = Engine2D()
    data = test_data[shape_key]
    engine.set_color(data["color"])
    shape = shape_class(**data["params"])
    shape.set_color(data["color"])
    engine.add_shape(shape)
    engine.draw()
    captured = capfd.readouterr()
    assert data["expected_message"] in captured.out
    assert len(engine.canvas) == 0


def test_engine_draw_empty_canvas(capfd):
    engine = Engine2D()
    engine.draw()
    captured = capfd.readouterr()
    assert captured.out == ""
