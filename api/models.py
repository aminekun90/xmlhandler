
'''models'''
import uuid
from .dbmodels import CustomElementTable
class CustomElement:
    '''Custom element'''
    element_type = ""
    el_complete = False
    attributes = {}
    text = ""
    el_id = ""
    parent_id = ""
    file_path=""
    file_type=""

    def __init__(self, element_type,file_path,file_type, attributes=None, text=None):
        self.element_type = element_type
        self.text = text
        self.el_id = uuid.uuid4()
        self.el_complete = False
        self.file_path=file_path
        self.file_type=file_type
        if attributes:
            self.attributes = attributes
        else:
            attributes = {}

    def complete(self):
        '''make element complete'''
        self.el_complete = True

    def is_completed(self):
        '''is the element complete ?'''
        return self.el_complete
    def to_custom_element_table(self):
        '''Returns a CustomElementTable instance to save to db'''
        return CustomElementTable(
            el_id=self.el_id,
            el_complete=self.el_complete,
            attributes=self.attributes,
            text=self.text,
            parent_id=self.parent_id,
            file_path=self.file_path,
            file_type=self.file_type
            )
    def dictify(self):
        return self.__dict__

    def __repr__(self):
        return str(self.__dict__)