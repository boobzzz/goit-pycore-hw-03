import re

num_len = 9


def normalize_phone(phone_number: str) -> str:
    trimmed = ''.join(re.findall(r"\+380|\d+", phone_number))

    if not re.search(r"\+380", trimmed):
        trimmed = f"+380{trimmed[len(trimmed) - num_len:]}"

    return trimmed
