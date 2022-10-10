def to_jaden_case(string):
    # ...
    newString = ""
    for word in string.split():
        newString += word.capitalize() + " "
    return newString.strip()


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
