from flask import Flask


def create_app():
    #make the app?? (initializing the app or flask...?)
    app = Flask(__name__)

    #set-up a config key (this is supposed to be a secret in actual web apps)
    #look for how it is done in actual practice
    app.config['SECRET_KEY'] = 'akuandsushi'


    #export blueprint 
    from website.views import views
    from website.auth import auth


    #register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    



    return app

