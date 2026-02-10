from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask on EKS!"

if __name__ == "__main__":
    # חשוב: host=0.0.0.0 כדי שזה יעבוד בתוך Docker / Kubernetes
    app.run(host="0.0.0.0", port=5000)

