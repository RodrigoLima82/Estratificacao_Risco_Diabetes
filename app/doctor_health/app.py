from flask import Flask, jsonify
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def home():
   return 'hello world'   

profissional = [
    {
        'id': 1,
        'nome': u'Rodrigo',
        'cargo': u'Cientista de Dados', 
        'idade': 38
    },
    {
        'id': 2,
        'nome': u'Amanda',
        'cargo': u'Estudante', 
        'idade': 18
    }
]

@app.route('/api', methods=['GET'])
def api_profissionais():
    return jsonify({'profissional': profissional}) 

if __name__ == '__main__':
    app.run()