# Creating Blocks

Now let’s think of a way to represent a block in Python. We could create a bigger dictionary and store our data inside this dictionary. But since blocks can be represented as objects, let’s create a Block Class which we can easily use to create new blocks.

Recall that a Block contains the following properties:

- Timestamp
- Transaction
- Hash
- Previous Hash
- Nonce

In this exercise, we will be creating the default constructor for the Block class in our Mini-Blockchain.

### Instructions

#### Step: 1
Every `Block` in the blockchain has a timestamp associated with it. In order to dynamically generate a timestamp, we must import a Python module that returns the current date and time.

Import the `datetime` module from the `datetime` library.

###### Hint:
To use a specific module in your code, you must first make it accessible by importing it to your script file. The following is an example of how to import a specific module from a library.

`from library import module`

#### Step: 2
Inside the [datetime module](https://docs.python.org/2/library/datetime.html) there is a `.now()` method that returns the current date and time.

Call the `datetime` module’s `.now()` method to print out the current date and time.

###### Hint:
The appropriate way to call this method is `datetime.now()` enclosed in a `print()` statement.

#### Step: 3
Now let’s work on creating our `Block`. We will be passing `transactions` and `previous_hash` to the default constructor each time a `Block` is created.

Complete the `__init__()` method inside the Block class by initializing the following instance variables:

- `transactions`
- `previous_hash`
- `nonce` (with a default value of `0`).

###### Hint:
The header for the function should look as follows:

`def __init__(self, transactions, previous_hash, nonce = 0):`

Be sure to initialize all the variables as well:

```def __init__(self, value):
  # Initialization:
  self.value = value```

#### Step: 4
Inside the `__init__()` method, create a `timestamp` instance variable that stores the current date and time.

###### Hint:
Call the `.now()` method from the `datetime` module and store the result in `timestamp`.
