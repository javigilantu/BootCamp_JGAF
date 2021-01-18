from flask import Flask, request, render_template
from utils.functions import read_json
import json, os

# Mandatory
app = Flask(__name__) # __name__ --> __main__( si ejecuto desde el terminal) o el nombre del fichero( si no ejecutas desde el main)

# ---------- Flask functions ----------
@app.route("/")  # @--> estas cosas se llaman decoradores
def home():
    """ Default path """
    return app.send_static_file('greet.html')

@app.route("/greet")  # capacidad para ejecutar archivos HTML
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/c_json")
def create_json():
    return '{"clave":"valor", "clave_2":3}'

@app.route('/give_me_id', methods=['GET']) # esta necesita que se le de info
def give_id():
    x = request.args['id']
    return request.args
#?id=6 el 6 no es necesario ( ? nombre de la variable = valor de la variable)
# & (añadiendo el & puedes meter más variables )
# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(os.path.dirname(os.getcwd()))
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    settings_file = os.path.dirname(__file__) + os.sep +"settings.json"
    # Load json from file 
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")

if __name__ == "__main__":
    main()