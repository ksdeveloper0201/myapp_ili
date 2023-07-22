from flask import Flask
from app_factory import create_app
from flaskr.routes.world import bp

app = create_app()

if __name__ == "__main__":
    app.run()
