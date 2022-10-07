def angram_check(s1, s2):
    if (sorted(s1) == sorted(s2)):
        check = "The strings are Anagrams."
    else:
        check = "The strings aren't Anagrams."
    return check


if __name__ == "__Main__":
    print("Enter first String: ", end="")
    s1 = input()
    print("Enter Second String:", end="")
    s2 = input()
    output = angram_check(s1, s2)
    print(output)
