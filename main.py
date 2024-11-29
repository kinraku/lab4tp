from abc import ABC, abstractmethod

# Стратегия
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array: list[int]) -> list[int]:
        pass


class BubbleSort(SortingStrategy):
    def sort(self, array: list[int]) -> list[int]:
        lst = array.copy()
        for i in range(len(lst)):
            for j in range(0, len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst


# Цепочка обязанностей
class Handler(ABC):
    def __init__(self):
        self.next_handler: Handler = None

    def set_next(self, handler: "Handler") -> "Handler":
        self.next_handler = handler
        return handler

    def handle(self, request: str) -> None:
        if self.can_handle(request):
            self.process_request(request)
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print(f"Запрос '{request}' остался необработанным.")

    @abstractmethod
    def can_handle(self, request: str) -> bool:
        pass

    @abstractmethod
    def process_request(self, request: str) -> None:
        pass


class OperatorHandler(Handler):
    def can_handle(self, request: str) -> bool:
        return request == "Простой запрос"

    def process_request(self, request: str) -> None:
        print(f"Оператор обработал запрос: {request}")


class ManagerHandler(Handler):
    def can_handle(self, request: str) -> bool:
        return request == "Средний запрос"

    def process_request(self, request: str) -> None:
        print(f"Менеджер обработал запрос: {request}")


class DirectorHandler(Handler):
    def can_handle(self, request: str) -> bool:
        return request == "Сложный запрос"

    def process_request(self, request: str) -> None:
        print(f"Директор обработал запрос: {request}")


# Итератор
class CustomCollection:
    def __init__(self, items: list[str]):
        self.items = items

    def __iter__(self) -> "CustomIterator":
        return CustomIterator(self.items)


class CustomIterator:
    def __init__(self, items: list[str]):
        self._items = items
        self._index = 0

    def __iter__(self) -> "CustomIterator":
        return self

    def __next__(self) -> str:
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


# Main функция
def main():

    # Стратегия
    print("Паттерн стратегия:")
    bubble_sort = BubbleSort()
    unsorted_array = [5, 3, 8, 4, 2]
    sorted_array = bubble_sort.sort(unsorted_array)
    print(f"Исходный массив: {unsorted_array}")
    print(f"Отсортированный массив: {sorted_array}")

    # Цепочка обязанностей
    print("\nПаттерн цепочка обязанностей:")
    operator = OperatorHandler()
    manager = ManagerHandler()
    director = DirectorHandler()
    operator.set_next(manager).set_next(director)

    operator.handle("Простой запрос")
    operator.handle("Средний запрос")
    operator.handle("Сложный запрос")
    operator.handle("Неизвестный запрос")

    # Итератор
    print("\nПаттерн итератор:")
    collection = CustomCollection(["Элемент 1", "Элемент 2", "Элемент 3"])
    for item in collection:
        print(item)


if __name__ == "__main__":
    main()
