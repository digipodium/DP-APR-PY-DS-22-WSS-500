import random
def generate_name():
    list1 = ['red', 'green', 'blue', 'yellow', 'orange',
             'purple', 'pink', 'brown', 'black', 'white']
    list2 = ['apple', 'banana', 'pear', 'grape', 'strawberry',
            'cherry', 'peach', 'pineapple', 'mango', 'watermelon']
    list3 = ['cat', 'dog', 'bird', 'fish', 'lion', 'tiger', 'bear', 'wolf',]

    p1 = random.choice(list1)
    p2 = random.choice(list2)
    p3 = random.choice(list3)
    return f'{p1}{p2}-{p3}'