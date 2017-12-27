import requests

params = {'username': '123', 'password': 'password'}

session = requests.Session()

# r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)

print("Cookie is set to: ")
print(s.cookies.get_dict())
print("----------------------------------")
print("Going to profile page: ")

# r = requests.get("http://pythonscraping.com/pages/cookies/profile.php")
# r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")

print(s.text)
