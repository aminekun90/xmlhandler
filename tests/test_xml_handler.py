'''Test cases for xml handler'''

import unittest
from api import XMLHandler
from api.models import CustomElement


class TestXMLHandler(unittest.TestCase):

    def setUp(self):
        '''Run at the begining of every test'''
        pass

    def tearDown(self):
        '''Run after the end of every test'''
        pass

    def test_broken_xml(self):
        '''Test xml file is broken'''
        self.assertRaisesRegex(
            AttributeError, r'The provided file is not well formed !', XMLHandler,
            file_path="tests/files/broken_xml.xml")

    def test_valid_xml(self):
        '''test valid xml file'''
        try:
            XMLHandler(file_path='tests/files/valid_xml.xml')
        except AttributeError as exception:
            self.fail(f'Test valid xml failed with error : {str(exception)}')

    def test_get_element_children(self):
        '''test get elements children'''
        handler = XMLHandler(file_path='tests/files/valid_xml.xml')
        try:
            handler.get_element_children(el_type='note')
        except Exception as exception:
            self.fail(f'Test get element children failed : {str(exception)}')
