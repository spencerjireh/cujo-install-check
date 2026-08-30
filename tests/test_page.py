from slicer import page


def test_filter_then_slice():
    assert page([1, 5, 3, 8, 9], 3, 2, 1) == [9]


def test_empty_page_past_end():
    assert page([1, 2], 0, 2, 5) == []
