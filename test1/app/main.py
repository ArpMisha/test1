from app import app
import view 
from kks.blueprint import kks

app.register_blueprint(kks)

if __name__ == '__main__':
	app.run(host = '0.0.0.0')

