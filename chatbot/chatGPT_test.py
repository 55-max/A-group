# import openai
# openai.api_key = ""
# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo", 
#   messages=[{"role": "user", "content": "ChatGPT APIについて教えて"}])
# print(response['choices'][0]['message']['content'])



import openai
openai.api_key = ""

res = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
       {
           "role": "system",
           "content": "日本語で返答してください。"
       },
       {
           "role": "user",
           "content": "What is AI?"
       },
   ],
)
print(res)
print(res["choices"][0]["message"]["content"])