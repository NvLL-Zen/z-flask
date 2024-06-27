from flask import Flask, request ,render_template
import git

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def update_server():
    if request.method == 'POST':
        repo = git.Repo('path/to/git_repo')
        origin = repo.remotes.origin
        origin.pull()

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)