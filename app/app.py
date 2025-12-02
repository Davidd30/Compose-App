from flask import Flask
import os

# Initialize the Flask application
app = Flask(__name__)

# Read the environment variable set by Docker Compose
FLASK_ENV = os.getenv('FLASK_ENV', 'production')

# The root route handler
@app.route('/')
def home():
    """
    Handles requests to the root path and returns a welcome message.
    It also displays the current FLASK_ENV setting for verification.
    """
    message = (
        f"<h1>Hello from the Containerized Flask App!</h1>"
        f"<p>The application is running successfully on port 5000.</p>"
        f"<p>Current Environment: <strong>{FLASK_ENV}</strong></p>"
        f"<p>This code is volume-mounted for easy development.</p>"
    )
    return message

# Run the app if the script is executed directly
# We run it on '0.0.0.0' to make it accessible outside the container's localhost.
if __name__ == '__main__':
    # Set host to '0.0.0.0' to bind to all interfaces
    # The port is 5000 as required.
    app.run(host='0.0.0.0', port=5000)
