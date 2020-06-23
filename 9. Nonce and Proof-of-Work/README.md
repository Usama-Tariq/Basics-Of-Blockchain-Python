# Nonce and Proof-of-Work
Let’s review the concepts of nonce and proof of work. In this exercise, we will implement an example that demonstrates the difficulty of the math problem that helps protect the blockchain from potential attackers.

### Instructions

#### Step: 1
Import the `sha256` hash function from the Python `hashlib` library

#### Step: 2
Create a variable called `difficulty` and assign it a value of 2. This sets the number of leading zeros that the hash we find must have.

Create another variable called `nonce` and assign it to a value of 0. This will be our default starting value.

#### Step: 3
Using the `.str()` method, cast `nonce` and `new_transactions` into strings. Pass the two strings into the sha256 function.

Store the resulting hash value into a variable called `proof` and print it out!

___Note:___ Use the `.hexdigest()` method over the resulting sha256 function to properly store the hash value.

###### Hint:
Remember to encode the input before passing it into the hash function. The method you call over the input is `.encode()`.

#### Step: 4
Come up with some code that increments the `nonce` value until the generated hash has `difficulty` number of leading zeros. Once the desired proof has been found, store it in a variable called `final_proof` and print it out to see the correct hash!

###### Hint:
Think about using a `while` loop to keep on incrementing the `nonce` value until the following condition is True.

`hash_value[:2] != '0'*difficulty`
