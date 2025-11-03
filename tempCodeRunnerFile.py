MODEL = os.getenv("MODEL", "llama3-8b-instant")
# PORT = int(os.getenv("PORT", 5000))
# MEMORY_TURNS = int(os.getenv("MEMORY_TURNS", 6))

# # --- Flask Setup ---
# app = Flask(__name__)
# CORS(app)

# # --- Emotional AI system instruction ---
# SYSTEM_PROMPT = (
#     "You are 'Aura', a compassionate, non-judgmental emotional support AI designed to listen actively, "
#     "validate feelings, and offer gentle, supportive perspectives. Your primary goal is to provide a safe "
#     "space for the user to express themselves. Use encouraging and warm language. Avoid giving direct "
#     "commands or medical advice. Focus on reflective listening, positive reframing, and confirming "
#     "understanding. Keep your responses concise, empathetic, and end with an open question."
# )

# # --- Chat Memory ---
# conversation_history = []


# # --- Groq API Call ---
# def call_groq_api(messages):
#     """
#     Sends messages to Groq's chat completion API.
#     """
#     url = "https://api.groq.com/openai/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json",
#     }

#     data = {
#         "model": MODEL,
#         "messages": messages,
#         "temperature": 0.8,
#         "max_tokens": 400,
#     }

#     try:
#         response = requests.post(url, headers=headers, json=data, timeout=60)
#         response.raise_for_status()
#         result = response.json()
#         return result["choices"][0]["message"]["content"]
#     except requests.exceptions.RequestException as e:
#         return f"[ERROR] API request failed: {e}"
#     except Exception as e:
#         return f"[ERROR] Unexpected issue: {e}"


# # --- API Endpoint for Chat ---
# @app.route('/chat', methods=['POST'])
# def chat():
#     global conversation_history
#     data = request.json
#     user_message = data.get("message", "").strip()

#     if not user_message:
#         return jsonify({"text": "Hey there, how are you feeling today?"})

#     # Add user message to memory
#     conversation_history.append({"role": "user", "content": user_message})
#     if len(conversation_history) > MEMORY_TURNS * 2:
#         conversation_history = conversation_history[-MEMORY_TURNS * 2:]

#     # Build messages payload for Groq
#     messages = [{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history

#     # Get AI response
#     ai_text = call_groq_api(messages)

#     # Add AI message to memory
#     conversation_history.append({"role": "assistant", "content": ai_text})

#     return jsonify({"text": ai_text})


# # --- Serve index.html (Frontend) ---
# @app.route('/')
# def index():
#     return render_template('index.html')


# # --- Run the app ---
# if __name__ == '__main__':
#     if not GROQ_API_KEY:
#         raise ValueError("❌ GROQ_API_KEY not found! Please set it in your .env file.")
#     app.run(debug=True, host='0.0.0.0', port=PORT)
