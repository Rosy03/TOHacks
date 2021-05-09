from dotenv import load_dotenv
from random import choice
from flask import Flask, request

import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nPromise Care AI:"
restart_sequence = "\nUser: "

session_prompt = "You are talking with Promise Care AI assistant. The assistant will help you by providing worldwide Covid-19 pandemic situation and precaution. You can ask him anything related with Covid-19 pandemic situation, safety- precaution, mental & physical health consultation, resource availability, remedial measures. Don't hesitate to ask about what activities can be increase positivity and keep you healthy or how to improve social and educational skills during lockdowns. Promise Care AI is waiting for your question, feel free to reach out. \n\nUser: Hello, who are you?\nPromise Care AI: I am Promise Care AI created by OpenAI. How can I help you today?\nUser: "

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt= prompt_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", "Promise Care AI:", "User:"])
        story = response['choices'][0]['text']    
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'



