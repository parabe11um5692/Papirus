import flet as ft
import os

import book_settings as bs
from book_settings import BookSample


import connection as con
con.connection_reg()

class LatestUserBooks:
    def __init__(self, book_sample):
        self.title = book_sample.title
        self.author = book_sample.author
        self.year = book_sample.year
        self.country = book_sample.country
        self.image_url_2 = book_sample.image_url_2

    def show_latest_books(self):
        return ft.Stack(
            controls=[
                ft.Image(
                    src=self.image_url_2,
                    width=400,
                    height=300,
                    fit=ft.ImageFit.COVER,
                    border_radius=25,
                ),
                ft.Container(
                    content=ft.Text(
                        self.title,
                        color="#e9eeca",
                        size=22,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.Alignment(0, 0),
                    padding=ft.Padding(15, -30, 15, 0),
                ),
                ft.Container(
                    content=ft.Text(
                        self.author,
                        color="#e9eeca",
                        size=17,
                        weight="light",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.Alignment(0, 0.2),
                    padding=ft.Padding(15, -10, 15, 0),
                ),
                ft.Container(
                    content=ft.Text(
                        f'{self.year}, {self.country}',
                        color="#e9eeca",
                        size=13,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.Alignment(0.1, 0.2 ),
                    padding=ft.Padding(0, 70, 20, 0),
                ),
            ],
            width=300,  
            height=200,
            
        )
first_book = LatestUserBooks(bs.book_1)
show_first_book = [first_book.show_latest_books()]

second_book = LatestUserBooks(bs.book_2)
show_second_book = [second_book.show_latest_books()]

third_book = LatestUserBooks(bs.book_3)
show_third_book = [third_book.show_latest_books()]

all_books = show_first_book + show_second_book + show_third_book

def main_user_profile():
            """Оформление кабинета пользователя"""
            return ft.Stack(
                controls=[
                    ft.Container(
                        ft.Text('Кабинет',
                        color="white",
                        size=25,
                        weight="bold"),
                        alignment=ft.Alignment(0, 0),
                        padding=ft.Padding(50, -200, 15, 0)
                    ),
                    ft.Container(
                        ft.CircleAvatar(
                        radius= 25,
                        color = ft.Colors.WHITE,
                        content = ft.Text('А', size= 20)
                    ),
                        alignment=ft.Alignment(0, 0),
                        padding=ft.Padding(470, -200, 15, 0)
                    ),
                    ft.Container(
                        ft.Text('Книг в моей коллекции: 3',
                        color="white",
                        size=15,
                        weight="bold",),
                        
                        alignment=ft.Alignment(0, 0),
                        padding=ft.Padding(50, -140, 15, 0)
                    ),
                    ft.Container(
                        content=ft.Row(controls= all_books, scroll=ft.ScrollMode.ALWAYS),
                        height=200,
                        width = 510,
                        margin=ft.Margin(50,-10,0,0)
                    ),
                ],
            )