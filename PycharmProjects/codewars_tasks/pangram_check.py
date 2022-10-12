def check_pangram(text:str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabet:
        if ch not in text.lower():
            return False
    return True

print(check_pangram("ABCDEF"))