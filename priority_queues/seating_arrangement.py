from queue import PriorityQueue

def seating_order(width_of_seats, n, order):
    width_row_details = [[-width_of_seats[i], i+1] for i in range(n)]
    width_row_details.sort(reverse=True)
    pq = PriorityQueue()
    index = 0
    res = []
    for char in order:
        if char == "0":
            res.append(width_row_details[index][1])
            pq.put(width_row_details[index])
            index += 1
        else:
            res.append(pq.get()[1])
    print(*res)

if __name__ == "__main__":
    n = int(input())
    width_of_seats = list(map(int, input().split()))
    order = input()
    seating_order(width_of_seats, n, order)