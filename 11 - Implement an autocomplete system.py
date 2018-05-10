"""

Good morning. Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False

def char_to_index(ch):
    return ord(ch)-ord('a')

def index_to_char(index):
    return chr(index+ord('a'))

def build_trie(possible_words):
    root_node = TrieNode()
    for word in possible_words:
        current_node = root_node
        for letter in word:
            if not current_node.children[char_to_index(letter)]:
                current_node.children[char_to_index(letter)] = TrieNode()
            current_node = current_node.children[char_to_index(letter)]
        current_node.is_end_of_word = True
    return root_node

def autocomplete(query_string, possible_words):
    current_node = build_trie(possible_words)
    word_list = []
    prefix = query_string
    for letter in query_string:
        if not current_node.children[char_to_index(letter)]:
            return word_list
        current_node = current_node.children[char_to_index(letter)]
    if current_node.is_end_of_word:
        word_list.append(prefix)
    def get_words(node, prefix):
        for index, child in enumerate(node.children):
            if child:
                get_words(child, prefix+index_to_char(index))
                if child.is_end_of_word:
                    word_list.append(prefix+index_to_char(index))
    get_words(current_node, prefix)
    return word_list

assert autocomplete('de', ['dog', 'deer', 'deal']) == ['deal', 'deer']
assert autocomplete('hel', ['hello', 'dog', 'hell', 'cat', 'hel', 'help', 'helps', 'helpings']) == ['hel', 'hello', 'hell', 'helpings', 'helps', 'help']
