from flask import Flask, request
app = Flask(__name__)

#http://127.0.0.1:5000/nota/1?nota_1=5&nota_2=0&nota_3=1
@app.route('/nota/1')
def teste_query_string_1_argumento_get():
    nota_1 = float (request.args.get('nota_1'))
    nota_2 = float (request.args.get('nota_2'))
    nota_3 = float (request.args.get('nota_3'))
    media = (nota_1 + nota_2 + nota_3) / 3

    if media >= 0 and media < 3:
        return '<h1> Reprovado </h1>'
        

    elif media >= 3 and media < 7:
        return '<h1> EXAME </h1>'
    
    else:
        return '<h1> APROVADO </h1>'    
   
    
if __name__ == '__main__':
     #executa o app no modo debug (default) na porta 5000 (default):
    app.run(debug= True, port=5000)

    