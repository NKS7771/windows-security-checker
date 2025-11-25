🛡️ Windows Security Checker

Ferramenta simples em Python que realiza checagens de segurança no Windows e gera um relatório automático com informações importantes sobre o sistema.

Este projeto é ideal para mostrar conhecimento em Python, análise de segurança e boas práticas de organização.

📌 Funcionalidades

A aplicação executa automaticamente diversas verificações:

🔥 Firewall

Verifica se o firewall do Windows está ATIVO ou DESATIVADO.

🦠 Antivirus

Lista antivírus instalados no sistema (ex.: Windows Defender).

🧩 Processos Suspeitos

Verifica programas em execução.

Compara com uma lista de processos suspeitos ou desconhecidos.

🌐 Portas Abertas

Lista portas abertas e serviços associados.

📝 Geração de Relatório

Um arquivo .json é criado automaticamente em:

data/reports/security_report.json


Ele inclui todas as informações coletadas com data e hora da análise.

📁 Estrutura do Projeto
windows-security-checker/

│

├── src/

│   ├── checker.py        # Arquivo principal que coordena todas as checagens

│   ├── firewall.py       # Funções relacionadas ao firewall

│   ├── antivirus.py      # Funções que verificam antivírus instalados

│   ├── processes.py      # Verifica e lista processos suspeitos

│   ├── network.py        # Lista portas abertas e conexões

│   └── report.py         # Gera o relatório final (JSON)

│

├── data/

│   └── reports/          # Saída dos relatórios gerados

│

├── README.md             # Documentação do projeto

├── requirements.txt      # Dependências necessárias

└── .gitignore            # Arquivos e pastas ignorados pelo Git



🚀 Como Rodar o Projeto

1️⃣ Criar ambiente virtual
python -m venv .venv

2️⃣ Ativar ambiente (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Executar o Checker
python src\checker.py



📄 Exemplo de Saída (JSON)

{
  "generated_at": "2025-11-25 19:52:04",
  
  "firewall": {
      "status": "OFF"
  },
  
  "antivirus": {
      "installed": [
          "Windows Defender"
      ]
  },
  
  "processes": {
      "suspicious_processes": [
          "armourycrate.service.exe",
          "armourycrate.usersessionhelper.exe"
      ]
  },
  
  "ports": {
      "open_ports": []
  }
}


🛠️ Tecnologias Utilizadas

Python 3.11

Bibliotecas padrão (subprocess, json, datetime)

Execução de comandos do Windows (PowerShell / CMD)


🧑‍💻 Objetivo do Projeto

Criar uma ferramenta simples que:

Demonstra habilidades em Python,

Mostra entendimento de segurança da informação,

Traz boas práticas de organização e estrutura de projeto.


Perfeito para quem tem interesse em Cybersecurity.
