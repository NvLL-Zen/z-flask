from flask import Flask, request, Response, abort ,render_template
from json import dumps
import git
import hmac
import hashlib

def is_valid_signature(x_hub_signature, data, private_key):
    # x_hub_signature and data are from the webhook payload
    # private key is your webhook secret
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def update_server():
    if request.method == 'POST':
        x_hub_signature = request.headers.get('X-Hub-Signature')
        if not is_valid_signature(x_hub_signature, request.data, "MULUTANDAKONTOL"):
            error_message = dumps({'Message': 'YOU SHALL NOT PASS!!!'})
            abort(Response(error_message, 401))
        repo = git.Repo('/home/Zenriel/z-flask/')
        origin = repo.remotes.origin
        origin.pull()
        return 200

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)