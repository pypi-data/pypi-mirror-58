""" Country-specific functions for converting IBAN to BBAN """


def finnish_iban_to_bban(iban: str) -> str:
    """
    Convert a Finnish bank account number from IBAN to BBAN machine language format.

    :param iban: Account number in IBAN format
    :return: Account number in BBAN machine language format
    :raises ValueError: If IBAN is in incorrect format
    """
    len_iban = len(iban)

    if len_iban == 18:
        if iban[4] in ('4', '5'):
            bban = iban[4:10] + '0' + iban[10] + '0' + iban[11:]
        else:
            bban = iban[4:10] + '00' + iban[10:]
    else:
        raise ValueError('IBAN is in incorrect format')

    return bban
