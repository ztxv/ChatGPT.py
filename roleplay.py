import openai

def chatgpt():
    openai.api_key = "ENTER API KEY HERE" #stores API key

    character = None # sets the character value to None
    user_input = None # sets user input to None

   

    if character is None: # makes sure this question is only asked once. Once user answers, character is not None
        character = input('\nType or describe the character you wish to interact with: ') # User chooses what character they want to talk to

    while True:
        user_input = input('\nYou ---> ') # User inputs their inital prompt to said character

        # Check if the user wants to exit the conversation
        if user_input.lower() == 'exit':
            print('Goodbye!')
            break

        conversation_history = [ # message history to make chatGPT talk like the specified character.
            {"role": "system", "content": f'I want you to pretend that you are {character}. '
                                          f'I want you to have the same mannerisms, behavior, '
                                          f'and just act like you are actually {character}. '
                                          f'Make it as believable as possible.'},
            {"role": "system", "content": f'Do not break character when responding to me.'
                                          f'Starting from now, your future prompts will only be in character of the character I chose you to act like. It is crucial that you remember this and not act like anyone besides the specified character I just told you. When I reply to you, no matter what you must stay in character'},
            {"role": "user", "content": user_input}, 
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # selects model of GPT to use
            messages=conversation_history, # sends convo history to chatGPT
        )

        chatgpt_reply = response["choices"][0]["message"]["content"] # gets ChatGPT's reply from API
        print('')
        print(chatgpt_reply) # sends chatGPT's reply
        print('')

chatgpt()
