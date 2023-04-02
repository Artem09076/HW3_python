s=str(input())
letter="f"
def find_indices(s, letter, offset=0):
    if len(s) == 0:
        return []
    elif s[0] == letter:
        return [offset] + find_indices(s[1:], letter, offset+1)
    else:
        return find_indices(s[1:], letter, offset+1)
print(*find_indices(s, letter, offset=0))