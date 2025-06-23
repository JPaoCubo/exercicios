# Entrada de dados
numero = int(input("Digite um número inteiro: "))

# Remove o dígito das unidades com divisão inteira por 10
numero_sem_unidade = numero // 10

# Pega o dígito das dezenas com o operador de módulo
digito_das_dezenas = numero_sem_unidade % 10

# Saída de dados
print(f"O dígito das dezenas é {digito_das_dezenas}")
