

def average(poop, *numbers : float | int) -> float | int:
    """Calculate the average of the given numbers."""
    return sum(numbers) / len(numbers)