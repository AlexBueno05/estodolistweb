from datetime import date
from flask import Flask, render_template, request, session, redirect, flash
from database import consultar_tarefas, inserir_tarefa



app = Flask(__name__)
app.secret_key = "dssenai"

ADMIN_EMAIL = "alex.bueno.senai@gmail.com"
ADMIN_SENHA = "Alex2010@bueno"

# -----------------------------------------------
# Validação
def validar_tarefa(nome, descricao, categoria, prazo, prioridade):
    erros = []
    if len(nome) < 5 or len(nome) > 30 or nome.isdigit():
        erros.append("Nome: de 5 a 30 caracteres, não só números.")
    if len(descricao) > 100:
        erros.append("Descrição: no máximo 100 caracteres.")
    if len(categoria) < 5 or len(categoria) > 30 or categoria.isdigit():
        erros.append("Categoria: de 5 a 30 caracteres, não só números.")
    if prioridade not in ("ALTA", "MEDIA", "BAIXA"):
        erros.append("Prioridade inválida.")
    # validar o prazo aqui

# -----------------------------------------------
# Rota para home
@app.route("/") # HomePage - Página Inicial
def home():
    if "login" not in session:
        return redirect ("/login")
    # Usuário logado
    tarefas = consultar_tarefas()
    return render_template("index.html", tarefas=tarefas)

# -----------------------------------------------
# Rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if "login" in session:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("login.html")

    # POST
    email = request.form.get("email") # Pegando o email que estava no form HTML
    senha = request.form.get("senha") # Está informação está no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True 
        return redirect('/') # Redireciona para a rota
    else:
        return render_template ("login.html", msgerro = "E-mail ou senha estão incorretos!")

# ------------------------------------------------
#Rota Logout
@app.route("/logout")
def logout():
    session.clear() #Apaga a lista sessão
    return redirect("/login")

# ------------------------------------------------
# Tratamento do erro - Código 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html")

# ------------------------------------------------
# Rota formulário
CATEGORIAS = ["escola", "Trabalho", "Projetos", "Pessoal", "Saúde", "Outros"]

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "GET":
        return render_template("Formulario.html", categorias=CATEGORIAS, dados={}, erros=[])

    # POST: ler o que veio do formulário
    nome_tarefa = request.form.get("nome_tarefa", "").strip()
    descricao = request.form.get("descricao", "").strip()
    categoria = request.form.get("categoria", "").strip()
    data_prazo = request.form.get("data_prazo", "")
    prioridade = request.form.get("prioridade", "")


    # validar os campos aqui

    if inserir_tarefa(nome_tarefa, descricao, categoria, data_prazo, prioridade):
        flash("Tarefa adicionada com sucesso!") 
    else:
        flash("Não foi possível salvar. Confira a conexão com o banco.")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # host="0,0,0,0" Habilita o IP Público