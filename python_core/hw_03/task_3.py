import re

def normalize_phone(phone_number: str) -> str:
    pattern = "[^0-9]"
    phone_number_without_symbols = re.sub(pattern, "", phone_number)

    if phone_number_without_symbols.find('38') == 0:
        return f"+{phone_number_without_symbols}"
    elif phone_number_without_symbols.find('+38') == 0:
        return f"{phone_number_without_symbols}"
    else:
        return f"+38{phone_number_without_symbols}"