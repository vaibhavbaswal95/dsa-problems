from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    # Sort the strings
    strs.sort()

    # Use first and last string after sorting
    first_str = strs[0]
    last_str = strs[-1]
    common_prefix = []

    # Find the minimum length between the first and last string
    min_length = min(len(first_str), len(last_str))

    for i in range(min_length):
        if first_str[i] == last_str[i]:
            common_prefix.append(first_str[i])
        else:
            break

    return ''.join(common_prefix)