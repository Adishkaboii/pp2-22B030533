def permute(s):
    if len(s) == 0:
        return ['']
    
    result = []
    
    for i in range(len(s)):
        sub_permutes = permute(s[:i] + s[i+1:])
        for sub_permute in sub_permutes:
            result.append(s[i] + sub_permute)
    
    return result

s = input()
print(permute(s))
