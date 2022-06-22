from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Author

def opendb():
    engine = create_engine('sqlite:///mydb.sqlite')
    Session = sessionmaker(bind=engine)
    return Session()

def add_author(name):
    db = opendb()               # open database
    a = Author(name=name)       # create new author
    db.add(a)                   # add author to database
    db.commit()                 # commit changes    
    db.close()                  # close database                    

def show_authors():
    db = opendb()
    authors = db.query(Author).all()
    db.close()
    return authors

while True:
    print('-'*20)
    print('1. Add author')
    print('2. Display authors')
    print('3. Quit')
    print('-'*20)
    choice = input('Enter your choice: ')
    if choice == '1':
        name= input('Enter author name: ')
        add_author(name)
        print('Author added')
    elif choice == '2':
        for author in show_authors():
            print(author)
    elif choice == '3':
        break
