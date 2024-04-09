def toBacon(text):
    ABdictionary = {
        'a': 'AAAAA', 'b': 'AAAAB', 'c': 'AAABA', 'd': 'AAABB', 'e': 'AABAA',
        'f': 'AABAB', 'g': 'AABBA', 'h': 'AABBB', 'i': 'ABAAA', 'j': 'ABAAB',
        'k': 'ABABA', 'l': 'ABABB', 'm': 'ABBAA', 'n': 'ABBAB', 'o': 'ABBBA',
        'p': 'ABBBB', 'q': 'BAAAA', 'r': 'BAAAB', 's': 'BAABA', 't': 'BAABB',
        'u': 'BABAA', 'v': 'BABAB', 'w': 'BABBA', 'x': 'BABBB', 'y': 'BBAAA',
        'z': 'BBAAB', ' ': 'BBBBB'
    }

    binaryDictionary = {
        'a': '00000', 'b': '00001', 'c': '00010', 'd': '00011', 'e': '00100',
        'f': '00101', 'g': '00110', 'h': '00111', 'i': '01000', 'j': '01001',
        'k': '01010', 'l': '01011', 'm': '01100', 'n': '01101', 'o': '01110',
        'p': '01111', 'q': '10000', 'r': '10001', 's': '10010', 't': '10011',
        'u': '10100', 'v': '10101', 'w': '10110', 'x': '10111', 'y': '11000',
        'z': '11001', ' ': '11111'
    }

    encodedAlpha = ''
    encodedBinary = ''
    
    for char in text.lower():
        if char in ABdictionary:
            encodedAlpha += ABdictionary[char]
            encodedBinary += binaryDictionary[char]
        else:
            encodedAlpha += char
            encodedBinary += char
            
    return encodedAlpha, encodedBinary

inputText = input("Enter plaintext: ")

encodedAlpha, encodedBinary = toBacon(inputText)

print("Bacon code: ", encodedAlpha)
print("Binary code: ", encodedBinary)