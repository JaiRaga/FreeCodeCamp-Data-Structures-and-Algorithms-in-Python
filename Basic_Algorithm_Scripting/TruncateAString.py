def truncateString(s, num):
    if len(s) <= num:
        return s
    return s[:num]+"..."

print(truncateString("A-tisket a-tasket A green and yellow basket", 8))
print(truncateString("Peter Piper picked a peck of pickled peppers", 11))
print(truncateString("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket")))
print(truncateString("A-", 1))