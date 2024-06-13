
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    print("Caesar Cipher, a shift cypher program.")
    print()

    while True:
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()
        if response == 'e':
            mode = "encrypt"
            break
        elif response == 'd':
            mode = "decrypt"
            break

    while True:
        maxKey = len(SYMBOLS) - 1
        print("Please input the key (0-{} to use.)".format(maxKey))
        response = input("> ").upper()
        if not response.isdecimal():
            continue

        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break

    print("Enter the message to {}".format(mode))
    msg = input("> ").upper()
    translated = ""

    for symbol in msg:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == "encrypt":
                num += key
            elif mode == "decrypt":
                num -= key

            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:
                num += len(SYMBOLS)

            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol

    print(translated)


if __name__ == "__main__":
    main()
