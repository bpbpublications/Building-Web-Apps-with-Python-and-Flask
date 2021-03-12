from flask import Flask, render_template
##app=Flask(__name__)
##from Institution.engg.routes import engg
##from Institution.mngmnt.routes import mngmnt
##app.register_blueprint(engg, url_prefix='/engineering')
##app.register_blueprint(mngmnt, url_prefix='/management')

def create_app():
    app=Flask(__name__)
    with app.app_context():
        from HiTech.engg.routes import engg
        from HiTech.mngmnt.routes import mngmnt
        app.register_blueprint(engg, url_prefix='/engineering')
        app.register_blueprint(mngmnt, url_prefix='/management')
        return app


##@app.route('/')
##def index():
##    return render_template('index.html')
