# Implementing Proof-of-Work
Now that we’ve seen a simple example of Proof-of-Work, let’s integrate it into our blockchain! Complete the `proof_of_work()` method inside the Blockchain class.

### Instructions


#### Step: 1
Inside the `.proof_of_work()` method, create a local variable `proof` and assign it the block’s `hash`.

###### Hint:
Call the `generate_hash()` method over the `Block` object to retrieve its hash.

#### Step: 2
Finish the rest of the method by creating a loop that increments the `nonce` value until the hash with the required difficulty has been generated.

After finding the correct hash, set the value of the `block.nonce` back to `0` and return the correct hash outside of the loop.

###### Hint:
The variable `difficulty` refers to the number of leading zeros required in the hash.

Try using a loop to automatically increase the `nonce` value as it generates new block hashes.
