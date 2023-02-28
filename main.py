import os
from random import randint

import pywebio
from pyperclip import copy
from pywebio import start_server
from pywebio.input import (input, NUMBER)
from pywebio.output import (put_image, put_html, put_button, put_success, put_error, put_row, clear, put_file, put_grid)

from symbols_for_password.symbols_for_password import symbols_for_password


class GeneratorPassword:
    def __init__(self):

        # todo: here we setup  window with title and theme properties
        pywebio.config(title='Generator Paasword', theme='dark')

        self.password = ''

    def refresh_page(self):
        # todo: This function is for refresh page by press button
        self.run()

    def write_and_read_password_file(self, your_password: str):
        # todo: we now write password in file
        with open(file='password.txt', mode='w') as file:
            file.write(your_password)

        # todo: we now read password from file
        with open(file='password.txt', mode='rb') as file:
            content = file.read()
            put_file(name='your_password.txt', content=content, label='download file')

    def next_interface(self):
        put_html(f'<h1>Your Password is : {self.password} </h1>')
        put_success('Generating password is successful', closable=True)

        put_row([put_button(label='copy password', onclick=lambda: copy(self.password)), None,
                 put_button(label='refresh page', onclick=self.refresh_page),
                 put_button(label='write in file and download',
                            onclick=lambda: self.write_and_read_password_file(your_password=self.password))],
                size='16% 16px 16%')

    def generator_password(self):
        # todo: This function is for generate password
        self.placeholder = 'Please Enter length password'
        self.help_text = 'Max count of the symbols, your password not has to be more big of area offered (1-2048)'

        try:
            length_password_input = input(placeholder=self.placeholder, help_text=self.help_text, type=NUMBER,
                                          maxlength=2048, required=True)

            for i in range(length_password_input):
                self.password = f'{self.password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
            self.next_interface()

        except Exception as ex:
            put_error('Your password is very big', closable=True)
            self.generator_password()

    def run(self):
        clear()
        logo_path = os.path.join('image', 'logo.jpg')
        put_image(open(file=logo_path, mode='rb').read())
        self.generator_password()


if __name__ == '__main__':
    generator = GeneratorPassword()
    start_server(generator.run, port=8000, debug=True)
