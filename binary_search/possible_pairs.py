if __name__ == "__main__":
    n, m, k = map(int, input().split())
    new_players = list(map(int, input().split()))
    old_players = list(map(int, input().split()))
    
    new_players.sort()
    old_players.sort()
    
    for i in range(n):
        new_players[i] += k 
    
    no_of_pairs = 0
    j = 0
    for i, player in enumerate(new_players):
        while j < m and old_players[j] <= player:
            j += 1 
        if j == m:
            break
        no_of_pairs += m - j
    print(no_of_pairs)        
    
    