
# import bardapi
# import os
import requests
# from bardapi import Bard, SESSION_HEADERS
import openai
openai.api_key = 'zu-049ebb017c7f7ceeef231495f1bc698a'
openai.api_base = "https://zukijourney.xyzbot.net/v1"  

# token = "bQh2OzDGvHb0xf13XMwCTm-pSDwBSrM4TRIyAz22QiVb-fOsKywVbvcNz6OKiQZU6u0RJg."
# session = requests.Session()
# session.cookies.set("__Secure-1PSID", "bQh2OxkN19HV8v0nuo3ah7WHRiHezMvAYYl04oc_FyziXRcjLEgpyAbwnwj4_gyrwfOuHA.")
# # session.cookies.set( "__Secure-1PSIDCC", "APoG2W-hz5p79jWs-HUEHDBvjyQydpTEjHC_Fb3aMLchYbmpoM-0IMk9PyAv9SLSADXEwhpH")
# # session.cookies.set("__Secure-1PSIDTS", "sidts-CjIB3e41hbPfJwzKVqR6t8_UUOLZO4MhAV8LNn28HT5IYkoJRoJ8phryh74nOQoe_OAg6xAA")
# session.headers = SESSION_HEADERS

# def get_bard_reponse(input_text):
#     bard = Bard(token=token, session=session, timeout=60)
#     b = bard.get_answer(input_text+"give me only code in cpp with using dfs or bfs")
#     return b['content']


def get_chatgpt_response(input_text):
    chat_completion = openai.ChatCompletion.create(
        stream=False,
        model="llama2",
        messages=[
            {
                "role": "user",
                "content": input_text
            }
        ],
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

# def reset_chatgpt_ip():
# get_chatgpt_response("hey what is 1+2")