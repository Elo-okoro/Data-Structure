prices = [10, 15, 20, 25, 30, 35, 40]
print("This is the price list:", prices)
profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i -1]:
        gain  = prices[i] - prices[i - 1]
        print("But at", prices[i-1], "Sell at", prices[i], "Gain", gain)
print("Maximum profit:", profit)

total_profit = 0
for i in range(1, len(prices)):
    daily_difference = prices[i] - prices[i - 1]
    if daily_difference>0:
        total_profit += daily_difference
        print("Added profit:", daily_difference)
print("Total Accumulated Profit:", total_profit)

heights = [0, 1, 2, 3, 4, 4, 6, 7, 5]
n = len(heights)
left_tallest = [0] * n
left_tallest[0] = heights[0]

for i in range(1, n):
    left_tallest[i] = max(left_tallest[i - 1], heights[i])

print("Heights:     ", heights)
print("Left Tallest:", left_tallest)

right_tallest = [0] * n
right_tallest[n - 1] = heights[n - 1]
for i in range(n-2, -1, -1):
    right_tallest[i] = max(right_tallest[i+1], heights[i])
print("Heights:      ", heights)
print("Right Tallest:", right_tallest)

water = 0
for i in range(n):
    small_bar = min(left_tallest[i], right_tallest[i])
    trapped = small_bar - heights[i]
    water += trapped

print("Total Rainwater Trapped:", water)
