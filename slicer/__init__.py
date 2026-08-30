"""Page a list after filtering it."""


def page(items: list[int], minimum: int, size: int, number: int) -> list[int]:
    """Return page `number` (0-based) of `size` items at or above `minimum`."""
    kept = [i for i in items if i >= minimum]
    start = number * size
    return kept[start : start + size]
