"""
Handlers for xml structure files
"""
import os
import xml.etree.cElementTree as ET
from .models import CustomElement
from .dbmodels import CustomElementTable


def normalize(name):
    '''normalize tag name'''
    if name[0] == "{":
        uri, tag = name[1:].split("}")
        return uri, tag
    else:
        return name


class XMLHandler:
    """
    HarvestedProductionHandler class
    """

    def __init__(self, file_path, file_type):
        if not os.path.isfile(file_path):
            raise AttributeError(
                f'{file_path} is not a correct file path !')
        self.elements = []
        # element_tree
        self.file_path = file_path
        self.file_type = file_type
        try:
            for event, elem in ET.iterparse(self.file_path, events=("start", "end")):
                tag = normalize(elem.tag)
                if isinstance(tag, str):
                    tag = tag
                elif isinstance(tag, tuple):
                    tag = tag[1]
                if event == 'start':
                    self.start_element(tag, elem.attrib, elem.text)
                if event == 'end':
                    self.end_element(tag)
                    elem.clear()
        except ET.ParseError:
            raise AttributeError(f'The provided file is not well formed !')
        except Exception as exception:
            raise AttributeError(f'An exception occured : {exception}')

    def get_element_children(self, el_id=None, el_type=None):
        '''Get element chidren'''
        if el_type:
            find_element = next(obj for obj in self.elements if
                                obj.element_type == el_type)
            return [obj for obj in self.elements if obj.parent_id == find_element.el_id]
        if el_id:
            return [obj for obj in self.elements if obj.parent_id == el_id]

        raise AttributeError(
            'You need to provide at least one argument el_type or el_id !')

    def end_element(self, name):
        '''Call when an element ends'''
        # last added current element and not completed

        last_added_elem = next((obj for obj in
                                reversed(self.elements)
                                if obj.element_type == name and obj.is_completed() is False), None)
        index = next((i for i, item in enumerate(self.elements)
                      if item.el_id == last_added_elem.el_id), None)
        # Last not completed
        last_not_completed = next((obj for obj in
                                   reversed(self.elements)
                                   if obj.is_completed() is False and obj.element_type != name), None)

        if last_added_elem:
            last_added_elem.complete()
            if last_not_completed:
                last_added_elem.parent_id = last_not_completed.el_id
            else:
                last_added_elem.parent_id = None
            if index is not None:
                self.elements[index] = last_added_elem
            else:
                raise ValueError(
                    f'An error occured cannot find the index of "{name}" CustomElement')

    def start_element(self, name, attributes, text):
        """Call when an element starts"""
        element = CustomElement(element_type=name,
                                file_path=self.file_path, file_type=self.file_type, attributes=attributes)
        if text and element:
            text = text.replace('\n', '').strip()
            if text:
                element.text = text

        self.elements.append(element)

    def push_to_db(self, session):
        '''push to db using sqlalchemy session'''
        try:
            list_of_elements_to_db = [
                element.to_custom_element_table() for element in self.elements]

            session.query(CustomElementTable).filter(CustomElementTable.file_path == self.file_path,
                                                     CustomElementTable.file_type == self.file_type).delete(synchronize_session=False)
            session.bulk_save_objects(list_of_elements_to_db)
            session.commit()
            new_list = session.query(CustomElementTable).filter(CustomElementTable.file_path == self.file_path,
                                                                CustomElementTable.file_type == self.file_type).all()
            session.close()
            return new_list
        except Exception as exception:
            raise Exception(f'cannot save to db !! {str(exception)}')
        finally:
            session.close()

    def __repr__(self):
        return str(self.__dict__)
