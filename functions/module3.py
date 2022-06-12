import os

if not os.path.exists('data analysis'):
    os.mkdir("data analysis")

print("the current location")
print(os.getcwd())

print('the current directory content')
content = os.listdir()
print(content)

if os.path.isdir('data analysis'):
    print('data analysis is a directory')

if os.path.isfile('set.ipynb'):
    print('set.ipynb is a file')

print('size of pic',os.path.getsize('riot.png')/1024,'KB')