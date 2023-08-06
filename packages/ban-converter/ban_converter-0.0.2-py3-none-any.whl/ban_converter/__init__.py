""" Functions for converting bank account numbers between BBAN and IBAN formats. """

__version__ = '0.0.2'

from ban_converter import bban_to_iban as bti
from ban_converter import iban_to_bban as itb


def convert_bban_to_iban(bban: str, country_code: str = 'FI') -> str:
    """
    Convert a bank account number from BBAN to IBAN format.

    :param bban: Account number in BBAN format
    :param country_code: Account ISO 3166 country code, defaults to 'FI' (Finland)
    :return: Account number in IBAN format
    :raises ValueError: If the country is not supported
    """
    if country_code == 'FI':
        iban = bti.finnish_bban_to_iban(bban)
    else:
        raise ValueError('This country is not supported.')

    return iban


def convert_iban_to_bban(iban: str) -> str:
    """
    Convert a bank account number from IBAN to BBAN manchine language format.

    :param iban: Account number in IBAN format
    :return: Account number in BBAN machine language format
    :raises ValueError: If the country is not supported
    """
    country_code = iban[:2]

    if country_code == 'FI':
        bban = itb.finnish_iban_to_bban(iban)
    else:
        raise ValueError('This country is not supported.')

    return bban
