class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        # used as dictionary for the letter and children of that letter

    def words(self, char):
        if self.end:
            yield char
        for letter, child in self.children.items():
            yield from child.words(char + letter)

            # after thorough reasearch, I found that using yield instead
            #   of return allows the function to continue, fixing some of the
            #   error I was having.

class TrieStructure:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for letters in word:
            new = current.children.get(letters)
            if not new:
                new = Node()
                current.children[letters] = new
            current = new
        current.end = True
    
    def all_words(self, char):
        current = self.root
        for L in char:
            current = current.children.get(L)
            if current is None:
                return  # No words with given char

        yield from current.words(char)


def create_trie(trie):

    # reads from Library.txt which contains all the words
    with open("Library.txt", "r") as L:
        lines = L.readlines()

    # removes the \n from each word
    new = []
    for words in lines:
        words = words.strip("\n")
        new.append(words)

    # inserts each word into the trie
    for word in new:
        trie.insert(word)

def printTrie(words):

    if words == []:
        print("*** None ***")
    
    for word in words:
        print(word)


def main():

    trie = TrieStructure()
    create_trie(trie)

    run = True

    while run == True:
        print()
        char = input("Enter characters: ")
        words = list(trie.all_words(char))
        print()
        printTrie(words)
        print()
        again = input("Again? ")
        if again == "no":
            run == False

#main()
