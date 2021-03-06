from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def root():
        return render_template('root.html', title='Blue Gold :D')
    
    @app.route('/overview')
    def about():
        return render_template('about.html', title='Project Overview - Blue Gold')
    
    @app.route('/cleaning')
    def imput():
        return render_template('imput.html', title='Cleaning & Imputation - Blue Gold')
    
    @app.route('/ml')
    def machine():
        return 'hello, world'
    
    @app.route('/water-budget')
    def rpeg():
        return 'hello, world'
    
    @app.route('/retro')
    def alldone():
        return 'hello, world'
    
    return app
