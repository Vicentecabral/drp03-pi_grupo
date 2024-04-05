import csv
import sqlite3

# Função para conectar ao banco de dados SQLite3
def conectar_bd():
    try:
        conn = sqlite3.connect('db.sqlite3')
        print('Conexão ao SQLite estabelecida.')
        return conn
    except sqlite3.Error as err:
        print(f'Erro ao conectar ao SQLite: {err}')
        return None

# Função para inserir dados do arquivo CSV no SQLite3
def inserir_dados_csv(connection, arquivo_csv, nome_tabela):
    try:
        cursor = connection.cursor()

        with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Pular cabeçalho

            for row in csvreader:
                query = f'''INSERT INTO {nome_tabela} (nome_do_livro, autor, tipo, quantidade_exemplar, saldo_exemplar, id_nicho_id, observacao_livro)
                           VALUES (?, ?, ?, ?, ?, ?, ?)'''
                cursor.execute(query, row)

        connection.commit()
        print('Dados inseridos com sucesso.')

    except sqlite3.Error as err:
        print(f'Erro ao inserir dados no SQLite: {err}')
        connection.rollback()
    finally:
        cursor.close()

# Conectar ao SQLite
connection = conectar_bd()

if connection:
    try:
        # Definir o caminho do arquivo CSV e o nome da tabela
        arquivo_csv = input('Digite o caminho do arquivo CSV: ')
        nome_tabela = 'livro'  # Nome da tabela já existente no SQLite

        # Inserir dados do arquivo CSV no SQLite
        inserir_dados_csv(connection, arquivo_csv, nome_tabela)

    except:
        print('Ocorreu um erro durante a execução do script.')

    finally:
        # Fechar conexão com o SQLite
        connection.close()
        print('Conexão ao SQLite fechada.')
else:
    print('Não foi possível estabelecer conexão com o SQLite.')
