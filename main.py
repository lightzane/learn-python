# x: str = 1

# def add_numbers(a: int, b: int, c: int) -> int:
#     return a + b + c

# add_numbers('1', '2', '3')

from typing import List, Optional, Callable

x: List[List[int]] = []
y: dict[str, str] = {'a': 'b'}

def foo(output: Optional[bool]=False):
    pass

def bar(output: bool=False):
    pass

z: tuple[int, int, int] = (1, 2, 3)

def fu(x: int, y: int) -> int:
    return x + y

def kung(func: Callable[[int, int], int]) -> None:
    func(1, 2)

kung(fu)

from typing import TypeVar

T = TypeVar('T')

def get_items(arr_list: list[T], index: int) -> T:
    return arr_list[index]

lemon = get_items(['lemon', 'orange'], 0)
print(lemon)

mixed = get_items(['lemon', 1, True], 2)
print(mixed)