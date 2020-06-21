load_file_in_context('blockchain.py')

test_block = Block(1,0)

test_blockchain = Blockchain()

test_proof = test_blockchain.proof_of_work(test_block)

try:
  proof
  if proof == test_proof:
    pass_tests()
except:
  fail_tests("Did you create a variable called proof?")
  
  