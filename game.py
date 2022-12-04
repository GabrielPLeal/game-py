from models.calcular import Calc


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    difficulty: int = int(input('Informe o nível de dificuldade desejada [1, 2, 3 ou 4]: '))

    calc: Calc = Calc(difficulty)

    print('Informe o resultado para a seguinte operação: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'Você tem {points} ponto(s).')

    _continue_game(points)


def _continue_game(points: int) -> None:
    answer: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] '))
    if answer == 0:
        print(f"Você finalizou com {points} ponto(s).")
        print('Até a próxima!')
    elif answer == 1:
        play(points)
    else:
        print(f"Resposta {answer} inexistente!")
        _continue_game(points)


if __name__ == '__main__':
    main()
