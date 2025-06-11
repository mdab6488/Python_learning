import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key = ""
)

# Step 1: Click on the chrome icon at coordinates (476, 35)
pyautogui.click(476, 35)
time.sleep(1) # wait for 1 second to ensure the click is resgisterd

# Step 2: Drag the mouse from (523, 300) to (1406, 864) to select the text
pyautogui.moveTo(919, 949)
pyautogui.dragTo(2046, 201, duration=1.0, button='left') # Drag for 1 second

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey("ctrl", "c")
pyautogui.click(2046, 201)
time.sleep(1) # Wait for 1 second to ensure the copy command is complete

# Step 4: Retrieve the text from the clipboard and store it is a variable
chat_history = pyperclip.paste()

# Print the copied text to verify
print(chat_history)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Alamin you speaks bangla as well as english. You are from Bangladesh and coder. You analyze chat history and respond like Alamin. Output should be the next chat response as Alamin",
        },
        {"role": "user", "content": chat_history},
    ],
)

response = completion.choices[0].message.content
pyperclip.copy(response)

# Step 5: Click at coordinates (1808, 1328)
pyautogui.click(1040, 120)
time.sleep(1) # Wait for 1 second to ensure the copy command is complete

# Step 6: Past the text
pyautogui.hotkey("ctrl", "v")
time.sleep(1) # Wait for 1 second to ensure the copy command is complete

# Step 7: Press Enter
pyautogui.press('enter')