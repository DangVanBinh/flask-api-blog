from app import create_app

app = create_app()

@app.route("/")
def welcome():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)