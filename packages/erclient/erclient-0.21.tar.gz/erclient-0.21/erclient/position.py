from functools import lru_cache

from .base import ErConnector
from .contact import Contact, Company
from .department import get_department_by_id
from .foldergroup import FolderGroup

class Position(object):

    def __init__(self, position_id, data=None):
        self.position_id = position_id
        if not data:
            # Fetch from remote
            self.refresh()
        else:
            # Allows it to be populated by list methods without an additional fetch
            self.data = data
        self.populate_from_data()

    def refresh(self):
        self.data = get_position_by_id(self.position_id).data
        self.populate_from_data()

    def populate_from_data(self):
        self.title = self.data.get('Title', None)
        self.web_description = self.data.get('WebDescription', None)
        self.contact_id = self.data.get('ContactID', None)
        self.department_id = self.data.get('PrimaryDepartmentID', None)
        self.type_id = self.data.get('TypeID', None)

    def department(self):
        return get_department_by_id(self.department_id)

    def contact(self):
        return Contact(self.contact_id)

    def type(self):
        return PositionType(self.type_id)

class PostedPosition(object):
    # PostedPosition is generated from the Position/InternallyPosted api call and the data is different than the
    # standard Position call
    def __init__(self, data):
        self.data = data
        self.populate_from_data()

    def refresh(self):
        self.data = get_position_by_id(self.position_id)
        self.populate_from_data()

    def populate_from_data(self):
        self.position_id = self.data.get('ID')
        self.web_position_title = self.data.get('WebPositionTitle', None)
        self.web_description = self.data.get('WebDescription', None)
        self.company_id = self.data.get('CompanyID', None)

    def address(self):
        return PostedPositionAddress(data=self.data.get('PrimaryAddress', {}))

    def company(self):
        try:
            return Company(company_id=self.company_id)
        except:
            return None

    def foldergroup(self):
        foldergroup_data = self.data.get('FolderGroup', None)
        try:
            return FolderGroup(foldergroup_id=foldergroup_data['ID'], data=foldergroup_data)
        except:
            return None

    def position(self):
        return Position(self.position_id)

class PostedPositionAddress(object):
    # PostedPositionAddress is generated from the Position/InternallyPosted api call and the data is different than the
    # standard Address obj in that it cannot be identified by a keyfield
    def __init__(self, data):
        self.data = data
        self.populate_from_data()

    def populate_from_data(self):
        self.address_line_1 = self.data.get('AddressLine1', None)
        self.address_line_2 = self.data.get('AddressLine2', None)
        self.city = self.data.get('City', None)
        self.region = self.data.get('Region', None)
        self.state = self.data.get('State', None)
        self.postal_code = self.data.get('PostalCode', None)
        self.latitude = self.data.get('Latitude', None)
        self.longitude = self.data.get('Longitude', None)

class PositionType(object):

    def __init__(self, positiontype_id, data=None):
        self.positiontype_id = positiontype_id
        if not data:
            # Fetch from remote
            self.refresh()
        else:
            # Allows it to be populated by list methods without an additional fetch
            self.data = data
        self.populate_from_data()

    def refresh(self):
        self.data = get_positiontype_by_id(self.positiontype_id).data
        self.populate_from_data()

    def populate_from_data(self):
        self.name = self.data.get('Name', None)
        self.category_id = self.data.get('CategoryID', None)
        self.subcategory_id = self.data.get('SubCategoryID', None)

def get_position_by_id(position_id):
    connector = ErConnector()  # 2.0 API
    url = 'Position/{id}'.format(
        id=position_id,
    )
    response = connector.send_request(
        path=url,
        verb='GET',
    )

    return Position(response['ID'], data=response)


def list_positions():
    # Currently it is not possible to list all positions. this method is an alias for list_posted_positions
    return list_posted_positions()

def list_posted_positions():
    connector = ErConnector()
    url = 'Position/InternallyPosted'
    response = connector.send_request(
        path=url,
        verb='GET',
    )
    return [PostedPosition(data) for data in response]

def get_posted_position_by_id(position_id):
    try:
        return [posted_position for posted_position in list_posted_positions() if posted_position.position_id==position_id][0]
    except Exception as E:
        return E



def get_positiontype_by_id(positiontype_id):
    connector = ErConnector()  # 2.0 API
    url = 'Position/Type/{id}'.format(
        id=positiontype_id,
    )
    response = connector.send_request(
        path=url,
        verb='GET',
    )

    return PositionType(response['ID'], data=response)


def list_positiontypes():
    connector = ErConnector()
    url = 'Position/Type'
    response = connector.send_request(
        path=url,
        verb='GET',
    )
    return response