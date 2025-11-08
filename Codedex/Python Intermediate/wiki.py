import wikipedia

a = wikipedia.search('Minecraft', results=10, suggestion=False)

b = wikipedia.summary('Minecraft', sentences=2)

print(a)
print(b)
