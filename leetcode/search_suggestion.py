'''

https://leetcode.com/problems/search-suggestions-system/

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.


NOTE:
=====
I know the solution below is almost BS and slow, but i wanted to 
do it using trie.

'''

from Listin import List

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.completeWord = ''
    
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, letters):
        currNode = self.root
        
        i = 0
        while i < len(letters):
            letter = letters[i]
            if letter not in currNode.children:
                currNode.children[letter] = TrieNode()
            
            currNode = currNode.children[letter]
            i += 1
        
        currNode.isWord = True
        currNode.completeWord = letters
    
    def getWordsStartingWith( self, letters):
        
        currNode = self.getLastNode(letters)
        words = []
        self.getWords(currNode, words)
        
        return words
        
    def getWords( self, currNode, words ):
        if currNode == '':
            return
        
        if len(words) == 3:
            return
        
        if currNode.isWord:
            words.append(currNode.completeWord)
            if not currNode.children:
                return
        
        if len(words) == 3:
            return
        
        for prefix in currNode.children:
            self.getWords(currNode.children[prefix], words)

            
    def getLastNode(self, letters):
        
        currNode = self.root
        i = 0
        while i < len(letters):
            letter = letters[i]
            if letter in currNode.children:
                currNode = currNode.children[letter]
            else:
                currNode = ''
                break
            i += 1
        
        return currNode
                    


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        
        for word in sorted(products):
            trie.insert(word)
        
        suggestions = []
        i = 1
        
        while i <= len(searchWord):
            words = trie.getWordsStartingWith(searchWord[:i])
            suggestions.append(words)
            i += 1
        
        return suggestions
        
