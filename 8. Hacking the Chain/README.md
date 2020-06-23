# Hacking the Chain

Now we can use the code in our previous exercise to spot a broken link. Let’s try tampering with the contents of the block and see how that creates a mismatch between hash values.

### Instructions

#### Step: 1
Instantiate a new Blockchain object called `my_blockchain`.

#### Step: 2
Add a new block to `my_blockchain` and pass in `new_transactions` as the argument.

Print out the contents of `my_blockchain` to see the new block!

###### Hint:
Remember, the `.add_block()` method is used to add a block. This method has `new_transactions` as its parameter. Similarly, the `print_blocks()` method is used to print the contents of a Blockchain object.

#### Step: 3
Select the transactions found in `my_blockchain`‘s `chain` attribute. Set the `transactions` variable of Block 1 to the string `"fake_transactions"`.

###### Hint:
Use `my_blockchain.chain[1]` to grab Block 1 on the blockchain. You can access this block’s transactions using the `transactions` attribute.

#### Step: 4
Now let’s check if the blockchain is still valid by calling the correct method on `my_blockchain`!

###### Hint:
Remember, the `validate_chain()` method is used to validate a Blockchain object.
