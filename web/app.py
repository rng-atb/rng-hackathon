from flask import Flask, render_template, request, Response
from pusher import Pusher

app = Flask(__name__)

# configure pusher object
pusher = Pusher(
app_id='944644',
key='f16ea1258675470a8b10',
secret='dd03e17c2a4bafe9c9ac',
cluster='us3',
ssl=True)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/our_endpoint', methods=['GET'])
def our_endpoint():
    some_arg = request.args.get("some_arg")
    if some_arg is None:
        print("arg some_arg was None")
        return Response(status=400)
    if some_arg == "option1":
        return Response(status=200)        
    else:
        return Response(status=200)

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/orders', methods=['POST'])
def order():
    data = request.form
    pusher.trigger(u'order', u'place', {
        u'units': data['units']
    })
    return "units logged"

@app.route('/message', methods=['POST'])
def message():
    data = request.form
    pusher.trigger(u'message', u'send', {
        u'name': data['name'],
        u'message': data['message']
    })
    return "message sent"

@app.route('/customer', methods=['POST'])
def customer():
    data = request.form
    pusher.trigger(u'customer', u'add', {
        u'name': data['name'],
        u'position': data['position'],
        u'office': data['office'],
        u'age': data['age'],
        u'salary': data['salary'],
    })
    return "customer added"

if __name__ == '__main__':
    app.run(debug=True)