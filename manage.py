# """ code modified from https://kanchanardj.medium.com/how-to-add-data-from-flask-to-postgresql-in-windows-2-77af756d017f """

# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from app import app, db
# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# if __name__ == '__main__':
#     manager.run()