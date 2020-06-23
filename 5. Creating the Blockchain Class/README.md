# Creating the Blockchain Class
Each computer participant has their own copy of the blockchain. Ideally, each copy of the blockchain should have the same properties and functionality to add and validate blocks.

We can represent the blockchain as an object. We are using objects for our implementation, because they offer the flexibility to create specific attributes and methods. Representing it as an object also allows us to create blockchain instances for each computer participant.

To review, our blockchain contains the following:

- ___Chain:___ A list that that holds all the blocks inside the blockchain.
- ___Unverified Transactions:___ A list that represents all the unverified transactions before being passed into a block.
- ___Genesis Block:___ A block automatically generated when the blockchain is initialized.

### Instructions


#### Step: 1
Fill in the `__init__()` method inside the `Blockchain` class by initializing instance variables `chain` and `all_transactions` as empty Python lists.

#### Step: 2
Complete the method `genesis_block` by instantiating a new `Block` object with an empty `transactions` list and a previous hash of `0`.

Append the resulting block to the `chain`.

###### Hint:
- The syntax to instantiate a new `Block` object is `Block(transactions, previous_hash)`.
- To access the `Blockchain` chain use `self.chain`.

#### Step: 3
Since we want to automatically create a Genesis Block when a new blockchain object is created, call the method `.genesis_block()` inside the `__init__()` method.

###### Hint:
The right way to initialize a genesis block is by writing `self.genesis_block()`
