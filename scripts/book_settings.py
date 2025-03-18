import flet as ft
import os
import connection_book as con
from connection_book import *

connection = con.connection_to_book()

class BookSample:
    """Основной класс для создания карточки книги. Данные вытягиваются из SQL-таблицы, форматируются flet"""
    def __init__(self, title, author, year, country ,description, full_text, image_url, image_url_2):
        self.title = title
        self.author = author
        self.year = year
        self.country = country
        self.description = description
        self.full_text = full_text
        self.image_url = image_url
        self.image_url_2 = image_url_2

        self.text_for_book = ft.Text(
            self.description,
            color="#e9eeca",
            size=15,
            weight="bold",
            text_align=ft.TextAlign.CENTER
        )

        self.button_sample = ft.IconButton(
            icon=ft.icons.EXPAND_MORE,
            icon_color='#c9764b',
            on_click=self.show_more
        )

        self.text_sample = ft.Container(
            self.text_for_book,
            alignment=ft.Alignment(0, 0),
            padding=ft.Padding(15, 170, 15, 0)
        )

        self.button_container = ft.Container(
            content=self.button_sample,
            alignment=ft.Alignment(0, 0.6),
            padding=ft.Padding(15, 10, 15, 0)
        )

        self.task_1 = ft.IconButton(ft.icons.EXPLORE, icon_color='white')
        self.task_2 = ft.IconButton(ft.icons.PALETTE, icon_color='#e85a4f', tooltip='Художественная')
        self.task_3 = ft.IconButton(ft.icons.SENTIMENT_DISSATISFIED_SHARP, icon_color='#e9eeca', tooltip='Трагедии')

    def show_more(self, e):
        """Развертывание описания с заменой иконки"""
        self.text_for_book.value = self.full_text
        self.button_sample.icon = ft.icons.EXPAND_LESS
        self.button_sample.on_click = self.show_less
        self.text_for_book.size = 14
        self.text_for_book.weight = 'bold'
        self.button_container.alignment = ft.Alignment(0, 0.6)

        self.text_sample.padding = ft.Padding(15, 170, 15, 0)

        self.button_container.update()
        self.text_sample.update()

    def show_less(self, e):
        """Свертывание описания с заменой иконки"""
        self.text_for_book.value = self.description
        self.button_sample.icon = ft.icons.EXPAND_MORE
        self.button_sample.on_click = self.show_more
        self.button_container.alignment = ft.Alignment(0, 0.6)
        self.text_for_book.size = 15
        self.text_for_book.weight = 'bold'
        self.button_container.update()
        self.text_for_book.update()

    def create_book_stack(self):
        """Форматирование вывода данных"""
        return ft.Stack(
            controls=[
                ft.Image(
                    src=self.image_url,
                    width=400,
                    height=700,
                    fit=ft.ImageFit.COVER,
                    border_radius=25,
                ),
                ft.Container(
                    ft.Image(
                        src=self.image_url_2,
                        width=400,
                        height=300,
                        fit=ft.ImageFit.COVER,
                        border_radius=25,
                    ),
                    padding=ft.Padding(15, 20, 15, 0)
                ),
                self.text_sample,
                ft.Container(
                    content=ft.Text(
                        self.title,
                        color="#e9eeca",
                        size=30,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.Alignment(0, 0),
                    padding=ft.Padding(15, -400, 15, 0),
                ),
                ft.Container(
                    content=ft.Text(
                        self.author,
                        color="#e9eeca",
                        size=20,
                        weight="light",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.Alignment(0, -0.3),
                    padding=ft.Padding(15, -90, 15, 0),
                ),
                ft.Container(
                    content=ft.Text(
                        f'{self.year}, {self.country}',
                        color="#e9eeca",
                        size=13,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.Alignment(0.1, -0.2),
                    padding=ft.Padding(0, 0, 20, 0),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[self.task_1, self.task_2, self.task_3]
                    ),
                    alignment=ft.Alignment(1, -0.3),
                    margin=ft.Margin(130, 0, 0, 20)
                ),
                self.button_container
            ],
            width=400,
            height=700,
        )
    
image_filename = 'book_background.jpg'
image_filename_1 = 'book.jpg'

url_for_first_book = os.path.join('..','img',image_filename)
url_2_for_first_book = os.path.join('..','img',image_filename_1)

#нужно оставить один sql-запрос и разобраться с импортом фотографий
with connection.cursor() as cursor:
        query = """SELECT title, author, year, country, description, full_text FROM books WHERE id = 5"""
        cursor.execute(query)
        result = cursor.fetchone()
        book_1 = BookSample(
            title  = result['title'],
            author = result['author'],
            year   =  result['year'],
            country=result['country'],
            description= result['description'],
            full_text= result['full_text'],
            image_url=url_for_first_book,
            image_url_2=url_2_for_first_book
        )

        image_filename_2 = 'book1_background.jpg'
        image_filename_3 = 'book1.jpg'
                
        url_for_second_book = os.path.join('..','img',image_filename_2)
        url_2_for_second_book = os.path.join('..','img',image_filename_3)

        query_2 = """SELECT title, author, year, country, description, full_text FROM books WHERE id = 9"""
        cursor.execute(query_2)
        result = cursor.fetchone()
        book_2 = BookSample(
            title  = result['title'],
            author = result['author'],
            year   =  result['year'],
            country = result['country'],
            description = result['description'],
            full_text = result['full_text'],
            image_url = url_for_second_book,
            image_url_2 = url_2_for_second_book
        )

        image_filename_4 = 'book2__background.jpg'
        image_filename_5 = 'book2.jpg'
                
        url_for_third_book = os.path.join('..','img',image_filename_4)
        url_2_for_third_book = os.path.join('..','img',image_filename_5)

        query_3 = """SELECT title, author, year, country, description, full_text FROM books WHERE id = 7"""
        cursor.execute(query_3)
        result = cursor.fetchone()
        book_3 = BookSample(
            title  = result['title'],
            author = result['author'],
            year   =  result['year'],
            country = result['country'],
            description = result['description'],
            full_text = result['full_text'],
            image_url = url_for_third_book,
            image_url_2 = url_2_for_third_book
        )
        #вывод книг
        stack_1 = book_1.create_book_stack()
        stack_2 = book_2.create_book_stack()
        stack_3 = book_3.create_book_stack()
 
