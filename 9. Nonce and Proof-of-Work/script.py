new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# import sha256
from hashlib import sha256 
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof 
proof =  sha256((str(nonce)+ str(new_transactions)).encode()).hexdigest()
# printing proof
print(proof)

# finding a proof that has 2 leading zeros
final_proof = proof
while final_proof[:2] != '0'*difficulty:
  nonce += 1
  print(nonce)
  final_proof =  sha256((str(nonce)+ str(new_transactions)).encode()).hexdigest()
# printing final proof that was found
print(final_proof)


'''
while (proof[:2] != '0' * difficulty):
  nonce += 1
  proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# printing final proof that was found
final_proof = proof
print(final_proof)
'''