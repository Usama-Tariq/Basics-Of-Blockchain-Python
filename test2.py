load_file_in_context('script.py')
import gc
import re

objs = gc.get_objects()[:]
blockchain_objects = []

for obj in objs:
  if(isinstance(obj, Blockchain)):
    blockchain_objects.append(obj)
    
blockchain = blockchain_objects[0]

if len(blockchain.chain) != 4:
  fail_tests('Did you add all three blocks to the blockchain?')

if blockchain.chain[1].transactions == block_one_transactions:
  if blockchain.chain[2].transactions == block_two_transactions:
    if blockchain.chain[3].transactions == block_three_transactions:
      with open('script.py','r') as file:
        occurences = len(re.findall('(local_blockchain)(\\.)(print_blocks)(\\(\\))', file.read()))
        if occurences == 2:
          pass_tests()
        else:
          fail_tests('Did you use the correct method to print the contents of the blockchain?')
    else:
      fail_tests('Did you add block_three_transactions into the correct block?')
  else:
    fail_tests('Did you add block_two_transactions into the correct block?')
else:
  fail_tests('Did you add block_one_transactions into the correct block?')
      