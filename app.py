from flask import Flask, request, jsonify
from datetime import datetime
import json
import config
import blockchain
from common import return_msg

patient = config.mock_data

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    data = json.loads(request.get_data())
    user_name = data['user_name']
    password = data['password']
    if not config.user_data.get(user_name):
        return return_msg('201', 'user not found')
    elif config.user_data[user_name] == password:
        return return_msg('200', 'success')
    else:
        return return_msg('202', 'username or password error')


@app.route("/patient/add", methods=['POST'])
def patient_add():
    data = json.loads(request.get_data())
    print(data['id'])
    # data = request.form['data']
    res = blockchain.set(json.dumps(data))
    return return_msg(res['ccCode'], data=res['ccData'])


@app.route("/patient/update", methods=['POST'])
def patient_update():
    data = json.loads(request.get_data())
    # data = request.form['data']
    res = blockchain.update(json.dumps(data))
    return return_msg(res['ccCode'], data=res['ccData'])


@app.route("/patient/delete", methods=['POST'])
def patient_delete():
    data = json.loads(request.get_data())
    patient_id = data['patient_id']
    res = blockchain.delete(patient_id)
    return return_msg(res['ccCode'], data=res['ccData'])


@app.route("/patient/get", methods=['POST'])
def patient_get():
    data = json.loads(request.get_data())
    patient_id = data['patient_id']
    res = blockchain.get(patient_id)
    return return_msg(res['ccCode'], data=json.loads(res['ccData']))


@app.route("/case/update", methods=['POST'])
def case_add():
    data = json.loads(request.get_data())
    patient_id = data['patient_id']
    case_data = data['data']
    print(data)
    patient = json.loads(blockchain.get(patient_id)['ccData'])
    time_list = [case['time'] for case in patient['caseList']]
    if case_data['time'] in time_list:
        patient['caseList'][time_list.index(case_data['time'])] = case_data
    else:
        patient['caseList'].append(case_data)
    res = blockchain.update(json.dumps(patient))
    return return_msg(res['ccCode'], data=res['ccData'])


@app.route("/case/delete", methods=['POST'])
def case_delete():
    data = json.loads(request.get_data())
    patient_id = data['patient_id']
    case_data = data['data']
    patient = json.loads(blockchain.get(patient_id)['ccData'])
    time_list = [case['time'] for case in patient['caseList']]
    if case_data['time'] in time_list:
        patient['caseList'].pop(time_list.index(case_data['time']))
    res = blockchain.update(json.dumps(patient))
    return return_msg(res['ccCode'], data=res['ccData'])


@app.route("/case/get", methods=['POST'])
def case_get():
    data = json.loads(request.get_data())
    patient_id = data['patient_id']
    patient = json.loads(blockchain.get(patient_id)['ccData'])
    return return_msg('200', data=patient['caseList'])


if __name__ == '__main__':
    if config.env == 'dev':
        app.run(host='127.0.0.1', port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', port=5000, debug=False)

