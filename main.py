###integrate html with flask
### HTTP verb GET and Post
### jinja2 template engine 

'''
{%...%} for statements
{{ }} expression to print output
{#...#} for comments
 
'''



from flask import Flask,redirect,url_for,render_template,request

#request to read the posted values
#render lib  for html page

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/sucess/<int:score>')


def success(score):
    
    
    
    res=""
    if score>=50:
        
        res="PASS"
        
    else:
        
        res="FAIL"
        
    
    return render_template('result.html',result=res)
    
    

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

###result checker html page 

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])###name in html 
        
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['C'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
        
    res=""
    
    if total_score>=50:
        
        res="success"
        
    else:
        res="fail"
        
        
        
        
    return redirect(url_for(res,score=total_score))
        
        
        
        
        
    
    
    
if __name__=='__main__':
    
    app.run(debug=True)
    