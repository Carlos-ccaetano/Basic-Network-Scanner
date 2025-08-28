# 🔍 Scanner de Rede Básico

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/status-concluído-green)
![Security](https://img.shields.io/badge/category-network--scanner-red)

---

## 📖 Descrição
Este é um script em **Python** que atua como um scanner de portas básico, verificando se portas comuns estão abertas em um host alvo.  
Ele utiliza a biblioteca padrão `socket` para tentar estabelecer conexões com as portas especificadas e reporta o status (aberta/fechada).  
Os resultados podem ser exportados para um arquivo JSON para fácil análise e integração.

---

## ⚙️ Funcionalidades
- ✅ Escaneia um conjunto predefinido de portas comuns (FTP, SSH, HTTP, HTTPS, etc.).  
- ✅ Identifica se uma porta está aberta ou fechada.  
- ✅ Exporta os resultados para JSON (`scan_results.json`).  

---

## 🚀 Como Usar

### 🔹 Pré-requisitos
- Python 3.11+ instalado.  
- Nenhuma biblioteca externa é necessária além da biblioteca padrão.

### 🔹 Execução
Navegue até o diretório do projeto e execute o script:

```bash
python3 port_scanner.py
```

### 🔹 Interação
- O script solicitará o **host alvo** (ex: `google.com` ou `192.168.1.1`).  
- Após o escaneamento, ele perguntará se você deseja exportar os resultados para `scan_results.json`.  

---

## 📸 Exemplo de Uso
```bash
Digite o host a ser escaneado (ex: google.com, 192.168.1.1): example.com
Escaneando portas comuns em example.com...

  Porta 20 (FTP Data): Fechada
  Porta 21 (FTP Control): Fechada
  Porta 22 (SSH): Fechada
  Porta 53 (DNS): Aberta
  Porta 80 (HTTP): Aberta
  Porta 443 (HTTPS): Aberta
  Porta 445 (SMB): Fechada
  Porta 3389 (RDP): Fechada

Exportar resultados para 'scan_results.json'? (s/n, padrão: s): s
Resultados exportados para scan_results.json
```

---

## 📂 Estrutura do Projeto
```
.|
├── port_scanner.py   # Código-fonte do scanner
└── README.md         # Documentação
```

---

## 🧠 Aprendizados
- Como utilizar a biblioteca `socket` em Python para conexões TCP.  
- Funcionamento básico de portas de rede e protocolos comuns.  
- Exportação de dados em formato **JSON** para integração.  

---

## 📌 Próximas atualizações:
*(No momento estou envolvido em outros projetos e pesquisas acadêmicas, por isso ainda não finalizei todas as melhorias. Mas seguem algumas ideias futuras — e claro, contribuições são bem-vindas!)*
- [ ] Adicionar range de portas personalizável.  
- [ ] Implementar **multithreading** para aumentar a velocidade.  
- [ ] Suporte a exportação também em CSV.  

---

## 🤝 Contribuições
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades.  
Abra uma **issue** ou envie um **pull request**.

---
## 👤 Autor
**Carlos Caetano**  
🔗 [LinkedIn](https://linkedin.com/in/SEU_LINKEDIN) | 💻 [GitHub](https://github.com/Carlos-ccaetano)  

---



