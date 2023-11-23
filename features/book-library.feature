Feature: Adding books to library
    Scenario Outline: Store book in the library
        Given <title> by <author> with <isbn>
        When I store the book in the library
        Then I am able to retrieve the book by the <isbn> number 

        Examples: Books
        | title | author | isbn |
        | The Lord of the Rings | J.R.R Tolkien | 0395974682 |
        | Turkey Man | NatedoggThanksgiving | 2468101200 |       