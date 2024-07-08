import re


def normalize_phone(phone_number: str) -> str:
    trimmed = ''.join(re.findall(r"\+?\d+", phone_number))
    if not re.search(r"\+", trimmed):
        trimmed = f"+380{trimmed[len(trimmed) - 9:]}"

    return trimmed
