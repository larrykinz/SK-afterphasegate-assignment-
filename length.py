def king_length(input_string):
    length = 0
    while True:
        try:
            input_string[length]
            length += 1
        except IndexError:
            break
    return length
print(king_length("kkiyvfgv"))

