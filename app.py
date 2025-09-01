from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = ["carlos", "pedro", "jonas", "matheus", "jose", "romario"]

@app.route("/", methods=['GET'])
def home_get():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def home_post():
    Nome = request.form.get("Nome")
    existe = False
    for usuario in usuarios:
        if Nome == usuario:
            existe = True
    if existe == False:
        usuarios.append(Nome)
    p = redirect(url_for('nome_usuario', name=Nome))
    return p

@app.route("/usuarios/<name>")
def nome_usuario(name):
    existe = False
    for usuario in usuarios:
        if name == usuario:
            existe = True

    if existe:
        renderizar = render_template("usuario.html", name=name)
    else:
        renderizar = render_template("404.html")
            
    return renderizar

@app.route("/usuarios", methods=["GET"])
def usuarios_get():
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios", methods=["POST"])
def usuarios_post():
    user_name = request.form.get("user_name")
    for usuario in usuarios:
        if user_name == usuario:
            usuarios.remove(user_name)
    return redirect(url_for('usuarios_get'))

if __name__ == "__main__":
    app.run(debug=True)
