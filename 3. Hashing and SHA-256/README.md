# Hashing and SHA-256
Before we create a more dynamic blockchain, let’s learn how to use a hash function in Python. Specifically, we will be using the [SHA-256 hash function](https://docs.python.org/2/library/hashlib.html) which can be easily imported in Python.

We will use the SHA-256 as a regular function that takes in a random string as its argument. To properly use this function in Python 3, our string must be encoded before being passed as an argument. To encode the string, we use the `.encode()` method.

### Instructions

#### Step: 1
Import `sha256` from the `hashlib` Python library.

#### Step: 2
Create a variable called `text`. Initialize the variable with this string `I am excited to learn about blockchain`.

#### Step: 3
Create a sha256 hash object, using the constructor `sha256()` and pass the `text` variable as its argument. Assign the value of this object to a variable called `hash_result`.

Be sure to use the `.encode()` method on the `text` variable.

###### Hint: 
In the argument of the sha256 default constructor, pass the string with the `.encode()` method attached as shown:

`sha256(string.encode())`

#### Step: 4
Call the `.hexdigest()` method on `hash_result` and print the result.

###### Hint: 
In order to properly print a hash object, you must first call the method `.hexdigest()` over it. This allows Python to print a readable string to the terminal.

`print(hash_object.hexdigest())`

#### Step: 5
Modify the `text` variable by adding an exclamation mark at the end and running your code.

Notice how this hash is completely different from the last one?
