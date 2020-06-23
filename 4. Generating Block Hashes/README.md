# Generating Block Hashes

Block hashes are used to uniquely identify and maintain the integrity of each block. The SHA-256 algorithm is used to generate the hash of the block using the timestamp, data, and previous hash — the three properties of our Block class!

Let’s create the `.generate_hash()` method for the Block class.

### Instructions

#### Step: 1
In the `.generate_hash()` method, create the variable `block_contents`, which combines the `Block` timestamp, transactions, nonce, and previous hash.

Wrap each item in the `str()` method in order to convert them to a string type to prepare for hashing.

Return the result.

###### Hint:
To combine strings together the following syntax is used:

`string = sub_string1 + sub_string2 + sub_string3`

#### Step: 2
Create a variable `block_hash`.

Create a new hash with `sha256()` and `block_contents` and save the value to `block_hash`.

Remember to use the `.encode()` method to encode the string.

Update the method to return `block_hash`.

#### Step: 3
Return the text hash value by calling the `hexdigest()` method on `block_hash`.

#### Step: 4
Uncomment the line in `__init__()` that calls the `generate_hash()` function to complete the `Block` class.
