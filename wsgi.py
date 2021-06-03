from app import create_app

app = create_app('config.Config')

if __name__ == "__main__":
    app.run(host="127.0.0.1:5000", debug=True)
