#!/usr/bin/python3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('DeepChat')

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing",
    "I'm doing great",
    "That is good to hear",
    "Thank you",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response(str(input("Type your message...")))
print(response)