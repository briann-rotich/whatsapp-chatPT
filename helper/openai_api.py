import os

import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = "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" #os.getenv('OPENAI_API_KEY')
#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


def chat_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt},
            ]
        )
        return {
            'status': 1,
            'response': response['choices'][0]['message']['content']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }