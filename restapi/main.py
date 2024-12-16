from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/armstrong/<int:n>')
def check_armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit * digit * digit
        temp = temp//10
    
    if sum==n:
        result={
            "Number":n,
            "Armstrong":True,
            "IP":"190.168.22.1"
        }
        return jsonify(result)
    else:
        result={
            "Number":n,
            "Armstrong":False,
            "IP":"190.168.22.1"
        }
        return jsonify(result)
        
if __name__=="__main__":
    app.run(debug=True)