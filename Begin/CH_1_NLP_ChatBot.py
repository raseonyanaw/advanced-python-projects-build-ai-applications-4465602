# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob
#Define intents
intents = {
    "hours":{
        "keywords":["hours","open","close"],
        "response": "We are open from 9AM to %PM, Monday to Friday"
    },
    "returns":{
        "keywords":["refund","money back","return"],
        "response":"I'd be happy to help you with the return process. Let me tranfer you to live agent"
    }
}
def get_response(message):
    #convert message to lowercase
    message = message.lower()
    #check if message contains keywords
    if any(word in message for word in intents["keywords"]):
        
        return intents["response"]
# Defining the ChatBot class for interaction.
            # Analyzing the sentiment of the user's message.
        sentiment = TextBlob(message).sentiment.polarity
            # Generating the chatbot's response based on sentiment.
        return ("That's so great to hear!" if sentiment>0 else
                "I'm so sorry to hear that. How can I help" if sentiment <0 else    
                "I see. Can you tell me more about that?")
            # Printing the chatbot's response and sentiment.
def chat():
    
    
    print("Chatbot: Hi how can I help you today")
   
    while(user_message:=input("You:").strip().lower()) not in ['exit','quit','bye']:
        print(f"\nChatbot: {get_response(user_message)}")        
    print("Chatbot: Thank you for chatting")
    
if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
     chat()
