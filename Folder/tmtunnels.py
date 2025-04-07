from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# Data in-memory untuk contoh
expected_token = 'minacantik'

@auth.verify_token
def verify_token(token):
    if token == expected_token:
        return token

@app.route('/')
def home():
    return jsonify(message="TMTunnels")

@app.route('/api/stats', methods=['GET'])
@auth.login_required
# make run bash and return output
def stats():
    import subprocess
    cmd = f'stats'
    try:
        outputsc = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
        return jsonify(message="Error")
    else:
        return outputsc
    


@app.route('/api/data', methods=['GET'])
@auth.login_required
def get_data():
    return jsonify(data_store)


@app.route('/api/createssh', methods=['POST'])
@auth.login_required
def create_ssh():
    import subprocess
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    exp = data.get('exp')
    limitip = data.get('limitip')
    
    if not username or not password or not exp or not limitip:
        return jsonify(message="Invalid data")
    

    cmd = f'tmtunnel create ssh {exp} {username} {password} {limitip}'
    try:
        outputsc = subprocess.check_output(cmd, shell=True).decode("utf-8")
        outputsc = outputsc.replace('[H[2J[3J', '')
    except:
        return jsonify(message="Error")
    else:
        return outputsc
    
@app.route('/api/createvmess', methods=['POST'])
@auth.login_required
def create_vmess():
    import subprocess
    data = request.get_json()
    username = data.get('username')
    exp = data.get('exp')
    limitip = data.get('limitip')
    limitbw = data.get('limitbw')
    
    if not username or not limitbw or not exp or not limitip:
        return jsonify(message="Invalid data")
    

    cmd = f'tmtunnel create vmess {exp} {username} {limitbw} {limitip}'
    try:
        outputsc = subprocess.check_output(cmd, shell=True).decode("utf-8")
        outputsc = outputsc.replace('[H[2J[3J', '')
    except:
        return jsonify(message="Error")
    else:
        return outputsc

@app.route('/api/createvless', methods=['POST'])
@auth.login_required
def create_vless():
    import subprocess
    data = request.get_json()
    username = data.get('username')
    exp = data.get('exp')
    limitip = data.get('limitip')
    limitbw = data.get('limitbw')
    
    if not username or not limitbw or not exp or not limitip:
        return jsonify(message="Invalid data")
    

    cmd = f'tmtunnel create vless {exp} {username} {limitbw} {limitip}'
    try:
        outputsc = subprocess.check_output(cmd, shell=True).decode("utf-8")
        outputsc = outputsc.replace('[H[2J[3J', '')
    except:
        return jsonify(message="Error")
    else:
        return outputsc
@app.route('/api/createtrojan', methods=['POST'])
@auth.login_required
def create_trojan():
    import subprocess
    data = request.get_json()
    username = data.get('username')
    exp = data.get('exp')
    limitip = data.get('limitip')
    limitbw = data.get('limitbw')
    
    if not username or not limitbw or not exp or not limitip:
        return jsonify(message="Invalid data")
    

    cmd = f'tmtunnel create trojan {exp} {username} {limitbw} {limitip}'
    try:
        outputsc = subprocess.check_output(cmd, shell=True).decode("utf-8")
        outputsc = outputsc.replace('[H[2J[3J', '')
    except:
        return jsonify(message="Error")
    else:
        return outputsc
    
@app.route('/api/deletexray', methods=['DELETE'])
@auth.login_required
def delete_vmess():
    import subprocess
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify(message="Invalid data")
    
    cmd = f'tmtunnel delete xray makan {username}'
    try:
        outputsc = subprocess.check_output(cmd, shell=True).decode("utf-8")
        outputsc = outputsc.replace('[H[2J[3J', '')
    except:
        return jsonify(message="Error")
    else:
        return outputsc
    
    
    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
