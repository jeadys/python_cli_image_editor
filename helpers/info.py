from inspect import cleandoc

"""
class_info is used when a file is directly executed such as a feature class.
This is done by using __name__ == '__main__'
class_info provides some extra information about the class such as functions within the class and the help command.
"""


def class_info(my_class):
    method_list = [attribute for attribute in dir(my_class) if callable(
        getattr(my_class, attribute)) and attribute.startswith('__') is False]

    help_command = f'python editor.py {my_class.__name__.lower()} -h, fore more info'

    description = {
        'Convert':
        '''
            Change the image(s) file format.
        ''',

        'Dimension':
        f'''
            Scale, rotate or flip the image(s).
            {help_command}
        ''',

        'Filter':
        f'''
            Apply a blur to the image(s).
            {help_command}
        ''',

        'Hue':
        f'''
            Add contrast or make image(s) black and white.
            {help_command}
        ''',

        'Watermark':
        f'''
            Add a watermark to your image(s).
            {help_command}
        ''',
    }

    print(cleandoc(description[my_class.__name__]))

    for method in method_list:
        print(method)

    return my_class
