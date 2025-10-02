

from typing import Tuple
from src.cars.utils import average

x : Tuple[Tuple[float | int, ...], ...] = (
    (1, 2, 3),
    (4, 5, 6),
    (3, 3, 3)
)

for y in x:
    print(average(*y))
