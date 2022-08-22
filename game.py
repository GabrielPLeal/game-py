from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejada [1, 2, 3 ou 4]: '))

    calcular: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calcular.mostrar_operacao()

    resultado: int = int(input())

    if calcular.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    _continuar_jogo(pontos)


def _continuar_jogo(pontos):
    resposta: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] '))
    if resposta == 0:
        print(f"Você finalizou com {pontos} ponto(s).")
        print('Até a próxima!')
    elif resposta == 1:
        jogar(pontos)
    else:
        print(f"Resposta {resposta} inxistente!")
        _continuar_jogo(pontos)


if __name__ == '__main__':
    main()
