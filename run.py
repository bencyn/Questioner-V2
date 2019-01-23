from app import create_app

config_name= 'development'
app = create_app(config_name)
@app.route('/')
def index():
    return "Hello there! Welcome to questioner"

if __name__ == "__main__":
    app.run(debug=True)
    
