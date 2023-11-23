from flask import Flask, render_template, jsonify
from flask import request, Response

app = Flask(__name__)

class Store():

    instances = any

    def __init__(self):
        self.instances = dict()
        self.storeBook(Book())

    def storeBook(self, Book):
        self.instances[Book.isbn] = Book
    
    def getBook(self, isbn):
        return self.instances[isbn]

class Book():
    def __init__(self, title="Big Nate", author="Natedogg", 
                 isbn="1234567890"):
        self.title = title
        self.author = author
        self.isbn = isbn

the_store = Store()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/retrievebook', methods = ['GET'])
def retrievebook():

    if request.method == 'GET':
        book_holder = the_store.getBook(request.args.get('isbn'))
    
        return "Title:" + book_holder.title + \
                        "\nby Author:" + book_holder.author + \
                        "\nISBN:" + book_holder.isbn
    return "SUCCESS"


@app.route('/addbook', methods = ['POST'])
def addbook():

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']

        the_store.storeBook(Book(title,author,isbn))

    return "SUCCESS"

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=81)
    #app.run()