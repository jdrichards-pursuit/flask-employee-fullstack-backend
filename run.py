from app import create_app
from dotenv import load_dotenv

import os


load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_RUN_PORT', 8080)),
        debug=os.getenv('FLASK_ENV') == 'development'
    )
