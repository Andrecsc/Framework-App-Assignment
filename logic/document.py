class Document(object):
    """
    Class used to represent a Document
    """

    def __init__(self, ID: int, title: str, number_pages: int, category: str, authors: str):
        """ Document constructor object.

        :param ID: id of document.
        :type ID: int
        :param title: title of document.
        :type title: str
        :param number_pages: pages of document.
        :type number_pages: int
        :param category: category of document.
        :type category: str
        :param authors: authors of document.
        :type authors: str
        :returns: document object
        :rtype: object
        """

        # attributes
        self._ID = ID
        self._title = title
        self._number_pages = number_pages
        self._category = category
        self._authors = authors

        # ID
        @property
        def ID(self) -> int:
            """ Returns ID of the document.
              :returns: ID of document.
              :rtype: int
            """
            return self._ID

        @ID.setter
        def ID(self, ID: int):
            """ The id of the document.
            :param ID: id of document.
            :type: int
            """
            self._ID = ID

        # title
        @property
        def title(self) -> str:
            """ Returns title of the document.
            :returns: title of document.
            :rtype: str
            """
            return self._tilte

        @title.setter
        def title(self, title: str):
            """ The title of the document.
            :param title: id of document.
            :type: str
            """
            self._title = title

        # number of pages
        @property
        def number_pages(self) -> int:
            """ Returns pages of the document.
            :returns: number_pages of document.
            :rtype: int
            """
            return self._number_pages

        @number_pages.setter
        def number_pages(self, number_pages: str):
            """ The pages of the document.
            :param number_pages: pages of document.
            :type: int
            """
            self._number_pages = number_pages

        # category
        @property
        def category(self) -> str:
            """ Returns category of the document.
            :returns: category of document.
            :rtype: str
            """
            return self._category

        @category.setter
        def category(self, category: str):
            """ The category of the document.
            :param category: category of document.
            :type: str
            """
            self._category = category

        # authors
        @property
        def authors(self) -> str:
            """ Returns authors of the document.
            :returns: authors of document.
            :rtype: str
            """
            return self._authors

        @authors.setter
        def authors(self, authors: str):
            """ The authors of the document.
            :param authors: authors of document.
            :type: str
            """
            self._authors = authors

        def __str__(self):
            """ Returns str of document.
            :returns: sting document
            :rtype: str
            """
            return '({0}, {1}, {2}, {3}, {4})'.format(self._ID, self._title, self._number_pages, self._category, self._authors)

        if __name__ == '__main__':
            book = Document(ID = 626, title = "Lilo & Stitch", number_pages = 100, category = "Kids", authors = "Disney")
            print(book)


