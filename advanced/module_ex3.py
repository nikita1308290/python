import os

print("current folder")
print(os.getcwd())
print(os.listdir())

print("C Drive content")
os.chdir('C:\\Program files')
print(os.getcwd())
print(os.listdir())

address = r'C:\Program files\Python\Python.exe'
if os.path.exists(address):
    print('valid address')
else:
    print('Invalid address')
