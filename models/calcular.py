from random import randint


class Calc:

    def __init__(self, difficulty: int, /) -> None:
        self.__difficulty: int = difficulty
        self.__value_1: int = self._make_value
        self.__value_2: int = self._make_value
        self.__operation: int = randint(1, 3)
        self.__result: int = self._make_result

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @property
    def value_1(self) -> int:
        return self.__value_1

    @property
    def value_2(self) -> int:
        return self.__value_2

    @property
    def operation(self) -> int:
        return self.__operation

    @property
    def result(self) -> int:
        return self.__result

    def __str__(self) -> str:
        operation: str = 'Operação desconhecida'
        if self.operation == 1:
            operation = 'Somar'
        elif self.operation == 2:
            operation = 'Diminuir'
        elif self.operation == 3:
            operation = 'Multiplicar'
        return (
            f"Valor 1: {self.value_1} \n"
            f"Valor 2: {self.value_2} \n"
            f"Difficuldade: {self.difficulty} \n"
            f"Operação: {operation}"
        )

    @property
    def _make_value(self) -> int:
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        elif self.difficulty == 4:
            return randint(0, 10000)
        return randint(0, 100000)

    @property
    def _make_result(self) -> int:
        if self.operation == 1:
            return self.value_1 + self.value_2
        elif self.operation == 2:
            return self.value_1 - self.value_2
        return self.value_1 * self.value_2

    @property
    def _symbol_operation(self) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        return 'x'

    def check_result(self, resposta: int) -> bool:
        certo: bool = False

        if self.result == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.value_1} {self._symbol_operation} {self.value_2} = {self.result}')
        return certo

    def show_operation(self) -> None:
        print(f'{self.value_1} {self._symbol_operation} {self.value_2} = ?')
