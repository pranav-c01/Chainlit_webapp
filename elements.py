# import chainlit as cl


# # Global Elements
# @cl.on_chat_start
# async def start():
#     # Send the elements globally
#     await cl.Image(path="./df.png", name="image1", display="inline").send()
#     await cl.Text(content="Here is a side text document", name="text1", display="side").send()
#     await cl.Text(content="Here is a page text document", name="text2", display="page").send()

#     # Send the same message twice
#     content = "Here is image1, a nice image of a cat! As well as text1 and text2!"

#     await cl.Message(
#         content=content,
#     ).send()

#     await cl.Message(
#         content=content,
#     ).send()


# '''Scoped Elements
# Scoped elements are elements that are scoped to a specific message. To better understand scoped elements, let’s look at an example.'''


# @cl.on_chat_start
# async def start():
#     # Send the first message without the elements
#     content = "Here is image1, a nice image of a cat! As well as text1 and text2!"

#     await cl.Message(
#         content=content,
#     ).send()

#     elements = [
#         cl.Image(path="./df.png", name="image1", display="inline"),
#         cl.Text(content="Here is a side text document", name="text1", display="side"),
#         cl.Text(content="Here is a page text document", name="text2", display="page"),
#     ]

#     # Send the second message with the elements
#     await cl.Message(
#         content=content,
#         elements=elements,
#     ).send()

# import matplotlib.pyplot as plt
# import chainlit as cl


# @cl.on_chat_start
# async def main():
#     fig= plt.figure(figsize=(45,50))
#     plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

#     # await cl.Pyplot(name="simple plot", figure=fig, display="inline").send()
#     # await cl.Message(
#     #     content="Here is a simple plot"
#     # ).send()

#     elements = [
#         cl.Pyplot(name="plot", figure=fig, display="inline")
#     ]
#     await cl.Message(
#         content="Here is a simple plot",
#         elements=elements
#     ).send()



# @cl.on_chat_start
# async def main():
#     # Sending an image with the local file path
#     # sending image with onkline url
#     elements = [
#     cl.Image(name="image1", display="inline",size="large",url="https://www.befunky.com/images/prismic/1f427434-7ca0-46b2-b5d1-7d31843859b6_funky-focus-red-flower-field-after.jpeg?auto=avif,webp&format=jpg&width=863")
#     ]
#     await cl.Message(content="Look at this local image!", elements=elements).send()

## Ask text from user 
# @cl.on_chat_start
# async def main():
#     res = await cl.AskUserMessage(content="What is your name?", timeout=10).send()
#     if res:
#         await cl.Message(
#             content=f"Your name is: {res['content']}",
#         ).send()

## Ask user to upload file and upload csv/print/txt
# @cl.on_chat_start
# async def start():
#     files = None

#     # Wait for the user to upload a file
#     while files == None:
#         files = await cl.AskFileMessage(
#             content="Please upload a text file to begin!", accept={"text/plain": [".txt", ".py",".csv",".pdf"]}
#         ).send()
#     # Decode the file
#     text_file = files[0]
#     text = text_file.content.decode('utf-8')
    
#     await cl.Message(
#         content=f"Content of this file is {text} \n\n\n "
#     ).send()

#     # Let the user know that the system is ready
#     await cl.Message(
#         content=f"`{text_file.name}` uploaded, it contains {len(text)} characters!"
#     ).send()
