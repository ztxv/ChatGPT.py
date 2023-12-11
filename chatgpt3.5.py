import openai



def chatgpt(done):
# Set your OpenAI API key
    openai.api_key = "ENTER API-KEY HERE"
    
    if done == None: # this is here to prevent chatGPT from asking "how can i help you" after the first times
        user_input = input('How can I help you?: ')
    else:
        user_input = done # takes your reply and store it as user input, which chatgpt than recieves to respond to


# Your conversation with GPT-3.5-turbo
    conversation_history = [
        {"role": "user", "content": user_input},
    ]

# Send a message to GPT-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
    )

# Get and print the chatgpt's reply
    chatgpt_reply = response["choices"][0]["message"]["content"]
    print('')
    print(chatgpt_reply)
    print('')
    again()


def again(): # continues convo with chatgpt or can end it
    done = input('Anything else?: ') # allows you to reply back to chatGPT after it responds to you
    if done == 'no':
        exit()
    else:
        chatgpt(done) # sends your reply back to the chatgpt function

chatgpt(None)