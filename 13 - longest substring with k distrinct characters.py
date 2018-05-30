"""

good morning. here's your coding interview problem for today.

this problem was asked by amazon.

given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

for example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

upgrade to premium and get in-depth solutions to every problem.

if you liked this problem, feel free to forward it along! as always, shoot us an email if there's anything we can help with!

"""

def longest_substring_with_distinct_characters(s, k):
    start_index = 0
    max_window_size = 0

    max_window_start = 0
    max_window_end = 0

    unique_char_dict = dict()
    unique_char_set = set()
    for i in range(len(s)):
        if s[i] not in unique_char_dict:
            unique_char_dict[s[i]] = 0
        unique_char_dict[s[i]] += 1
        unique_char_set.add(s[i])

        while len(unique_char_set) > k:
            unique_char_dict[s[start_index]] -= 1
            if unique_char_dict[s[start_index]] == 0:
                unique_char_set.remove(s[start_index])
            start_index += 1

        if i + 1 - start_index > max_window_size:
            max_window_size = i + 1 - start_index
            max_window_start = start_index
            max_window_end = i + 1
    return s[max_window_start:max_window_end]

assert longest_substring_with_distinct_characters("abcba", 2) == "bcb"
assert longest_substring_with_distinct_characters("aabacbebebe", 3) == "cbebebe"
