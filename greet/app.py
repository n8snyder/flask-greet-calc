from flask import Flask, request

app = Flask(__name__)


@app.get("/welcome")
def welcome():
    return """
        <HTML>
            <body>
                welcome
            </body>
        </HTML>
        """


@app.get("/welcome/home")
def welcome_home():
    return """
        <HTML>
            <body>
                welcome home
            </body>
        </HTML>
        """


@app.get("/welcome/back")
def welcome_back():
    return """
        <HTML>
            <body>
                welcome back
            </body>
        </HTML>
        """
