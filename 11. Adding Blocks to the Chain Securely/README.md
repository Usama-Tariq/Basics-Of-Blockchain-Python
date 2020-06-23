# Adding Blocks to the Chain Securely
Now that we have implemented our Proof-of-Work method, we can now work on adding new blocks securely.

### Instructions


#### Step: 1
In the `.add_block()` method, calculate the `proof_of_work` for the `new_block`. Assign the calculated `proof_of_work` to a variable named `proof` before appending the `new_block` to the blockchain.

Return, in order, the calculated `proof` and the `new_block` itself.

###### Hint:
The proper way to call the Proof-of-Work method is the following: `.proof_of_work(block_name)`.

Remember that you can return two values from a function by separating them with a comma: `return value_one, value_two`.
