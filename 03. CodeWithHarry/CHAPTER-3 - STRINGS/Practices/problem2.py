letter = '''Dear <|name|>, 
            You are selected! 
            <!Date>'''

print(letter.replace("<|name|>", "Riyan").replace("<!Date>", "28-11-2025"))