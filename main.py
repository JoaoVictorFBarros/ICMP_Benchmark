import os
import time
from scapy.all import sr1, IP, ICMP
import socket

# Configurações
server = '8.8.8.8'
ping_count = 10
timeout = 1

def test_latency(destination, count):
    latencies = []
    for _ in range(count):
        start_time = time.time()
        response = os.system(f"ping -c 1 {destination} > /dev/null 2>&1")
        end_time = time.time()
        if response == 0:
            latency = end_time - start_time
            latencies.append(latency)
        time.sleep(1)
    return latencies

def test_packet_loss(destination, count):
    lost_packets = 0
    for _ in range(count):
        try:
            pkt = IP(dst=destination)/ICMP()
            resp = sr1(pkt, timeout=timeout, verbose=0)
            if resp is None:
                lost_packets += 1
        except Exception as e:
            print(f"Erro durante o envio do pacote: {e}")
        time.sleep(1)
    packet_loss = (lost_packets / count) * 100
    return packet_loss

try:
    socket.gethostbyname(server)
except socket.error:
    print(f"Não foi possível resolver o endereço: {server}")
    server = '8.8.8.8'
    print(f"Usando endereço fallback: {server}")

print("Iniciando testes...")

latency_results = test_latency(server, ping_count)
if latency_results:
    avg_latency = sum(latency_results) / len(latency_results)
    max_latency = max(latency_results)
    min_latency = min(latency_results)
    print("\nResultados do teste de latência:")
    print(f"Média: {avg_latency:.4f} s")
    print(f"Máximo: {max_latency:.4f} s")
    print(f"Minimo: {min_latency:.4f} s")
else:
    print("\nNenhum resultado de latência foi obtido.")

packet_loss_percentage = test_packet_loss(server, ping_count)
print("\nResultados do teste de perda de pacotes:")
print(f"Percentual de perda de pacotes: {packet_loss_percentage:.2f}%")
