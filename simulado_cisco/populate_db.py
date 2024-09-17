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
