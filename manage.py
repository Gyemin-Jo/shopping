# parser
from werkzeug.debug import DebuggedApplication

from app import create_app

app = create_app()

from users import views, models

if __name__ == '__main__':
    # app = DebuggedApplication(app, evalex=True)
    app.debug = True
    app.run(host='127.0.0.1', port='5000')
