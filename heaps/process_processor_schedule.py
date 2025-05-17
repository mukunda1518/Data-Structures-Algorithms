import heapq


def get_minimum_time(process_sizes, capacity):
    max_capcity = max(capacity)
    max_process_size = max(process_sizes)
    if max_process_size > max_capcity:
        return -1

    # sort the processes by size largest
    processes = sorted(process_sizes, reverse=True)
    
    # create a min heap for available processors
    # format: (time_available, -processor_capacity)
    processors = [(0, -capacity[i]) for i in range(len(capacity))]
    heapq.heapify(processors)
    
    for size in processes:
        # try to find a capable processor
        temp_processors = []
        found_capable = False
        
        while processors and not found_capable:
            time, capacity = heapq.heappop(processors)
            
            if -capacity >= size:  # this processor can handle the process
                heapq.heappush(processors, (time + 2, capacity))  # +2 for execute + pause
                found_capable = True
            else:
                temp_processors.append((time, capacity))
        
        if not found_capable:
            return -1  # no capable processor found
        
        for proc in temp_processors:
            heapq.heappush(processors, proc)
        
    return max(0, max(time for time, _ in processors) - 1)


if __name__ == "__main__":
    process_sizes = [7, 2, 6, 5, 4]
    capacity = [8, 3, 5]
    print(get_minimum_time(process_sizes, capacity))
