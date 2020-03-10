from flask import Flask, escape, request
app = Flask('clase5pr')
@app.route('/')
def suma():
    valor1 = int (request.args.get("valor1", 0))
    valor2 = int (request.args.get("valor2", 0))
    return 'Sumatoria, {}!'.format(valor1 + valor2)
