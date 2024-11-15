import sys
from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from .exception import CustomException
from .logger import logging


# Initialize logger
logger = logging.getLogger()

class DarazChatbot:
    def __init__(self, model_name="llama3.2"):
        # Initialize the Ollama model
        try:
            self.llm = Ollama(model=model_name)
            logger.info(f"Successfully initialized the model: {model_name}")
        except Exception as e:
            logger.error(f"Error initializing the model: {e}")
            raise CustomException(f"Error initializing the model: {e}", sys)

        # Create a memory buffer to maintain the context of the conversation
        self.memory = ConversationBufferMemory()

        # Define the prompt template to include `history`
        self.template = """
        You are an AI chatbot for the website "https://www.daraz.pk," Pakistan's leading e-commerce platform.
        Your job is to help users with:
        1. Product searches and recommendations.
        2. Order tracking and related issues.
        3. Website troubleshooting (login, payment, etc.).
        4. Customer support (returns, refunds, complaints, etc.).

        The conversation history is as follows:
        {history}

        User: {input}
        Chatbot:
        """
        
        # Create the conversation prompt with memory and template
        self.prompt = PromptTemplate(input_variables=["history", "input"], template=self.template)
        self.chatbot = ConversationChain(llm=self.llm, memory=self.memory, prompt=self.prompt)

    def get_response(self, user_input: str) -> str:
        """Get the response from the chatbot"""
        try:
            if not user_input:
                raise CustomException("User input cannot be empty.", sys)
            
            response = self.chatbot.run(input=user_input)
            logger.info(f"User input: {user_input}, Response: {response}")
            return response

        except CustomException as ce:
            logger.error(f"CustomException occurred: {ce}")
            return f"Error: {ce}"

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise CustomException(str(e), sys)

    def chat(self):
        """Simulate a conversation with the chatbot."""
        print("Welcome to the Daraz Chatbot! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Thank you for using Daraz support! Have a great day!")
                logger.info("Chat ended.")
                break

            response = self.get_response(user_input)
            print(f"Chatbot: {response}")
            logger.info(f"Response sent: {response}")

# Entry point for the chatbot to interact
if __name__ == "__main__":
    try:
        chatbot = DarazChatbot()
        chatbot.chat()
    except CustomException as e:
        print(f"Error: {e}")
        logger.error(f"Error: {e}")
