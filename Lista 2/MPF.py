def g(x: float) -> float:
    """Função de iteração g(x) deduzida do problema."""
    # Equivalente a raiz cúbica de (x + 1)
    return (x + 1) ** (1/3)

def metodo_ponto_fixo(x0: float, tol: float, max_iter: int = 100) -> float:
    """
    Executa o Método do Ponto Fixo.
    
    :param x0: Chute inicial.
    :param tol: Tolerância (precisão) para o critério de parada.
    :param max_iter: Número máximo de iterações permitidas (evita loops infinitos).
    """
    x_atual = x0
    print(f"Iteração 0: x = {x_atual:.5f}")
    
    for i in range(1, max_iter + 1):
        x_prox = g(x_atual)
        erro = abs(x_prox - x_atual)
        
        print(f"Iteração {i}: x = {x_prox:.5f} | Erro: {erro:.5f}")
        
        if erro < tol:
            print(f"\n=> Critério de parada satisfeito (Erro < {tol}) na iteração {i}.")
            print(f"=> Raiz aproximada: {x_prox:.5f}")
            return x_prox
            
        x_atual = x_prox
        
    print("\n=> Limite máximo de iterações atingido sem convergência.")
    return x_atual

# Parâmetros definidos pelo Exercício 2
chute_inicial = 1.0
precisao = 0.01

# Executando o algoritmo
metodo_ponto_fixo(chute_inicial, precisao)