string = "{ [] {[(]}} {{[()]} }"
string = "".join(string.split())
string_tmp = ""
collisions = {}


def close_char(char):
    if char == "{": return "}"
    if char == "[": return "]"
    if char == "(": return ")"


i = 0
for ch in string:
    if ch in "{[(":
        string_tmp += ch
    else:
        if ch == close_char(string_tmp[-1]):
            string_tmp = string_tmp[:-1]
        else:
            string_tmp = string_tmp[:-1]
            collisions[string[i-1]] = [i-1, False]
            string = string[:i-1:]+string[i:]
            if len(string_tmp) == 0 or ch == close_char(string_tmp[-1]):
                string_tmp = string_tmp[:-1]
            print(string)

    i += 1

print(collisions)


