

# parser
from datetime import timedelta

from app import create_app


app = create_app('settings')


@app.before_request
def before_request():
    # db_session.begin()
    # session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)


# @app.teardown_request
# def teardown_request(exception):
#     try:
#         try:
#             db_session.commit()
#         except Exception as e:
#             db_session.rollback()
#     except exc.SQLAlchemyError as Ex:
#         print("SQLAlchemyError : %s" % Ex)
#         db_session.rollback()
#     finally:
#         db_session.remove()


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
#     db_session.close()


if __name__ == '__main__':
    # app = DebuggedApplication(app, evalex=True)
    app.debug = True
    app.run(host='0.0.0.0', port='5000')