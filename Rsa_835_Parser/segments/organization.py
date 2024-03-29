""" Organization segment """
from rsa_835_parser.elements.identifier import Identifier
from rsa_835_parser.elements.organization_type import OrganizationType
from rsa_835_parser.segments.utilities import split_segment

class Organization:
    """ Organization (N1) segment """

    identification = 'N1'

    identifier = Identifier()
    type = OrganizationType()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.type = segment[1]
        self.name = segment[2]
        self.identification_code = int(segment[4]) if len(segment) >= 5 else None

    def __repr__(self):
        return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
    pass
