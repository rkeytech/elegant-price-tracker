import string
from app import add_element


def test_can_add_element_in_list():
    testing_list: list[string] = add_element("my testing")
    assert len(testing_list) == 1
