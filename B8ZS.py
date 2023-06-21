import re
from VigenereCipher import *

class B8ZS:
    @classmethod
    def encode(self, text: str) -> str:
        binary = self._encode_to_binary(text)
        ami = self._encode_to_ami(binary)
        return self._encode_b8zs(ami)

    @classmethod
    def decode(self, text: str) -> str:
        ami = self._decode_b8zs(text)
        binary = self._decode_ami(ami)
        return self._decode_binary(binary)

    def _decode_b8zs(text: str) -> str:
        decoded = text.replace("000+-0-+", "00000000")
        return decoded.replace("000-+0+-", "00000000")

    def _decode_ami(text: str) -> str:
        decoded = text.replace("+", "1")
        return decoded.replace("-", "1")

    def _decode_binary(text: str) -> str:
        binary_chunks = [text[i : i + 10] for i in range(0, len(text), 10)]
        characters = [chr(int(chunk, 2)) for chunk in binary_chunks]
        return "".join(characters)

    def _encode_to_binary(text: str) -> str:
        binaries = [bin(ord(char))[2:].zfill(10) for char in text]
        return "".join(binaries)

    def _encode_to_ami(text: str) -> str:
        result = ""

        flag = True

        for char in text:
            if char == "1":
                result += "+" if flag else "-"
                flag = not flag
            else:
                result += char

        return result

    def _encode_b8zs(text: str) -> str:
        pattern = r"(?=0{8})"
        matches = re.finditer(pattern, text)
        indices = [match.start() for match in matches]
        next = 0
        b8zs = list(text)
        for i in indices:
            if i < next:
                continue
            if i == 0 or text[i - 1] == "+":
                b8zs[i : i + 8] = "000+-0-+"
            else:
                b8zs[i : i + 8] = "000-+0+-"
            next = i + 8

        return "".join(b8zs)


# a = "O pé do chulé tem zé, o Lee caminhões, o Lucas florais xing xong, o Diogo ni hao xie xie wo de peng you, garret crînge"
# key = "h189G%@A8AWFfbwahg!#"

# step1 = VigenereCipher.encrypt(a, key)
# print("#### STEP1: encrypted ####")
# print(step1)
# step2 = B8ZS.encode(step1)
# print("#### STEP2: encoded ####")
# print(step2)
# step3 = B8ZS.decode(step2)
# print("#### STEP3: decoded ####")
# print(step3)
# step4 = VigenereCipher.decrypt(step3, key)
# print("#### STEP4: decrypted ####")
# print(step4)
