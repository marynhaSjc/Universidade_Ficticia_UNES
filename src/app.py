from flask import Flask, render_template #Importa classe Flask   /*redirect, url_for: NÃO USANDOS

app = Flask(__name__) #Cria uma instância dessa classe

@app.route("/") # criando rotas com decorator chamado @app.route("rota") / é o raíz 
def home(): # função para retornar uma mensagem
    return render_template("index.html")

@app.route("/index.html") # não deve ser exibido o html no navegador. Deixei para lembrete! Se alterar aqui, precisa altera href no HTML.
def home_clicada():
    return render_template("index.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

