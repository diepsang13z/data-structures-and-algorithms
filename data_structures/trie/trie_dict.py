class TrieNode:

    def __init__(self) -> None:
        self.child: dict = {}
        self.isLeaf: bool = False


class Trie:

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for char in word:
            if char not in curr_node.child:
                curr_node.child[char] = TrieNode()
            curr_node = curr_node.child[char]
        curr_node.isLeaf = True

    def search(self, word: str) -> bool:
        curr_node: TrieNode = self.root
        for char in word:
            if char not in curr_node.child:
                return False
            curr_node = curr_node.child[char]
        return (curr_node.isLeaf) and (curr_node is not None)

    def start_with(self, prefix: str) -> bool:
        curr_node: TrieNode = self.root
        for char in prefix:
            if char not in curr_node.child:
                return False
            curr_node = curr_node.child[char]
        return True

    def remove(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for char in word:
            if char not in curr_node.child:
                raise ValueError('Word not found')
            curr_node = curr_node.child[char]
        curr_node.isLeaf = False


def main():
    trie = Trie()

    trie.insert('car')
    trie.insert('card')
    trie.insert('chip')
    trie.insert('trie')
    trie.insert('try')

    print(trie.search('car'))
    print(trie.search('card'))
    print(trie.search('ca'))
    print(trie.search('cat'))

    print(trie.start_with('car'))
    print(trie.start_with('card'))
    print(trie.start_with('ca'))
    print(trie.start_with('cat'))

    trie.remove('try')
    print(trie.search('try'))


if __name__ == '__main__':
    main()
