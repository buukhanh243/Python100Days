
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
   highest_bid = 0
   winner = ""
   for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
   print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
 name = input('what is your name?: ')
 price = int(input('What is your bid?: $'))
 #them thuoc tinh vao trong dict
 bids[name] = price
 print(bids)
 should_continue = input('Are there any orther bidders? Type YES or NO. \n')
 if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bidding_record=bids)
 elif should_continue == 'yes':
    pass