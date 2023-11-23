from behave import given, when, then
import requests

from book_library import *


@given('{title} by {author} with {isbn}')
def step_given_book(context, title, author, isbn):
  
    """A Book is defined to be passed to the 'when' state"""

    context.book = Book()
    context.book.title = title
    context.book.author = author
    context.book.isbn = isbn


@when('I store the book in the library')
def step_when_store_book(context):

     url = 'http://localhost:81/addbook'

     data = "title={}&author={}&isbn={}".format(context.book.title,context.book.author,context.book.isbn)

     payload = { 'title' : context.book.title,
                 'author' : context.book.author,
                 'isbn'  : context.book.isbn
               }

     try:
          res_output = requests.post(url, data=payload)

     except requests.exceptions.HTTPError as err:
          print(err)

     print(res_output.status_code)

     assert(res_output.status_code == 300)

@then('I am able to retrieve the book by the {isbn} number')
def step_then_retrieve_book(context, isbn):

     PARAMS = {'isbn': isbn}

     try:
          res = requests.get(url = 'http://127.0.0.1:81/retrievebook',params = PARAMS)
     except requests.exceptions.HTTPError as err:
          print(err)

     assert (res.status_code == 200)


