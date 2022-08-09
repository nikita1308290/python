names = ['Bruce Wayne', 'Clark Kent', 'Wally West']
initials = []

for name in names:
    parts = name.split()
    initials.append(parts[0][0]+parts[-1][0])
print(initials)

#comprehension
names = ['Bruce Wayne', 'Clark Kent', 'Wally West']
initials = [n.split()[0][0]+n.split()[-1][0] for n in names]
print(initials)