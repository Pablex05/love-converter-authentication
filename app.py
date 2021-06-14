import os
from main import create_app

# Creating Flask app instance
app = create_app()

# Loading app context
app.app_context().push()

if __name__ == '__main__':
    app.run(port=os.getenv('PORT'))
