import re

url = input("URL: ").strip()
# print(url)

# username = url.replace("https://x.com/", "")
# username = url.removeprefix("https://x.com/")
# print(f"Username: {username}")

# username = re.sub(r"^(https?://)?(www\.)?x\.com/", "", url)
# print(f"Username: {username}")
# matches = re.search(r"^https?://(www\.)?x\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username: ", matches.group(2))

# if matches := re.search(r"^https?://(www\.)?x\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username: ", matches.group(2))

# if matches := re.search(r"^(?:https?://)?(?:www\.)?x\.com/([a-z0-9_]+)", url, re.IGNORECASE):
#     print(f"Username: ", matches.group(1))

if matches := re.search(r"^(?:https?://)?(?:www\.)?x\.com/([\w]+)", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
