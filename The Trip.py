# Function to calculate the minimum amount of money that must change hands to equalize stu-dents' costs 
def calculate_money_exchange(trip_data): 
    total_cost = sum(trip_data) 
    num_students = len(trip_data) 
    avg_cost = total_cost / num_students 
    min_exchange = sum([max(0, round(avg_cost - cost, 2)) for cost in trip_data]) 
    return f"${min_exchange:.2f}" 
  
# Main program to read input and calculate money exchange for each trip 
while True: 
    num_students = int(input()) 
    if num_students == 0: 
        break 
    trip_expenses = [float(input()) for _ in range(num_students)] 
    result = calculate_money_exchange(trip_expenses) 
    print(result) 
 
