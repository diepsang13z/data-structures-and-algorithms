class TrieNode:

    def __init__(self) -> None:
        self.child: list[str] = [None] * 26
        self.isLeaf: bool = False


class Trie:

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for char in word:
            index = self._get_char_index(char)
            if not curr_node.child[index]:
                curr_node.child[index] = TrieNode()
            curr_node = curr_node.child[index]
        curr_node.isLeaf = True

    def search(self, word: str) -> bool:
        curr_node: TrieNode = self.root
        for char in word:
            index = self._get_char_index(char)
            if not curr_node.child[index]:
                return False
            curr_node = curr_node.child[index]
        return (curr_node.isLeaf) and (curr_node is not None)

    def start_with(self, prefix: str) -> bool:
        curr_node: TrieNode = self.root
        for char in prefix:
            index = self._get_char_index(char)
            if not curr_node.child[index]:
                return False
            curr_node = curr_node.child[index]
        return True

    def remove(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for char in word:
            index = self._get_char_index(char)
            if not curr_node.child[index]:
                raise ValueError('Word not found')
            curr_node = curr_node.child[index]
        curr_node.isLeaf = False

    def _get_char_index(self, char: str):
        return ord(char) - ord('a')


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
