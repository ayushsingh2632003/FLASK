from flask import Flask,redirect,url_for,request
#request to read the posted values
app=Flask(__name__)

@app.route('/')
def welcome():
    return "hii people"

@app.route('/sucess/<int:score>')


def sucess(score):
    
    return "the person has passed with "+ str(score)

@app.route('/fail/<int:score>')


def fail(score):
    
    return "the person has failed  with "+ str(score)




@app.route('/results/<int:marks>')


def results(marks):
    
    result=""
    if marks <50:
        
        result='fail'
        
    else:
        result='sucess'
        
    return redirect(url_for(result,score=marks))


def welcome():
    return "hii people"

if __name__=='__main__':
    app.run(debug=True)
    