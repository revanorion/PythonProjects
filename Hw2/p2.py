def find_dup_str(s, n):
    for c in range(n, len(s)):
        if s[c:].find(s[c - n:c]) > -1:
            return s[c - n:c]
    return ""


def find_max_dups(s):
    max = ""
    for n in range(0, len(s)):
        result = find_dup_str(s, n)
        if len(result) > len(max):
            max = result
    return max

s = input("Enter a string to test for duplicate: ")
n = int(input("Enter the size of the duplicate: "))
print("Result of s = %s, n = %d\t%s" % (s, n, find_dup_str(s, n)))
print("Result max of s = %s\t%s" % (s, find_max_dups(s)))
