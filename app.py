from flask import Flask
from users.user_route import users_bp
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app)
app.register_blueprint(users_bp)


if __name__ == '__main__':
    app.run(port = 5000)

