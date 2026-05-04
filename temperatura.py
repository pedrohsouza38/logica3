import time
import random

# Monitor de Temperatura de Servidor

# Configurações do sistema
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

# Executar o monitor
if __name__ == "__main__":
    try:
        monitorar_servidor()
    except KeyboardInterrupt:
        # Permite encerrar o programa com Ctrl+C de forma limpa
        print("\nMonitor encerrado pelo usuário.")