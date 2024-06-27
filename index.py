from flask import Flask, request ,render_template
import git

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook received")
    if request.method == 'POST':
        try:
            repo = git.Repo('/home/yourusername/yourproject')  # Replace with your project path
            origin = repo.remotes.origin
            origin.pull()
            print("Repository updated successfully")
            return '', 200
        except Exception as e:
            print(f"Error: {e}")
            return '', 500
    else:
        return '', 400


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)