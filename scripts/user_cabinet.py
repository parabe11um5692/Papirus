import flet as ft
import os

import book_settings as bs
from book_settings import BookSample

import connection as con
from connection import *

from config import user_login_value

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
            user_photo = 'user_photo.jpg'
            url_for_user_photo = os.path.join('..','img',user_photo)
            first_achievement  =  ft.Icon(name=ft.icons.CHROME_READER_MODE,color='white', tooltip='За добавление 5 книг')
            second_achievement =  ft.Icon(name=ft.icons.ACCESS_ALARM_OUTLINED,color='white', tooltip='За проведение 24 часов в приложении')
            third_achievement  =  ft.Icon(name=ft.icons.FORMAT_LIST_BULLETED_ROUNDED,color='white', tooltip='За добавление книг из 3 разных жанров')

            """Оформление кабинета пользователя"""
            return ft.Stack(
                controls=[
                    ft.Container(
                        ft.Text(f'Ваше имя: {user_login_value}',
                        color="white",
                        size=25,
                        weight="bold"),
                        alignment=ft.Alignment(0, 0),
                        margin=ft.Margin(340, -80, 15, 0)
                    ),
                    
                    ft.Container(
                        ft.Text('Дата регистрации в Папирус: ',
                        color="white",
                        size=15,
                        weight="light"),
                        alignment=ft.Alignment(0, 0),
                        margin=ft.Margin(340, -10, 15, 0)
                    ),
                    ft.Container(
                        ft.Image(
                        src=url_for_user_photo,
                        border_radius=25,
                        width= 250,
                        height=250,
                        fit=ft.ImageFit.COVER,
                    ),
                        alignment=ft.Alignment(0, 0),
                        margin=ft.Margin(50, -70, 15, 0)
                    ),
                    ft.Container(
                        content = ft.Row(controls=[first_achievement,second_achievement,third_achievement]),
                        alignment=ft.Alignment(0, 0),
                        margin=ft.Margin(125, 200, 15, 0)
                    ),
                    ft.Container(
                        ft.Text('Последние добавленные книги:',
                        color="white",
                        size=15,
                        weight="bold",),
                        
                        alignment=ft.Alignment(0, 0),
                        margin=ft.Margin(50, 300, 15, 0)
                    ),

                    ft.Container(
                        ft.Text('Книг в моей коллекции: 3',
                        color="white",
                        size=15,
                        weight="bold",),
                        
                        alignment=ft.Alignment(0, 0),
                        margin=ft.Margin(350, 300, 15, 0)
                    ),
                    
                    ft.Container(
                        content=ft.Row(controls= all_books, scroll=ft.ScrollMode.ALWAYS),
                        margin=ft.Margin(50, 350, 15, 0),
                        height=200,
                        width = 510,
                        padding=ft.Padding(10,0,0,0)
                    )
                ]
            )