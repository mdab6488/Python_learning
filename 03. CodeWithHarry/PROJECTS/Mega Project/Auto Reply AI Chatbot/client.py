from openai import OpenAI

# pip install opeai
# if you saved the key under a diffrent environment variable name, you can do something like:
client = OpenAI(
    api_key = ""
)
command = '''

'''
response = client.responses.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a person named harry who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Harry",
        },
        {"role": "user", "content": command},
    ],
)

print(response.output_text)