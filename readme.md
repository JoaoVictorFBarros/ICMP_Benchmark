# Monitoramento de Latência e Perda de Pacotes

Este projeto tem como objetivo monitorar a latência e a perda de pacotes em uma rede, utilizando o protocolo ICMP. Abaixo estão as instruções e explicações sobre o funcionamento do projeto, especialmente do ponto de vista da camada de transporte de dados.

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/ICMP_Benchmark.git
```


### Instalação das Dependências

Se ainda não tiver as bibliotecas instaladas, use:

```
pip install scapy
```

### Executando o Projeto

Para iniciar o simulador, execute:

```
sudo python3 main.py
```
<div align="center">
<img src=print.png >
</div>


## Descrição

O script realiza dois testes principais:

1. **Teste de Latência:** Mede o tempo que um pacote leva para ir do cliente até o servidor e voltar.
2. **Teste de Perda de Pacotes:** Avalia a porcentagem de pacotes que não receberam resposta do servidor.

## Funcionamento

### Teste de Latência

1. **Camada de Transporte:** O teste utiliza pacotes ICMP (Internet Control Message Protocol), que operam na camada de rede do modelo OSI, logo acima da camada de transporte. Apesar de ICMP não ser um protocolo de transporte tradicional (como TCP ou UDP), ele é utilizado para diagnóstico e monitoramento.
2. **Processo:** O script executa comandos `ping` para enviar pacotes ICMP para o servidor. O tempo entre o envio e a recepção do pacote é medido para calcular a latência.
3. **Cálculo:** Para cada pacote enviado, o tempo de ida e volta é registrado e utilizado para calcular:
   - Latência Média
   - Latência Máxima
   - Latência Mínima

### Teste de Perda de Pacotes

1. **Camada de Transporte:** O teste de perda de pacotes também utiliza pacotes ICMP. Embora ICMP não ofereça garantias de entrega ou ordem, ele é útil para diagnosticar a perda de pacotes.
2. **Processo:** Pacotes ICMP são enviados ao servidor e o script conta o número de pacotes que não receberam resposta.
3. **Cálculo:** A porcentagem de pacotes perdidos é calculada dividindo o número de pacotes sem resposta pelo total de pacotes enviados.

## Configuração

1. **Configuração do Servidor:**
   - O servidor padrão é `8.8.8.8` (servidor DNS público do Google). Se o endereço fornecido não puder ser resolvido, o script usa esse IP como fallback.

2. **Configuração do Teste:**
   - `ping_count`: Número de pings realizados para medir latência e perda de pacotes.
   - `timeout`: Tempo de espera para respostas dos pacotes ICMP.

## Observações

- **ICMP e Diagnóstico:** ICMP é um protocolo usado para envio de mensagens de erro e diagnóstico na rede. Embora não forneça um controle de transporte completo (como confiabilidade e controle de fluxo), é útil para monitorar a conectividade e o desempenho da rede.
- **Permissões:** Dependendo do sistema operacional e das configurações, pode ser necessário executar o script com permissões elevadas para enviar pacotes ICMP.
