from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')
@manager.command
@manager.shell

def make_shell_context():
    return dict(app = app,db = db,User = User )

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

manager = Manager(app)
manager.add_command('server',Server)



if __name__ == '__main__':
    manager.run()