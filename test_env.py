import os
from dotenv import load_dotenv

# Load the .env file from current folder
load_dotenv(dotenv_path=".env")

# Print the API key value
print("Loaded GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
