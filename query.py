
# import requests
# id = 43
# problem= """A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words"""
# url = 'https://try-rz8w.onrender.com/save?'+ f'id={id}' + f'&&problem="{problem}"'
# print(url)
# r = requests.get(url, verify=False)
# print(r.content)

# import openai, re, requests, json, tempfile

# openai.api_key = "<your key, you can get it with /key on @zuki.api>"  
# openai.api_base = "https://zukijourney.xyzbot.net/v1" # or "https://zukijourney.xyzbot.net/unf" 

# response = openai.Embedding.create(input="cock and balls", model="balls")
# print(response)
# response = openai.Image.create(prompt="balls", n=1, size="1024x1024")
# print(response)

# chat_completion = openai.ChatCompletion.create(
#     stream=False, # can be true
#     model="gpt-4",  # "claude-2",
#     messages=[
#         {
#             "role": "user",
#             "content": 'There are 50 books in a library. Sam decides to read 5 of the books. How many books are there now? If there are 45 books, say "1". Else, if there is the same amount of books, say "2".', #responds 2: gpt-4, responds 1: gpt-3.5, didn't check claude or the others lol
#         },
#     ],
# )
# print(chat_completion.choices[0].message.content)

# js = {"input": "cock and balls."}
# headers = {"Content-Type": "application/json"}
# r = requests.post(
#     "https://zukijourney.xyzbot.net/v1/audio/speech", headers=headers, data=json.dumps(js)
#  )
#  files = {"file": ("audio.mp3", r.content, "audio/mpeg")}

# res = requests.post("https://zukijourney.xyzbot.net/v1/audio/transcriptions", files=files)
# print(res.text)
# print(res.json())