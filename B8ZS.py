import re


class B8ZS:
    @classmethod
    def encode(self, text: str) -> str:
        binary = self._encode_to_binary(text)
        print(len(binary))
        ami = self._encode_to_ami(binary)
        return self._encode_b8zs(ami)

    @classmethod
    def decode(self, text: str) -> str:
        ami = self._decode_b8zs(text)
        binary = self._decode_ami(ami)
        print(binary)
        return self._decode_binary(binary)

    def _decode_b8zs(text: str) -> str:
        decoded = text.replace("000+-0-+", "00000000")
        return decoded.replace("000-+0+-", "00000000")

    def _decode_ami(text: str) -> str:
        decoded = text.replace("+", "1")
        return decoded.replace("-", "1")

    def _decode_binary(text: str) -> str:
        binary_chunks = [text[i : i + 8] for i in range(0, len(text), 8)]
        characters = [chr(int(chunk, 2)) for chunk in binary_chunks]
        return "".join(characters)

    def _encode_to_binary(text: str) -> str:
        binaries = [bin(ord(char))[2:].zfill(8) for char in text]
        print(binaries)
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


print(B8ZS.decode("+-0+-0+-0+0-0+0000-+0-00+-+-000+0000-"))
