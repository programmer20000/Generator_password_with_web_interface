from pyperclip import copy
from pywebio.output import (put_html, toast, put_row, put_button, put_file)


def write_and_read_password_file(your_password: str):
    # todo: we now write password in file
    with open(file='password.txt', mode='w') as file:
        file.write(your_password)

    # todo: we now read password from file
    with open(file='password.txt', mode='rb') as file:
        content = file.read()
        put_file(name='yours_password.txt', content=content, label='download file')


def copy_password(password: str) -> str:
    copy(password)
    toast('password successful copy')


def refresh_page(func):
    # todo: This function is in state of the development
    return func()

def next_interface(password):
    put_html(f'<h1>Your Password is : {password} </h1>')
    toast('Generating password is successful')

    put_row([put_button(label='copy password', onclick=lambda: copy_password(password)), None,
             put_button(label='refresh page', onclick=refresh_page),
             put_button(label='write in file and download',
                        onclick=lambda: write_and_read_password_file(your_password=password))],
            size='16% 16px 16%')
