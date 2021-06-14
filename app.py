import os
from main import create_app

# Creating Flask app instance
app = create_app()

# Loading app context
app.app_context().push()
from main import db

if __name__ == '__main__':
    db.create_all()
    app.run(port=os.getenv('PORT'))
