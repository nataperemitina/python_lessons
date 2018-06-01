from flask import Flask
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_pony import Pony

app = Flask(__name__)
app.config.from_object('shop.setting.DevConfig')

pony = Pony(app)

CSRFProtect(app)
Bootstrap(app)

from . import model
from . import views

pony.connect()
