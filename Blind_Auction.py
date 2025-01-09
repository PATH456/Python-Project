# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

res_dict = {}
start = True
bid_value = 0
while start == True:
    user_name = input("What is your name? ")
    user_bid = int(input("what is your bid? "))
    res_dict[user_name] = user_bid
    other_user = input("Are there any others who want to bid?\nType 'yes' or 'no ")
    if other_user == "no":
        start = False

for key in res_dict:
    if res_dict[key] > bid_value:
        bid_value = res_dict[key]
        winner = key
print(f"The winner is {winner}, with the bid of {bid_value}")












