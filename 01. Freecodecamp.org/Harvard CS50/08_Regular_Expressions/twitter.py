# https://twitter.com/mdab6488
# http://twitter.com/mdab6488
# https://www.twitter.com/mdab6488
# http://www.twitter.com/mdab6488
# www.twitter.com/mdab6488
# re.sub(pattern, repl, string, count=0, flags=0)
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)

# A|B either A or B
# (...) a group
# (?:...) non-capturing version

import re

print()
# while True:
#     url = input("URL: ").strip()
#
#     # username = url.replace("https://twitter.com/", "")
#     # username = re.sub(r"^(http|https)://twitter\.com/", "", url)
#     username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#
#     print(f"Username: {username}")

while True:
    url = input("URL: ").strip()
    # matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
    #
    # if matches:
    #     print(f"Username:",matches.group(3))

    if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.(?:com|org)/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
        print(f"Username:",matches.group(1))


