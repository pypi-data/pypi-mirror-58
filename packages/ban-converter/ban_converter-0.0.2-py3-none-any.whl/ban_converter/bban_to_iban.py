""" Country-specific functions for converting BBAN to IBAN """


def finnish_bban_to_iban(bban: str) -> str:
    """
    Convert a Finnish BBAN to IBAN.

    :param bban: Account number in BBAN format
    :return: Account number in IBAN format
    :raises ValueError: If BBAN is too short or too long
    """
    country = 'FI'
    len_orig = len(bban)
    bban_no_dash = bban.replace('-', '')
    len_bban_no_dash = len(bban_no_dash)
    zeros = '0000000'

    if len_orig == 16 and bban.find('-') == -1:
        account_number = bban[0:4] + bban[5:8] + bban[9:]
    elif bban_no_dash[0] in ('4', '5'):
        if 8 <= len_bban_no_dash <= 13:
            account_number = bban_no_dash[0:7] + zeros[:(14 - len_bban_no_dash)]\
                             + bban_no_dash[7:]
        else:
            account_number = bban_no_dash
    elif 7 <= len_bban_no_dash <= 13:
        account_number = bban_no_dash[0:6] + zeros[:(14 - len_bban_no_dash)]\
                         + bban_no_dash[6:]
    elif len_bban_no_dash < 7:
        raise ValueError('BBAN is too short')
    else:
        raise ValueError('BBAN is too long')

    checksum = 98 - int(account_number + '151800') % 97
    iban = country + (zeros + str(checksum))[-2:] + account_number

    return iban
