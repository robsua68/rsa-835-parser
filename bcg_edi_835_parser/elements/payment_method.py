""" Payment Method (BPR04) """
from Bcg_Edi_835_Parser.elements import Element

payment_methods = {"ACH": "automatic deposit", "CHK": "check", "NON": "no payment"}


class PaymentMethod(Element):
    """Payment Method Class"""

    def parser(self, value: str) -> str:
        value = value.strip()
        return payment_methods.get(value, value)
