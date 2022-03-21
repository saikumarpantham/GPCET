from flask import Flask

app=Flask(__name__)

@app.route('/')
def homePage():
    return('Hello GPCET-AI')

if(__name__=="__main__"):
    app.run()