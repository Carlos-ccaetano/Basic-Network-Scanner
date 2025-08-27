# Scanner de Rede Básico

Este é um script Python simples que atua como um scanner de portas básico, verificando se portas comuns estão abertas em um host alvo. Ele utiliza a biblioteca `socket` para tentar estabelecer conexões com as portas especificadas e reporta o status (aberta/fechada). Os resultados podem ser exportados para um arquivo JSON.

## Funcionalidades

- Escaneia um conjunto predefinido de portas comuns (FTP, SSH, HTTP, HTTPS, etc.).
- Identifica se uma porta está aberta ou fechada.
- Exporta os resultados do escaneamento para um arquivo JSON para fácil análise e integração.

## Como Usar

1. **Pré-requisitos:**
   Certifique-se de ter o Python 3 instalado em seu sistema. Nenhuma biblioteca externa é necessária além das bibliotecas padrão do Python.

2. **Execução:**
   Navegue até o diretório `scanner_rede` no seu terminal e execute o script:
   ```bash
   python3 port_scanner.py
   ```

3. **Interação:**
   O script solicitará o host alvo a ser escaneado (ex: `google.com` ou `192.168.1.1`). Após o escaneamento, ele perguntará se você deseja exportar os resultados para `scan_results.json`.

## Exemplo de Uso

```
Digite o host a ser escaneado (ex: google.com, 192.168.1.1): example.com
Escaneando portas comuns em example.com...
  Porta 20 (FTP Data): Fechada
  Porta 21 (FTP Control): Fechada
  Porta 22 (SSH): Fechada
  Porta 23 (Telnet): Fechada
  Porta 25 (SMTP): Fechada
  Porta 53 (DNS): Aberta
  Porta 80 (HTTP): Aberta
  Porta 110 (POP3): Fechada
  Porta 135 (MSRPC): Fechada
  Porta 139 (NetBIOS Session Service): Fechada
  Porta 143 (IMAP): Fechada
  Porta 443 (HTTPS): Aberta
  Porta 445 (SMB): Fechada
  Porta 3389 (RDP): Fechada
  Porta 8080 (HTTP Proxy): Fechada
Exportar resultados para 'scan_results.json'? (s/n, padrão: s): s
Resultados exportados para scan_results.json
```

## Estrutura do Projeto

```
.|
├── port_scanner.py
└── README.md
```

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Abra uma issue ou envie um pull request.


