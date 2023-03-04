import os
import openai
import gradio as gr

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_api(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )

  return response.choices[0].text

  def chat(input, history):
    history = history or []
    gradio_state = list(sum(history, ()))
    gradio_state.append(input)
    inpt = ' '.join(gradio_state)
    output = openai_create(inpt)
    history.append((input, output))
    return history, history