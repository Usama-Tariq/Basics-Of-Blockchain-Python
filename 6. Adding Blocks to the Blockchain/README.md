# Adding Blocks to the Blockchain
Now that we have everything in place, let’s begin adding blocks to the blockchain.

### Instructions

#### Step: 1
Complete the function `add_block()`.

To do this, create a variable named `new_block` that takes in a transaction and the `previous_block`‘s hash. Append `new_block` to the end of the `chain`.

###### Hint:
The proper way to access a specific block’s hash from the `chain` is through this line of code: `self.chain[index].hash`.

- The previous block can be accessed by `self.chain[len(self.chain)-1]`.
- Your resulting code should be as follows: `Block(transactions, previous_block_hash)`

