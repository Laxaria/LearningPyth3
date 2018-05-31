from urllib.request import urlopen


with urlopen("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt") as f:
    g = f.encode('utf-8')
    print(g)