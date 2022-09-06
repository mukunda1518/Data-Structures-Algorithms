def get_max_in_window_x(customers, x, n):
    max_ = 0
    sum_ = 0
    for i in range(n):
        sum_ += customers[i]
        if i >= x:
            sum_ -= customers[i-x]
        max_ = max(max_, sum_)
    return max_

def max_statisfed_customer(customers, sleepy, n, x):
    satisfy_cus_sum = 0
    for i in range(n):
        if sleepy[i] == 0:
            satisfy_cus_sum += customers[i]
            customers[i] = 0
    return satisfy_cus_sum + get_max_in_window_x(customers, x, n)

if __name__ == "__main__":
    n, x = map(int, input().split())
    customers = list(map(int, input().split()))
    sleepy = list(map(int, input().split()))
    
    print(max_statisfed_customer(customers, sleepy, n, x))
    