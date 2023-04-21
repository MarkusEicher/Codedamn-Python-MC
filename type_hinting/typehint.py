txt = "AnyText"

txt: str = "AnyTextHinted"

num : int | float = 5.0

lst: list[int] = [1, 2, 3]
lst2: list[str] = ["a", "b", "c"]

tpl: tuple[int, int, int] = (1, 2, 3)
tpl2: tuple[str, str, str] = ("a", "b", "c")

contacts: dict[str, int] = {"Dale": 123}


def root(num: int|float) -> int:
    return pow(num, .5)

root_25 = root(25)
