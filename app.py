from flask import Flask
from views import views

#__name__ is just the name of the module 
app = Flask(__name__)
app.register_blueprint(views, url_prefrix="/")

if __name__ == '__main__':
  app.run(debug=True, port=8000)

  