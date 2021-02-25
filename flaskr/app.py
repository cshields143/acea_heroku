from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def root():
        return render_template('root.html', title='Blue Gold :D')
    
    return app
