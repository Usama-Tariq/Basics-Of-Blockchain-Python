# Checking for a Broken Chain

Hashing helps to maintain the integrity of the blockchain. In this exercise, we will see this in action. Let’s write a `.validate_chain()` method that checks to see if blocks are linked to each other properly.

In order to validate the entire blockchain, we must loop through each of the blocks stored inside the blockchain itself. Then, we will check through each of the blocks to ensure that the previous hash value matches with the hash value inside our previous block.

### Instructions


#### Step: 1
In the `.validate_chain()` method, create a for loop with the loop variable `i` and traverse through the entire length of `self.chain`. Be sure to start at index `1` instead of index `0`.

Inside the `for` loop, create a variable `current` and assign it to the current block being indexed with `i`. Create another variable `previous` and assign it to the previous block using index `i-1`.

###### Hint:
Loop through the correct part of the chain with the following snippet:

`for i in range(1, len(self.chain)):`

#### Step: 2
Verify that the hash of the current block is NOT equal to the value the current block generates via the `generate_hash()` method. If this condition is true, then the blockchain is not valid, therefore we should return `False`.

#### Step: 3
Verify that the hash of the previous hash of the current block is NOT equal to the value generated over the previous block using the `generate_hash()` method. If this condition is true, then the blockchain is not valid, therefore we should return `False`.

#### Step: 4
If the above conditions are not satisfied, then the blockchain is valid! Return `True` outside the `for` loop.
