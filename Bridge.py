num_cases = int(input())
for _ in range(num_cases):
    n = int(input())
    times = sorted(int(input()) for _ in range(n))
    total_time = 0
    strategy = []
    if n == 1:
        total_time = times[0]
        strategy.append((times[0],))
    else:
        # Strategy for more than one person
        while n > 3:
            # Fastest and next fastest go across, fastest comes back
            strategy.append((times[0], times[1]))
            strategy.append((times[0],))
            strategy.append((times[-2], times[-1]))
            strategy.append((times[1],))
            total_time += times[1] + times[0] + times[-1] + times[1]
            n -= 2

            # Strategy for the remaining people
            if n == 3:
                total_time += sum(times)
                strategy.append((times[0], times[1]))
                strategy.append((times[0],))
                strategy.append((times[0], times[2]))
            elif n == 2:
                total_time += times[1]
                strategy.append((times[0], times[1]))
            else:
                total_time += times[0]
                strategy.append((times[0],))

        print(total_time)
        for step in strategy:
            print(" ".join(map(str, step)))
        if _ < num_cases - 1:
            print()
