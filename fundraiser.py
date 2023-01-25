def money_raised(num_tickets_sold, prize_cost):
    revenue = num_tickets_sold * 5
    profit = revenue - prize_cost
    return profit

print(money_raised(50, 50))
print(money_raised(100, 50))