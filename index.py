from flask import Flask, request ,render_template
import git

app = Flask(__name__)

@app.route('/RYxgOWavSXjuZRCtafAdSPQuEhNWyDxV', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./')
        origin = repo.remotes.origin
        origin.pull()
        return '', 200
    else:
        return '', 400


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)