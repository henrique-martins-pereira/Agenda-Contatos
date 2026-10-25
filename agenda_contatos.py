import sqlite3

conn = sqlite3.connect ('Agenda.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS agenda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL
)
''')

conn.commit()

def adicionar_contato():
    print("ADICIONAR CONTATO")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cursor.execute("INSERT INTO agenda (nome, telefone) VALUES (?,?)", (nome, telefone))
    conn.commit()
    print("Contato salvo com sucesso!")

def ver_contatos():
    print("VER CONTATOS")
    cursor.execute("SELECT * FROM agenda")
    contatos = cursor.fetchall()
    if len(contatos) == 0:
        print("Nenhum contato salvo!")
    else:
        for contato in contatos:
            print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]}")

def deletar_contato():
    print("DELETAR CONTATO")
    print("Aviso: As ações aqui não poderão ser restauradas")
    cursor.execute("SELECT * FROM agenda")
    contatos = cursor.fetchall()

    if len(contatos) == 0:
        print("Nenhum contato salvo!")
    else:
        for contato in contatos:
            print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]}")

    id = int(input("ID: "))
    cursor.execute("DELETE FROM agenda WHERE id = ?", (id,))
    conn.commit()
    print("Contato excluido com sucesso!")

def atualizar_telefone():
    print("ATUALIZAR TELEFONE")
    print("Aviso: As ações aqui não poderão ser restauradas")

    cursor.execute("SELECT * FROM agenda")
    contatos = cursor.fetchall()

    if len(contatos) == 0:
        print("Nenhum contato salvo!")
    else:
        for contato in contatos:
            print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]}")

    id = int(input("ID: "))
    telefone = input("Telefone: ")

    cursor.execute("UPDATE agenda SET telefone = ? WHERE id = ?", (telefone, id))
    conn.commit()
    print("Contato atualizado com sucesso!")


print("AGENDA DE CONTATOS")
while True:
    print("-"*20)
    print("""
1. Adicionar Contato
2. Ver Contato
3. Deletar Contato
4. Atualizar Contato
5. SAIR
""")
    opcao = int(input("Escolha o número da opção: "))
    if opcao == 1:
        print("-"*20)
        adicionar_contato()
    elif opcao == 2:
        print("-"*20)
        ver_contatos()
    elif opcao == 3:
        print("-"*20)
        deletar_contato()
    elif opcao == 4:
        print("-"*20)
        atualizar_telefone()
    elif opcao == 5:
        print("-"*20)
        print("Saindo...")
        break
    else:
        print("-"*20)
        print("Opção inválida!")