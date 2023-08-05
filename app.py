from flask import Flask

# Create a simple flask application
app = Flask(__name__)


# Making URL dynamic
@app.route('/')
def welcome():
    
    return "hello guys"





if __name__ == '__main__':
    
    app.run(debug=True)
