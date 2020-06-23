load_file_in_context('script.py')

try:
  my_transaction
except NameError:
  fail_tests("Did you remember to define `my_transaction`?")

if "amount" not in my_transaction:
  fail_tests("Oops! It looks like the key `amount` was not found in `my_transaction`.")
  
if "sender" not in my_transaction:
  fail_tests("Oops! It looks like the key `sender` was not found in `my_transaction`.")

if "receiver" not in my_transaction:
  fail_tests("Oops! It looks like the key `receiver` was not found in `my_transaction`.")
  
pass_tests()
