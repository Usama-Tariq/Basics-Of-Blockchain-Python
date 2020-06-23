import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash):
    self.timestamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()