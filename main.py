import os

import pywebio
from pywebio import start_server
from pywebio.output import (put_image, clear)

from next_interface import (generator_password)


class GeneratorPassword:
    def __init__(self):
        # todo: here we setup  window with title and theme properties
        pywebio.config(title='Generator Paasword', theme='dark')

    def run(self):
        # todo: This method give start to app
        clear()
        logo_path = os.path.join('image', 'logo.png')
        put_image(open(file=logo_path, mode='rb').read())
        generator_password()


if __name__ == '__main__':
    generator = GeneratorPassword()
    start_server(generator.run, port=8000, debug=True)
