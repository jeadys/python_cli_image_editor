from inspect import cleandoc


def class_info(my_class):
    method_list = [attribute for attribute in dir(my_class) if callable(
        getattr(my_class, attribute)) and attribute.startswith('__') is False]

    for method in method_list:
        print(method)

    help_command = f'python editor.py {my_class.lower()} -h, fore more info'
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

    print(cleandoc(description[my_class]))
