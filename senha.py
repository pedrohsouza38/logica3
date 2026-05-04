def validar_senha(senha):
    # Variáveis de controle (flags) para cada critério
    comprimento_ok = len(senha) >= 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    # Conjunto de caracteres especiais para comparação
    especiais = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|"

    # Estrutura de Repetição: Percorre cada caractere da string individualmente
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in especiais:
            tem_especial = True

    # Lista para armazenar o que falta na senha
    erros = []
    
    # Estruturas de Decisão: Verificam quais flags permaneceram False
    if not comprimento_ok:
        erros.append("Mínimo de 8 caracteres")
    if not tem_maiuscula:
        erros.append("Pelo menos uma letra maiúscula")
    if not tem_minuscula:
        erros.append("Pelo menos uma letra minúscula")
    if not tem_numero:
        erros.append("Pelo menos um número")
    if not tem_especial:
        erros.append("Pelo menos um caractere especial")

    # Retorno do resultado baseado na lista de erros
    if not erros:
        return "Senha forte"
    else:
        return "Senha fraca. Requisitos ausentes: " + ", ".join(erros)

# Teste do programa
senha_usuario = input("Digite sua senha para validar: ")
resultado = validar_senha(senha_usuario)
print(resultado)