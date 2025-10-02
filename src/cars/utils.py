def average(*numbers: float) -> float | int:
    """Calculate the average of the given numbers."""
    return sum(numbers) / len(numbers)
