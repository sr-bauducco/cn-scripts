#calculo numerico - bolzanno

def f(x):
    # Aqui definimos a função da Questão 4
    return x**3  - 7 * x**2 + 14 * x - 6

def bissecao(a, b, tolerancia):
    # Passo 1: Verificar se existe raiz no intervalo (Teorema de Bolzano)
    if f(a) * f(b) >= 0:
        print("Erro: A função precisa ter sinais opostos em f(a) e f(b).")
        return None

    iteracao = 1
    erro_atual = (b - a) / 2

    # Cabeçalho da nossa tabela
    print(f"{'Iteração':<10} | {'a':<10} | {'b':<10} | {'x_m (Raiz)':<12} | {'Erro'}")
    print("-" * 65)

    # Passo 2: O laço de repetição (Critério de Parada)
    while erro_atual > tolerancia:
        x_m = (a + b) / 2  # Ponto médio
        
        # Imprime os dados da iteração atual
        print(f"{iteracao:<10} | {a:<10.5f} | {b:<10.5f} | {x_m:<12.5f} | {erro_atual:.5f}")

        # Passo 3: Atualizar o intervalo
        if f(a) * f(x_m) < 0:
            b = x_m  # A raiz está na primeira metade
        else:
            a = x_m  # A raiz está na segunda metade

        # Atualiza o erro e o contador para a próxima rodada
        erro_atual = (b - a) / 2
        iteracao += 1

    # Imprime a iteração final que atende ao critério
    x_m = (a + b) / 2
    print(f"{iteracao:<10} | {a:<10.5f} | {b:<10.5f} | {x_m:<12.5f} | {erro_atual:.5f}")
    
    print("-" * 65)
    print(f"\nResultado Final: A raiz aproximada é {x_m:.5f}")
    print(f"Total de iterações realizadas: {iteracao}")

# Executando o script para o intervalo [1, 2] com precisão de 10^-4 (0.0001)
bissecao(1, 2, 0.0001)