from random import randint

from pywebio.input import (radio, input, NUMBER)
from pywebio.output import (toast, put_text)

from symbols_for_password import symbols_for_password
from .next_interface import next_interface


def select_variance(password: str):
    # todo: This function is in state of the development
    put_text('This option at will')
    variance = radio("Choose one", options=['uppercase', 'lowercase'])

    match variance:
        case 'uppercase':
            password.upper()

        case 'lowercase':
            password.lower()


password = ''


def generator_password():
    global password
    # todo: This method is the main he's for creating password
    try:
        length_password_input = input(placeholder='Please Enter length password',
                                      help_text='Max count of the symbols, your password not has to be more big of area offered (1-2048)'.upper(),
                                      type=NUMBER,
                                      maxlength=2048, required=True)
        # select_variance(password=password)

        for i in range(length_password_input):
            password = f'{password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
        next_interface(password=password)

    except Exception as ex:
        toast('Your password is very big')
        generator_password()
