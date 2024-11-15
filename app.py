from flask import Flask, render_template, request, jsonify
from src.chatbot import DarazChatbot
from src.logger import logging
from src.exception import CustomException
import sys

# Initialize Flask app with template folder configuration
app = Flask(__name__, template_folder='src/frantend')

# Initialize logger
logger = logging.getLogger()

# Initialize the chatbot
chatbot = DarazChatbot()

@app.route('/')
def index():
    """Render the homepage with the chatbot."""
    try:
        # Render the index.html template from the correct directory
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering template: {e}")
        return jsonify({"error": "Failed to render the homepage."}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """Receive user input and return the chatbot's response."""
    try:
        user_input = request.json.get('user_input')
        if not user_input:
            raise CustomException("User input is empty", sys)
        
        # Get chatbot response
        response = chatbot.get_response(user_input)
        return jsonify({"response": response})

    except CustomException as ce:
        logger.error(f"CustomException: {ce}")
        return jsonify({"error": str(ce)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
