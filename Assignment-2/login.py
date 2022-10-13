from flask import Flask,session,render_template,request,redirect,url_for

app=Flask(__name__)

app.secret_key='asdsdfsdfs13sdf_df%&'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/')
def index():
    login=False
    if 'username' in session:
        login=True
    return render_template('login_home.html',login=login)

if __name__=='__main__':
    app.run(debug=True)