import requests

# params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
#
# r = requests.post("http://pythonscraping.com/files/processing.php", params)

params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)

print(r.text)
