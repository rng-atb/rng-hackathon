from flask import Flask, render_template, request, Response
# from pusher import Pusher
import pandas
import json
import os, sys
#first change the cwd to the script path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../common")

#import your module stored in '../common'
from ..populate.back_end import Profile

# global prof

app = Flask(__name__)

# # configure pusher object
# pusher = Pusher(
# app_id='944644',
# key='f16ea1258675470a8b10',
# secret='dd03e17c2a4bafe9c9ac',
# cluster='us3',
# ssl=True)

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

@app.route('/graph', methods=['GET'])
def graph():
    path = request.args.get("filepath")
    print("the path is: {0}".format(path))
    return render_template('graph.html', data_path=path)

@app.route('/populate')
def populate():
    profile = Profile()
    profile.populateProfile()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    csv_file = "tmp.csv"
    print(dir_path)
    # dir_path = dir_path + "/static/data/tmp.csv"
    profile.writeToCsv(dir_path + "/static/data/" + csv_file)
    return render_template('jsongraph.html', data_path="data/"+csv_file)    # 
    # df = profile.getProfile()
    # print(df)
    # print(type(df))
    # # df = df.__str__()
    # df = json.dumps(df)
    # print(type(df)) 
    # print(df)
    # print("\n\n")   
    # # df = json.loads(df.__str__())
    # # print(type(df))
    # df = pandas.read_json(df)
    # print(df)
    # df = df.to_csv()
    # print(df)
    # print(type(df))
    # lines = df.splitlines()
    # correct_csv = ""
    # for line in lines:
    #     # print("line: {}".format(line))
    #     # print("\t{}".format( line[line.index(",")+1:]))
    #     correct_csv += line[line.index(",")+1:] + "\n"
    # print(correct_csv)
    # # keep_col = ["source", "target", "weight"]
    # # df = df[keep_col]
    # # print(df)
    # # print(profile.getProfile())
    
    # return render_template('jsongraph.html', data=correct_csv)
    # global prof
    # print(prof)
    #profile = Profile()
    #profile.populateProfile()
    #profile.writeToCsv("data.csv")
    #profile.createReport()
    #profile.writeToFile("profiles.json")
    #print(profile.getInterestedProfiles("Learning", 7))

@app.route('/demo1')
def demo1():
    return render_template('graph.html', data_path="data/account.csv")

@app.route('/demo2')
def demo2():
    return render_template('graph.html', data_path="data/account.json")

@app.route('/demo3')
def demo3():
    return render_template('graph.html', data_path="data/force.csv")

@app.route('/demo4')
def demo4():
    return render_template('graph.html', data_path="data/data.csv")

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/orders', methods=['POST'])
# def order():
#     data = request.form
#     pusher.trigger(u'order', u'place', {
#         u'units': data['units']
#     })
#     return "units logged"

# @app.route('/message', methods=['POST'])
# def message():
#     data = request.form
#     pusher.trigger(u'message', u'send', {
#         u'name': data['name'],
#         u'message': data['message']
#     })
#     return "message sent"

# @app.route('/customer', methods=['POST'])
# def customer():
#     data = request.form
#     pusher.trigger(u'customer', u'add', {
#         u'name': data['name'],
#         u'position': data['position'],
#         u'office': data['office'],
#         u'age': data['age'],
#         u'salary': data['salary'],
#     })
#     return "customer added"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # global prof
    