# Leetcode: https://leetcode.com/problems/diameter-of-binary-tree/

# https://www.youtube.com/watch?v=Rezetez59Nk



# Rule1: Longest path between 2 nodes
# Rule2: Path does not need to pass via root

maxi = 0

def get_height(root):
    if root is None:
        return 0
    left_depth = get_height(root.left)
    right_depth = get_height(root.right)
    return max(left_depth, right_depth) + 1


# Bruteforce Approach
def find_max_bruteforce_approach(root):
    if not root:
        return
    global maxi
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    maxi = max(maxi, left_height + right_height)

    find_max_bruteforce_approach(root.left)
    find_max_bruteforce_approach(root.right)


def find_max_optimized_approach(root, maxi):
    if not root:
        return 0

    lh = find_max_optimized_approach(root.left, maxi)
    rh = find_max_optimized_approach(root.right, maxi)

    maxi = max(maxi, lh + rh)
    return 1 + max(lh, rh), maxi




