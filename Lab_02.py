class House:
    color: str
    window_count: int

    def __init__(self, color: str, window_count: int) -> None:
        self.color = color
        self.window_count = window_count

    def get_color(self) -> str:
        return f'elewacja budynku jest koloru: {self.color}'

    def add_windows(self, amout: int) -> None:
        self.window_count += amout

    def __privte_method(self) -> None: # Pojedynczy _ protective
        print('dasdas')


house_1 = House('blue', 10)
house_2 = House('green', 8)
house_1.__private_method()

print(f'dom nr 1 ma {house_1.window_count} okien')
print(f'dom nr 2 ma {house_2.window_count} okien')

house_2.add_windows(3)
print(f'dom nr 1 ma {house_1.window_count} okien')
print(f'dom nr 2 ma {house_2.window_count} okien')

print(house_1.get_color())
print(house_2.get_color())

house_1.color = 'afroamerican'
print(house_1.get_color())
print(house_2.get_color())
