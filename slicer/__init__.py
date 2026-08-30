"""Page a list after filtering it."""


def page(items: list[int], minimum: int, size: int, number: int) -> list[int]:
    """Return page `number` (0-based) of `size` items at or above `minimum`."""
    start = number * size
    window = items[start : start + size]
    return [i for i in window if i >= minimum]
