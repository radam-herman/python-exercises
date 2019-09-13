def normalize_name(s):
    s = s.strip()
    char_check = ["abcdefghijklmnopqrstuvwxyz0123456789_"]
    if s[0].isdigit():
        print("must not begin with a number")
    else:
        for char in s:
            if char.lower not in char_check:
                if char == " ":
                    s.lower().replace(" ", "_")
                else:
                    s.lower().replace(char, "")
    return s.lower()


