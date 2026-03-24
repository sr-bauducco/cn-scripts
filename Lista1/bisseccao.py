#calculo numerico - bolzanno

def f(x):
    
    return x**3  - 7 * x**2 + 14 * x - 6

def bissecao(a, b, tolerancia):

    if f(a) * f(b) >= 0:
        print("Erro: A função precisa ter sinais opostos em f(a) e f(b).")
        return None

    iteracao = 1
    erro_atual = (b - a) / 2

    
    print(f"{'Iteração':<10} | {'a':<10} | {'b':<10} | {'x_m (Raiz)':<12} | {'Erro'}")
    print("-" * 65)


    while erro_atual > tolerancia:
        x_m = (a + b) / 2 
        

        print(f"{iteracao:<10} | {a:<10.5f} | {b:<10.5f} | {x_m:<12.5f} | {erro_atual:.5f}")

  
        if f(a) * f(x_m) < 0:
            b = x_m  
        else:
            a = x_m  

        erro_atual = (b - a) / 2
        iteracao += 1

    x_m = (a + b) / 2
    print(f"{iteracao:<10} | {a:<10.5f} | {b:<10.5f} | {x_m:<12.5f} | {erro_atual:.5f}")
    
    print("-" * 65)
    print(f"\nResultado Final: A raiz aproximada é {x_m:.5f}")
    print(f"Total de iterações realizadas: {iteracao}")

bissecao(1, 2, 0.0001)