

# Problem: https://neetcode.io/problems/foreign-dictionary

# Alien Dictionary
# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

# Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

# The first letter where they differ is smaller in a than in b.
# There is no index i such that a[i] != b[i] and a.length < b.length.


# Example

# Input: ["hrn","hrf","er","enn","rfnn"]

# Output: "hernf"

# Explanation:

# from "hrn" and "hrf", we know 'n' < 'f'
# from "hrf" and "er", we know 'h' < 'e'
# from "er" and "enn", we know get 'r' < 'n'
# from "enn" and "rfnn" we know 'e'<'r'
# so one possibile solution is "hernf"

# Youtube: https://www.youtube.com/watch?v=U3N_je7tWAs&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=17

from collections import defaultdict, deque


def alien_order(words):
    
    # Step1 - Build Graph
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    # Step 2: Create edges
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))

        # Edge case: Check invalid case like ["abc", "ab"]
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                    break
    
    # Step 3: Topological Sort using Kahn's Algorithm
    queue = deque([ char for char in in_degree if in_degree[char] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbour in graph[char]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)
    # If all characters are not used, there was a cycle (invalid order)
    if len(result) < len(in_degree):
        return ""
    
    return "".join(result)


if __name__ == "__main__":

    # Example Test Cases
    print(alien_order(["z", "o"]))                    # Output: "zo"
    print(alien_order(["hrn", "hrf", "er", "enn", "rfnn"]))  # Output: "hernf" or other valid topo order

            
            
