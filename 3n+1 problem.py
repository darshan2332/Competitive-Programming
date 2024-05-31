def cycle_length(n): 
    length = 1 
    while n != 1: 
        if n % 2 == 0: 
            n = n / 2 
        else: 
            n = 3 * n + 1 
        length += 1 
    return length 
 
def max_cycle_length(i, j): 
    max_length = 0 
    for num in range(i, j+1): 
        current_length = cycle_length(num) 
        if current_length > max_length: 
            max_length = current_length 
    return max_length 
 
# Reading input pairs and calculating maximum cycle lengths 
while True: 
    try: 
        line = input() 
        if not line: 
            break 
        i, j = map(int, line.split()) 
        result = max_cycle_length(i, j) 
        print(f"{i} {j} {result}") 
    except ValueError: 
        print("Invalid input") 
