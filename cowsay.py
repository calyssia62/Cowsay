print('cowsay is originally a linux package that generates ASCII art of a cow saying a message.')
print('After "cowsay" command, enter your message.')
text = input('cowsay ').strip()
text = text.replace('\n', ' ')
if len(text) <= 40:
    print(' ' + ('_' * (len(text) + 2)))
    print('< ' + text + ' >')
    print(' ' + ('-' * (len(text) + 2)))
elif len(text) > 40 and len(text) <= 80:
    print(' ' + ('_' * 42))
    print('/ ' + text[:40] + ' \\')
    print('\\ ' + text[40:] + (len(text[:40]) - len(text[40:])) * ' ' + ' /')
    print(' ' + ('-' * 42))
elif len(text) > 80:
    print(' ' + ('_' * 42))
    print('/ ' + text[:40] + ' \\')
    last = len(text)%40
    for i in range(40, len(text) - last, 40):
        print('| ' + text[i:i+40] + ' |')
    print('\\ ' + text[-last:] + (len(text[:40]) - len(text[-last:])) * ' ' + ' /')
    print(' ' + ('-' * 42))

if len(text) == 1:
    space = 0
elif len(text) <= 40:
    space = len(text)//2
else:
    space = 20

print(' ' * space + '  \\   ^__^')
print(' ' * space + '   \\  (oo)\\_______')
print(' ' * space + '      (__)\\       )\\/\\')
print(' ' * space + '          ||----w |')
print(' ' * space + '          ||     ||')
