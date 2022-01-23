import os
from Controllers import companyController
from Controllers import stateController
from flask import Flask, jsonify
from flask_cors import CORS


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
CORS(app)

app.register_blueprint(companyController.bp)
app.register_blueprint(stateController.bp)

# unrouted page
@app.route('/')
def hello():
    return 'The McHacks 22 Back End'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)