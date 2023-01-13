import os
from random import randint

import pywebio
from pyperclip import copy
from pywebio import start_server
from pywebio.input import (input, NUMBER)
from pywebio.output import (put_image, put_html, put_button, put_success, put_error, put_row, clear)

from symbols_for_password.symbols_for_password import symbols_for_password

pywebio.config(title='Generator Password')
pywebio.config(theme='dark')

password = ''


def refresh_page():
    # todo: This function is for refresh page by press button
    main()


def next_interface():
    put_html(f'<h1>Your Password is : {password} </h1>')
    put_success('Generating password is successful', closable=True)

    put_row([put_button(label='copy password', onclick=lambda: copy(password)), None,
             put_button(label='refresh page', onclick=refresh_page), put_button(label='write in file', onclick='')],
            size='16% 5px 16%')



def generator_password():
    # todo: This function is for generate password

    try:
        length_password_input = input(placeholder='Please Enter length password', type=NUMBER, maxlength=2048)
        global password
        for i in range(length_password_input):
            password = f'{password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
        next_interface()

    except Exception as ex:
        put_error('Your password is very big', closable=True)
        generator_password()


def main():
    clear()
    logo_path = os.path.join('image', 'logo.jpg')
    put_image(open(file=logo_path, mode='rb').read())
    generator_password()


if __name__ == '__main__':
    start_server(main, port=8000, debug=True)
