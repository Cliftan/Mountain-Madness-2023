from Website import create_app
import "api.py"

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)