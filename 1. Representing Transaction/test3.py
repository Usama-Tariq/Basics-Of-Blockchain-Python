load_file_in_context('script.py')

try:
  block_transactions
except NameError:
  fail_tests("Did you remember to define `block_transactions`?")

if len(block_transactions) != 3:
  fail_tests("Did you select 3 transactions to add to `block_transactions`?")


pass_tests()