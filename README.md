# logica3
Exercícios de Lógica com Python 3

1. Validador de Complexidade de Senha

Garantir que uma senha tenha o comprimento mínimo e caracteres especiais.
Regras:
1. Comprimento mínimo: 8 caracteres;
2. Um caracter maiúsculo;
3. Um caracter minúsculo;
4. Um caracter especial;
5. Um número;

Lógica: Percorrer a string caractere por caractere para validar critérios.
Resultado Esperado: "Senha forte" ou lista de requisitos ausentes.

def validar_senha(senha):
    #Variáveis de controle (flags) para cada critério
    comprimento_ok = len(senha) >= 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    #Conjunto de caracteres especiais para comparação
    especiais = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|"

    #Estrutura de Repetição: Percorre cada caractere da string individualmente
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in especiais:
            tem_especial = True

    #Lista para armazenar o que falta na senha
    erros = []
    
    #Estruturas de Decisão: Verificam quais flags permaneceram False
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

    #Retorno do resultado baseado na lista de erros
    if not erros:
        return "Senha forte"
    else:
        return "Senha fraca. Requisitos ausentes: " + ", ".join(erros)

   #Teste do programa
    senha_usuario = input("Digite sua senha para validar: ")
    resultado = validar_senha(senha_usuario)
    print(resultado)

Justificativa das Estruturas Utilizadas

Estrutura de Repetição (for char in senha):

Por que usar: É a forma mais direta de "inspecionar" o conteúdo da senha. Como precisamos validar diferentes tipos de caracteres (números, letras, símbolos), percorrer a string um por um permite classificar cada item sem precisar de múltiplas varreduras ou funções complexas de busca.

Estruturas de Decisão (if, elif, else):

Dentro do loop: O if/elif serve como um "filtro". Para cada caractere, o programa pergunta: "Você é maiúsculo? Não? Então é número?". Isso evita processamento desnecessário, pois se um caractere já foi identificado como letra, o programa não precisa testar se ele é um número.

Após o loop: O if not é utilizado para verificar quais critérios de segurança não foram satisfeitos. É a forma mais lógica de transformar estados booleanos (True/False) em mensagens legíveis para o usuário final.

2. Monitor de Temperatura de Servidor
Monitorar um valor constante e agir caso ultrapasse o limite.

Lógica: Implementar um loop que "escuta" um sensor (valor manual) até que o sistema seja desligado.

Regra: Temperatura limite do servidor: 80 °C

Resultado Esperado: Alerta de "Resfriamento ativado".

import time
import random

   #Monitor de Temperatura de Servidor

   #Configurações do sistema
TEMPERATURA_LIMITE = 80  # °C
INTERVALO_LEITURA = 2    # segundos entre leituras

def ler_sensor_temperatura():
    """
    Simula a leitura de um sensor de temperatura.
    Em um cenário real, aqui ficaria o código para ler o hardware.
    """
    # Gera uma temperatura aleatória entre 60 e 95 para simular variações
    return random.randint(60, 95)

def monitorar_servidor():
    print("--- Iniciando Monitor de Temperatura do Servidor ---")
    print(f"Limite definido: {TEMPERATURA_LIMITE}°C\n")

    # ESTRUTURA DE REPETIÇÃO (Loop Infinito)
    # Justificativa: O monitoramento de servidor precisa ser contínuo (24/7).
    # O loop 'while True' garante que o programa não finalize após a primeira leitura,
    # "escutando" o sensor continuamente até que o processo seja interrompido manualmente.
    while True:
        temperatura_atual = ler_sensor_temperatura()
        print(f"Temperatura atual: {temperatura_atual}°C")

        # ESTRUTURA DE DECISÃO (if/else)
        # Justificativa: Necessária para avaliar a temperatura atual contra o limite.
        # Se a temperatura exceder, executa a ação de alerta (if).
        # Caso contrário, o sistema continua operando normalmente (else).
        if temperatura_atual > TEMPERATURA_LIMITE:
            print(f"ALERTA: Temperatura alta ({temperatura_atual}°C)! Resfriamento ativado.")
        else:
            print("Status: Operando dentro da temperatura segura.")

        print("-" * 30)
        
        # Pausa a execução para não sobrecarregar o processador
        time.sleep(INTERVALO_LEITURA)

#Executar o monitor
if __name__ == "__main__":
    try:
        monitorar_servidor()
    except KeyboardInterrupt:
        # Permite encerrar o programa com Ctrl+C de forma limpa
        print("\nMonitor encerrado pelo usuário.")

Justificativa das Estruturas Utilizadas

Estrutura de Repetição (while True):

Por que usar: Um monitor de hardware não pode rodar apenas uma vez e fechar. Ele precisa monitorar o tempo todo. O while True cria um loop infinito que mantém o programa rodando, permitindo que a função ler_sensor_temperatura() seja chamada repetidamente.

Estrutura de Decisão (if / else):

Por que usar: O sistema precisa agir de forma condicional. A regra de negócio é clara: se a temperatura ultrapassar 80°C, resfriar; senão, continuar normalmente. O if verifica essa condição crítica.

Simulação (random e time.sleep):

random.randint é usado para simular o comportamento do sensor sem precisar de hardware físico.

time.sleep é crucial para pausar o loop por alguns segundos, impedindo que o programa consuma 100% da CPU fazendo leituras frenéticas.
