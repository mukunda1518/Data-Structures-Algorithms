if __name__ == "__main__":
    m, n = map(int, input().split())
    difficulty = list(map(int, input().split()))
    points = list(map(int, input().split()))
    potential = list(map(int, input().split()))

    challenges = []
    for i in range(m):
        challenges.append((difficulty[i], points[i]))
    challenges.sort()
    potential.sort()
    max_points = 0
    j = 0
    total_points = 0
    for i in range(n):
        while j < m and potential[i] >= challenges[j][0]:
            max_points = max(max_points, challenges[j][1])
            j += 1
        total_points += max_points
    print(total_points)


