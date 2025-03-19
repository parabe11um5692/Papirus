import flet as ft
import connection as con
import book_settings as bs
import user_cabinet as uc
from config import user_login_value
con.connection_reg() #подключение к базе данных

user_login_value = 'имя'
def main(page: ft.Page):
    """Основная настройка страницы"""
    global user_login_value

    page.title = 'Папирус'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 600
    page.window.height = 900
    page.window.resizable = False   

    logged_in = False #переменная-заглушка, меняется при авторизации пользователя и позволяет посмотреть личный кабинет
    
    def register(e):
        """Функция для регистрации нового пользователя"""

        global user_login_value
        with con.connection_to_data_base_reg.cursor() as cursor:
            query = f"""
            INSERT INTO `reg`(user_name, user_pass) VALUES('{user_login.value}', '{user_password.value}')"""
            try:
                cursor.execute(query)
                con.connection_to_data_base_reg.commit()
                page.open(ft.SnackBar(ft.Text(f'Приятно познакомиться,{user_login.value}')))
                user_password.value = ''
                user_login_value = user_login.value
                print(user_login_value)

            except Exception as ex:
                page.open(ft.SnackBar(ft.Text('Имя занято')))
                print('Ошибка', ex)
            page.update()
            
    def auth(e):
        """Функция для авторизации пользователя"""
        global user_login_value
        with con.connection_to_data_base_reg.cursor() as cursor:
            query = """
            SELECT * FROM reg WHERE user_name = %s AND user_pass = %s
            """
            try:
                cursor.execute(query, (user_login.value, user_password.value))
                result = cursor.fetchone() 
                if result: 
                    user_password.value = ''
                    user_login_value = user_login.value
                    print(user_login_value)
                    nonlocal logged_in
                    logged_in = True
                    
                    navigate(None)
                    page.navigation_bar.destinations.pop(0)
                    page.navigation_bar.destinations.pop(0)
                    
                    global second_nav
                    second_nav = ft.NavigationBar(
                        destinations= [
                            ft.NavigationBarDestination(icon=ft.icons.BOOK, label= 'Кабинет'),
                            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="На поиски"),
                            ft.NavigationBarDestination(icon=ft.icons.MY_LIBRARY_BOOKS, label="Моя подборка")
                        ],
                        on_change=navigate_for_cabinet)
                    page.add(second_nav)                           
                else: 
                    page.open(ft.SnackBar(ft.Text('Неверные данные')))
                page.update()
            except Exception as ex:
                print('Ошибка', ex)
                auth_btn.text = 'Не получилось'

    def valid(e):
        """Функция для проверки заполненности полей"""
        if all([user_login.value, user_password.value]):
            registr_btn.disabled = False
            auth_btn.disabled = False
        else:
            registr_btn.disabled = True
            auth_btn.disabled = True
        page.update()

    def change_pass(e):
        """Функция для смены иконки замка и отображения пароля"""
        if pass_lock.icon == ft.icons.LOCK:
            pass_lock.icon = ft.icons.LOCK_OPEN  
            user_password.password = False  
        else:
            pass_lock.icon = ft.icons.LOCK  
            user_password.password = True  
        page.update()       
    
    user_login = ft.TextField(label='Ваше имя', width= 200, on_change= valid)
    pass_lock = ft.IconButton(icon=ft.icons.LOCK, on_click= change_pass)
    user_password = ft.TextField(label='Ваш пароль', width= 200, on_change= valid, password=True, suffix_icon=pass_lock)
    registr_btn = ft.OutlinedButton(text='Начать', width=200, on_click= register, disabled=True)
    auth_btn = ft.OutlinedButton(text='Начать', width=200, on_click= auth, disabled=True)    
    registration = ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Регистрация'),
                        user_login,
                        user_password,
                        registr_btn
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER

        )
    autorisation = ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Авторизация'),
                        user_login,
                        user_password,
                        auth_btn
            
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    
    def open_all_books(e):
        page.controls.clear()
        show_books_container = ft.Container(
        content=ft.Column( 
            controls=show_books,  
            alignment=ft.MainAxisAlignment.CENTER,  
            scroll=ft.ScrollMode.ALWAYS, 
            width=400,
            height=700, 
        ),alignment=ft.Alignment(0, 0))
        page.add(navigate_for_my_books) 
        page.add(show_books_container) 
        page.add(second_nav)  
        page.update() 

    def open_all_foreign_books(e):
        page.controls.clear()
        show_books_container = ft.Container(
        content=ft.Column( 
            controls=show_books,  
            alignment=ft.MainAxisAlignment.CENTER,  
            scroll=ft.ScrollMode.ALWAYS, 
            width=400,
            height=700, 
        ),alignment=ft.Alignment(0, 0))
        page.add(navigate_for_my_books) 
        page.add(show_books_container) 
        page.add(second_nav)  
        page.update() 

    def open_all_art_books(e):
        page.controls.clear()
        show_books_container = ft.Container(
        content=ft.Column( 
            controls=show_books[:2],  
            alignment=ft.MainAxisAlignment.CENTER,  
            scroll=ft.ScrollMode.ALWAYS, 
            width=400,
            height=700, 
        ),alignment=ft.Alignment(0, 0))
        page.add(navigate_for_my_books) 
        page.add(show_books_container) 
        page.add(second_nav)  
        page.update() 

    def open_all_adventure_books(e):
        page.controls.clear()
        show_books_container = ft.Container(
        content=show_books[1],
        alignment=ft.Alignment(0, 0), 
        padding=10)
        page.add(navigate_for_my_books)
        page.add(show_books_container) 
        page.add(second_nav)
        page.update()
       
    def open_all_tragedy_books(e):
        page.controls.clear()
        show_books_container = ft.Container(
        content=show_books[0],
        alignment=ft.Alignment(0, 0), 
        padding=10)
        page.add(navigate_for_my_books)
        page.add(show_books_container) 
        page.add(second_nav)
        page.update()
     
   
    navigate_for_my_books = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(ft.icons.COLLECTIONS_BOOKMARK, icon_color='#e85a4f', on_click=open_all_books),
                ft.IconButton(ft.icons.EXPLORE, icon_color='white', on_click=open_all_foreign_books),
                ft.IconButton(ft.icons.PALETTE, icon_color='#e85a4f', on_click=open_all_art_books),
                ft.IconButton(ft.icons.MAP, icon_color='#e9eeca', on_click=open_all_adventure_books),
                ft.IconButton(ft.icons.SENTIMENT_DISSATISFIED_SHARP, icon_color='white', on_click=open_all_tragedy_books)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=70,
        ),
        height=80, 
        padding = ft.Padding(0,0,0,0)
    )
    
    cabinet = ft.Row(
            [   
                uc.main_user_profile()
            ]   
        )
    search = ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Здесь вы найдете книги своей мечты')
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    show_books = [
        bs.stack_1,
        bs.stack_2,
        bs.stack_3
    ]
    
    my_books = ft.Column(
        controls=[
            ft.Container(navigate_for_my_books),
            ft.Container(
                ft.Column(
                    controls=show_books,
                    alignment=ft.MainAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ALWAYS,
                    width=400,
                    height=700,     
                ),
                alignment=ft.Alignment(0,0),
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
    )
    def navigate(e):
        """Выбор между регистрацией и авторизацией. Развертывание личного кабинета для авторизованных пользователей"""
        page.clean()
        if logged_in:
            page.add(cabinet)
        else:
            index = page.navigation_bar.selected_index
            if index == 0:
                page.add(registration)
            elif index == 1:
                page.add(autorisation)
        page.update()

    def navigate_for_cabinet(e):
        """Навигация внутри личного кабинета"""
        index = second_nav.selected_index
        page.clean()
        if index == 0:
            page.add(cabinet)
            page.add(second_nav)
        elif index == 1:
            page.add(search)
            page.add(second_nav)
        elif index == 2:
            page.add(my_books)
            page.add(second_nav)
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK_ADD, label="Регистрация"),
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="Авторизация"),
        ],
        on_change=navigate
    )
   
    page.add(registration)

ft.app(target=main)
con.connection_reg.close()
