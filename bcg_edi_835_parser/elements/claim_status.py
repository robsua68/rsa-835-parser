from bcg_edi_835_parser.elements import Element

class ClaimStatus(Element):
    """Claim Status"""

    # todo: https://x12.org/codes/claim-status-codes
    
    def parser(self, value: str) -> int:
        return int(value)