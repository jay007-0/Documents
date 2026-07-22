import random

print("\n--- Trade Sim v1 ---")
## 1. A simple list to track the price history day by day
price_history = [100.00]

volatility = 0
while True:
    try:
        volatility = int(input("Choose the volatility of the stock from 1-5: "))
        if 1 <= volatility <= 5:
            break #stops the while loop
        else:
            print("Enter a number from 1-5.")
    except KeyboardInterrupt:
        print("\nProgram stopped safely by the user!")
        exit()
    except:
        print("Not a valid number.")

market_drift = 0

for day in range(1,6): 
    max_swing = volatility * 3 #3 scales the percentage to be meaningful
    pct_change = random.uniform(-max_swing, max_swing) + market_drift

    #calculate new price
    new_price = price_history[-1] * (1 + pct_change/100)

    #append
    price_history.append(new_price)


    print(f"\n--- Day {day} Price ---")
    for price in price_history:
        print(f"${price:.2f}", end=", ")
    print("\n-------------------\n")
    market_drift += 0.5 #increasing drifting up


if price_history[0] > price_history[-1]:
    print(f"You lost ${(price_history[0] - price_history[-1]):.2f}!")
else:
    print(f"You made ${(price_history[-1] - price_history[0]): .2f}!")