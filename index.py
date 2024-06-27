from flask import Flask, request ,render_template
import git
import hmac
import hashlib

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def update_server():
    if request.method == 'POST':
        repo = git.Repo('/home/Zenriel/z-flask/')
        origin = repo.remotes.origin
        origin.pull()
        return 'Access Granted', 200

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)