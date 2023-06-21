import math


class VigenereCipher:
    @classmethod
    def encrypt(self, text: str, key: str) -> str:
        key = self._get_key(text, key)
        text_ac, key_ac = self._get_ascii(text, key)

        ascii_code = []
        for i in range(len(text)):
            code = text_ac[i] + key_ac[i]
            code = code if code < 0 else code + 255
            ascii_code.append(chr(code))

        return "".join(ascii_code)

    @classmethod
    def decrypt(self, text: str, key: str) -> str:
        key = self._get_key(text, key)
        text_ac, key_ac = self._get_ascii(text, key)
        ascii_code = []
        for i in range(len(text)):
            print(f"{text_ac[i]}  {key_ac[i]} <= {text[i]}")
            code = text_ac[i] - key_ac[i]
            code = code if code <= 255 else code - 255
            code = code if code >= 0 else code + 255
            ascii_code.append(chr(code))

        return "".join(ascii_code)

    def _get_key(text: str, key: str) -> str:
        amount = math.floor(len(text) / len(key))
        return amount * key + key[: len(text) - amount * len(key)]

    def _get_ascii(text: str, key: str) -> tuple[str, str]:
        text_ac = [ord(char) for char in text]
        key_ac = [ord(char) for char in key]
        return text_ac, key_ac


print(VigenereCipher.decrypt("ƶŐƧȡ", "h189G%@A8AWFfbwahg!#"))
"+-0+-0+-0+0-0+0000-+0-00+-+-000+0000-"
