def preprocess(text: str) -> str:
    return ''.join(char for char in text.lower() if char.isalpha())