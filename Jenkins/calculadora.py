import sys

def multiplicar(a, b):
    """
    Multiplica dos números y retorna el resultado.
    
    Args:
        a: Primer número
        b: Segundo número
        
    Returns:
        float: El resultado de la multiplicación
    """
    return float(a) * float(b)

def main():
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py <numero1> <numero2>")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        resultado = multiplicar(num1, num2)
        print(f"El resultado de {num1} * {num2} = {resultado}")
    except ValueError:
        print("Error: Por favor ingrese números válidos")
        sys.exit(1)

if __name__ == "__main__":
    main() 