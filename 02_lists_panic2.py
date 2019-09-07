"""A variant of the previous panic program."""

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase += ''.join([plist[5], plist[4], plist[7], plist[6]])

print(new_phrase)
