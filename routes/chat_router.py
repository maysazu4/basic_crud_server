from fastapi import APIRouter, WebSocket
import re

router = APIRouter()

# Function to filter out profanity
def filter_profanity(message):
    profane_words = ["Bullshit","Bitch","Shit","Son of a bitch","Asshole","Cow","Damn","Bastard","Fuck","Pig"] 
    for word in profane_words:
        message = re.sub(r'\b{}\b'.format(re.escape(word)), '*' * len(word), message, flags=re.IGNORECASE)
    return message



# Function to enforce message length and capitalization
def enforce_rules(message):
    # Trim message to 50 characters
    message = message[:50]
    # Capitalize first letter
    message = message.capitalize()
    return message

@router.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            # Receive message from the client
            message = await websocket.receive_text()

            # Apply filtering and rules
            message = filter_profanity(message)
            message = enforce_rules(message)

            # Send the filtered message back to the client
            await websocket.send_text(message)
        except Exception as e:
            print(e)
            break
