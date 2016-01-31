from flask import Flask
app_clp = Flask(__name__)

@app_clp.route('/hello_clp')
def hello_world_clp():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    return 'Hello World!'

if __name__ == '__main__':
    app_clp.run(debug=True)
