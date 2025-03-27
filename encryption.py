from random import randint

def emoji_encryption(text: str, emojies: list):
    return ''.join(emojies[int(bit)][randint(0, 49)] for bit in '2'.join(format(byte, '08b') for byte in text.encode()))

if __name__=="__main__":
    with open("files/emoji.txt", 'r', encoding='utf-8') as file:
        emojies = file.readlines()
    print(emoji_encryption('Parsa Safaie', emojies=emojies))