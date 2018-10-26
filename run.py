"""
This is run.py contains the main function
"""

from api import XMLHandler


def main():
    '''This is the main function'''
    print('running !')
    hpr_handler = XMLHandler(file_path='tests/files/valid_xml.xml')
    print(hpr_handler.get_element_children(el_type='note'))


if __name__ == '__main__':
    main()