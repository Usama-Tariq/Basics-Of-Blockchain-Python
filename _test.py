load_file_in_context('script.py')
import gc
import re

objs = gc.get_objects()[:]
blockchain_objects = []

for obj in objs:
  if(isinstance(obj, Blockchain)):
    blockchain_objects.append(obj)
    
blockchain = blockchain_objects[0]

if blockchain.chain[2].transactions != fake_transactions:
  fail_tests('Did you modify the transactions to fake_transactions in the second block that was added?')
  
with open('script.py','r') as file:
  if re.search('(local_blockchain)(\\.)(validate_chain)(\\(\\))', file.read()):
    pass_tests()
  else:
    fail_tests('Did you use the correct method to validate the blockchain?')