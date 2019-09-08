"""Convert 'Don't Panic' to 'on tap' using only list methods."""

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)
for i in range(4):
    plist.pop()
plist.remove("'")

print(plist)
plist.extend([plist.pop(), plist.pop()])        # Swaps 'p' and 'a'
plist.insert(2, plist.pop(3))                   # Pops the ' ' and inserts it in index 2

new_phrase = ''.join(plist)
print(new_phrase)
