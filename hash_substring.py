# 221RDB405 Ralfs Rozenbergs
# python3

def read_input():
    input_type = input()
    pattern = ""
    text = ""
    if "F" in input_type:
        try:
            file = open("tests/06","r")
            lines = file.readlines()
            pattern = lines[0]
            text = lines[1]
            file.close()
        except Exception:
            print("File not found")
    elif "I" in input_type:
        pattern = input()
        text = input()
    else:
        print("Incorrect format - choose I or F")

    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    patternhash = 0
    result = []
    textlen = len(text)
    patternlen = len(pattern)
    
    for i in range(patternlen):
        patternhash = patternhash+ord(pattern[i])
    for i in range(textlen-patternlen+1):
        texthash = 0
        for j in range(patternlen):
            texthash = texthash + ord(text[i+j])
        if texthash == patternhash:
            if text[i:i+patternlen] == pattern:
                result.append(i)
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))