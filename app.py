from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    mensagem = ""
    resultado = None

    if request.method == "POST":
        mensagem = request.form.get("mensagem", "")

        palavras_negativas = [
            "ruim",
            "péssimo",
            "pessimo",
            "erro",
            "defeito"
        ]

        tem_negativa = any(
            termo in mensagem.lower()
            for termo in palavras_negativas
        )

        if tem_negativa:
            resultado = {
                "tipo": "negativo",
                "mensagem": "🚨 Prioridade Alta: Mensagem contém termos negativos!"
            }
        else:
            resultado = {
                "tipo": "positivo",
                "mensagem": "✅ Prioridade Normal: Nenhuma palavra negativa detectada."
            }

    return render_template(
        "index.html",
        mensagem=mensagem,
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(debug=True)