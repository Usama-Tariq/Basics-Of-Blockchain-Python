# import datetime library
from datetime import datetime
# print current date and time
print(datetime.now())

class Block:
  timestamp = 0
# default constructor for block class
  def __init__(self, transactions, previous_hash, nonce = 0 ):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.timestamp = datetime.now()
    pass