app.config['SECRET_KEY'] = 'secret value'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH_CREDENTIALS'] = {
   'facebook': {
       'id': '143303334215278',
       'secret': 'eca5d89aed8b90604734d412ae76b485'
   }
}