
# Simulado Cisco

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📝 Descrição

**Simulado Cisco** é uma aplicação web interativa desenvolvida para ajudar estudantes e profissionais a treinarem seus conhecimentos sobre a configuração de roteadores Cisco via Interface de Linha de Comando (CLI). Utilizando **FastAPI** para o backend, **Jinja2** para templates, **SQLite** para armazenamento de dados e **JavaScript** para interatividade, este sistema permite que os usuários respondam a perguntas de múltipla escolha, visualizem seus resultados e acompanhem seu progresso através de gráficos de desempenho.

## 🎯 Funcionalidades

- **Simulado de Perguntas de Múltipla Escolha**: Responda a perguntas relacionadas à configuração de roteadores Cisco.
- **Feedback Detalhado**: Veja quais respostas você acertou ou errou e onde pode melhorar.
- **Histórico de Pontuação**: Acompanhe seu desempenho ao longo do tempo com gráficos interativos.
- **Interface Intuitiva**: Navegação fácil e responsiva para uma melhor experiência do usuário.

## 🛠 Tecnologias Utilizadas

- **Backend**:
  - [FastAPI](https://fastapi.tiangolo.com/) - Framework moderno e rápido para APIs.
  - [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para interação com o banco de dados.
  - [SQLite](https://www.sqlite.org/index.html) - Banco de dados relacional leve.
- **Frontend**:
  - [Jinja2](https://jinja.palletsprojects.com/) - Motor de templates para renderização de HTML.
  - [Chart.js](https://www.chartjs.org/docs/latest/) - Biblioteca JavaScript para criação de gráficos.
  - **HTML/CSS** - Estrutura e estilo das páginas.
  - **JavaScript** - Interatividade e lógica de navegação.
- **Outras Ferramentas**:
  - [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI para execução da aplicação.
  - [Python](https://www.python.org/) 3.12

## 📁 Estrutura do Projeto

```
simulado_cisco/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── question.html
│   │   └── result.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
├── populate_db.py
├── questions.db
├── requirements.txt
└── README.md
```

## 🚀 Começando

### 🔧 Pré-requisitos

Certifique-se de ter instalado em sua máquina as seguintes ferramentas:

- [Python 3.12](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/)

### 📦 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/simulado_cisco.git
   cd simulado_cisco
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Popule o banco de dados com as perguntas:**

   ```bash
   python populate_db.py
   ```

   **Nota:** Este script cria o banco de dados `questions.db` e insere as perguntas de múltipla escolha.

### 📄 Uso

1. **Inicie o servidor FastAPI:**

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Acesse a aplicação:**

   Abra seu navegador e vá para [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. **Inicie o Simulado:**

   - Clique em "Iniciar Simulado" na página inicial.
   - Responda às perguntas de múltipla escolha apresentadas.
   - Ao finalizar, veja sua pontuação, feedback detalhado e um gráfico com seu desempenho histórico.

## 🛠️ Refatoração do `populate_db.py`

O script `populate_db.py` foi refatorado para utilizar uma abordagem **síncrona** com SQLAlchemy, garantindo compatibilidade e simplicidade durante a população do banco de dados.

### 📄 Código Refatorado

```python
# populate_db.py
from sqlalchemy import insert
from app.database import engine, metadata
from app.models import questions
from sqlalchemy.orm import sessionmaker

def populate():
    # Cria as tabelas no banco de dados
    metadata.create_all(engine)
    
    # Lista completa de perguntas de múltipla escolha
    questions_list = [
        {
            "question": "Qual é o prompt que indica que o roteador está no Modo Usuário?",
            "option_a": "roteador#",
            "option_b": "roteador(config)#",
            "option_c": "roteador>",
            "option_d": "roteador(interfaces)#",
            "correct_option": "C"
        },
        {
            "question": "Qual comando é usado para entrar no Modo Privilegiado a partir do Modo Usuário?",
            "option_a": "configure terminal",
            "option_b": "enable",
            "option_c": "disable",
            "option_d": "exit",
            "correct_option": "B"
        },
        {
            "question": "No Modo Privilegiado, qual comando permite entrar no Modo de Configuração Global?",
            "option_a": "conf t",
            "option_b": "config global",
            "option_c": "enable secret",
            "option_d": "hostname",
            "correct_option": "A"
        },
        {
            "question": "Qual comando salva a configuração atual do roteador na NVRAM?",
            "option_a": "copy startup-config running-config",
            "option_b": "write memory",
            "option_c": "copy running-config startup-config",
            "option_d": "save config",
            "correct_option": "C"
        },
        {
            "question": "Para definir o nome do roteador, qual comando deve ser utilizado no Modo Global?",
            "option_a": "set hostname",
            "option_b": "hostname",
            "option_c": "name",
            "option_d": "set name",
            "correct_option": "B"
        },
        {
            "question": "Qual comando no Modo de Configuração de Interface desabilita a interface?",
            "option_a": "disable",
            "option_b": "shutdown",
            "option_c": "no enable",
            "option_d": "down",
            "correct_option": "B"
        },
        {
            "question": "No Modo de Configuração Global, como você define uma rota estática para a rede 192.168.0.0/24 via o próximo salto 172.16.1.1?",
            "option_a": "ip route 192.168.0.0 255.255.255.0 172.16.1.1",
            "option_b": "route add 192.168.0.0/24 via 172.16.1.1",
            "option_c": "set ip route 192.168.0.0 172.16.1.1",
            "option_d": "ip static-route 192.168.0.0 172.16.1.1",
            "correct_option": "A"
        },
        {
            "question": "Qual comando exibe a tabela de roteamento do roteador?",
            "option_a": "show ip route",
            "option_b": "show routes",
            "option_c": "display routes",
            "option_d": "show routing",
            "correct_option": "A"
        },
        {
            "question": "Para configurar o endereço IP 5.5.5.5 com máscara 255.255.255.0 em uma interface, qual comando é utilizado?",
            "option_a": "set ip 5.5.5.5/24",
            "option_b": "ip address 5.5.5.5 255.255.255.0",
            "option_c": "configure ip 5.5.5.5 mask 255.255.255.0",
            "option_d": "assign ip 5.5.5.5/255.255.255.0",
            "correct_option": "B"
        },
        {
            "question": "Qual comando permite visualizar os últimos comandos digitados no roteador?",
            "option_a": "show commands",
            "option_b": "show history",
            "option_c": "display history",
            "option_d": "show log",
            "correct_option": "B"
        },
    ]
    
    # Cria uma sessão para interagir com o banco de dados
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Insere cada pergunta na tabela
        for q in questions_list:
            stmt = insert(questions).values(
                question=q['question'],
                option_a=q['option_a'],
                option_b=q['option_b'],
                option_c=q['option_c'],
                option_d=q['option_d'],
                correct_option=q['correct_option']
            )
            session.execute(stmt)
        
        # Confirma as transações
        session.commit()
        print("Banco de dados populado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu um erro: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    populate()
```

### 📌 Observações

- **Compatibilidade**: Este script foi refatorado para utilizar SQLAlchemy de forma síncrona, resolvendo o erro relacionado ao uso do contexto assíncrono com conexões síncronas.
- **Adicionar Mais Perguntas**: Para adicionar mais perguntas, simplesmente expanda a lista `questions_list` com novos dicionários seguindo o mesmo formato.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.

1. Fork o projeto
2. Crie sua branch de feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📫 Contato

Seu Nome - [@seu_usuario_twitter](https://twitter.com/seu_usuario_twitter) - seu.email@example.com

Projeto Link: [https://github.com/seu-usuario/simulado_cisco](https://github.com/seu-usuario/simulado_cisco)

## 🎉 Agradecimentos

- Agradecemos à comunidade do [FastAPI](https://fastapi.tiangolo.com/) e [SQLAlchemy](https://www.sqlalchemy.org/) pelo excelente suporte e documentação.
- Inspirado por necessidades de treinamento em redes e configuração de roteadores Cisco.
