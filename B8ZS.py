import re


class B8ZS:
    @classmethod
    def execute(self, text: str) -> str:
        binary = self._convert_to_binary(text)
        print(f"BINARY\n {binary}\n\n")
        ami = self._convert_to_ami(binary)
        print(f"AMI\n {ami}\n\n")
        b8zs = self._execute_b8zs(ami)
        print(f"b8zs\n {b8zs}\n")

        return b8zs

    def _convert_to_binary(text: str) -> str:
        binaries = [bin(ord(char))[2:].zfill(8) for char in text]
        return "".join(binaries)

    def _convert_to_ami(text: str) -> str:
        result = ""

        flag = True

        for char in text:
            if char == "1":
                result += "+" if flag else "-"
                flag = not flag
            else:
                result += char

        return result

    def _execute_b8zs(text: str) -> str:
        pattern = r"(?=0{8})"
        matches = re.finditer(pattern, text)
        indices = [match.start() for match in matches]
        next = 0
        b8zs = list(text)
        for i in indices:
            if i < next:
                continue
            if i == 0 or text[i - 1] == "+":
                b8zs[i: i + 8] = "000+-0-+"
            else:
                b8zs[i: i + 8] = "000-+0+-"
            next = i + 8

        return "".join(b8zs)


B8ZS.execute("Bom dia meu guri véio bora come farinha!!")
