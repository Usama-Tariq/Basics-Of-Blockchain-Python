load_file_in_context('script.py')

try:
  my_transaction
except NameError:
  fail_tests("Did you remember to define `my_transaction`?")

if len(mempool) != 7:
  fail_tests("Did you add `my_transaction` to `mempool`?")

if type(mempool[6]) is not dict:
  fail_tests("Looks like the item you added to `mempool` is not of type `dictionary`")

pass_tests()