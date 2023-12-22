import chainlit as cl


api_key = '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'

@cl.on_message
async def main(message: str):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()

import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

os.environ["OPENAI_API_KEY"] = "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"

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0,streaming=True), verbose=True)

    return llm_chain

