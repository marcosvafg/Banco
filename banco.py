# Importar bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

# Instanciando a app
banco = Flask(__name__)

# Configurar bd
banco.config['MYSQL_DATABASE_USER'] = 'root'
banco.config['MYSQL_DATABASE_PASSWORD'] = 'root'
banco.config['MYSQL_DATABASE_DB'] = 'banco'

# Instanciar bd
mysql = MySQL()
mysql.init_app(banco)

# Rota para /
@banco.route('/')
# Metodo para rota /
def index():
    return render_template('form_login.html')

# Rota para /login
@banco.route('/login')
#Metodo que responde /login
def login():
    # Obtendo as parametros do formulario
    cpf_cliente = request.args.get('cpf_cliente')
    senha_cliente = request.args.get('senha_cliente')

    # Criar conexao com bd e cursor
    cursor = mysql.connect().cursor()
    # Submeter o comando SQL
    cursor.execute(f'SELECT nomecliente FROM cliente where cpfcliente = {cpf_cliente} and senhacliente = {senha_cliente}')
    # Recuperar os dados
    dados = cursor.fetchone()
    mysql.connect().close()

    # Imprimir nome
    return render_template('logado.html', nome_cliente=str(dados[0]))

# Executar a app
banco.run()


