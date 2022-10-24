from flask import Flask, request
app = Flask(__name__)

# http://http://127.0.0.1:5000/temperatura/1?temperatura=90
@app.route('/temperatura/1')
def teste_query_string_1_argumento_get():
    temperatura = float (request.args.get('temperatura'))
    faherenheit = (temperatura * 1.8) + 32
    return '''<h1>Temperatura informada em graus Celsius: {}</h1>
    <h1>Temperatura informada em graus faherenheit: {}</h1>'''.format(temperatura,faherenheit)
    

if __name__ == '__main__':
    #executa o app no modo debug (default) na porta 5000 (default):
    app.run(debug= True, port=5000)