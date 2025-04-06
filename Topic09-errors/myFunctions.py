def fibonacci (number):
    return[]


# Test the code
if __name__ == '__main__': 
   # tests will go here 
  print("all good")

# Run test cases before function is complete
# Use asset built in python statement for testing and debugging
return7 = [0,1,1,2,3,5,8] 
return11 = [0,1,1,2,3,5,8,13,21,34,55] 
assert fibonacci(7) == return7, 'incorrect return for 7' 
assert fibonacci(11) == return11, 'incorrect return for 11' 
assert fibonacci(0) == [], 'incorrect return value for 0' 
assert fibonacci(1) == [0], 'incorrect return value for 1' 

# Test for the negative input
try: 
   fibonacci(-1) 
except ValueError: 
    pass 
else: 
    assert False, 'fibonacci missing ValueError' 


# # logging.basicConfig(level=logging.DEBUG)  # Uncomment for debugging
import logging 
logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number < 0:
        raise ValueError("number must be > 0")
    if number == 0:
        return []
    if number == 1:
        return [0]

    a = 0
    b = 1
    fibonacciSequence = [0]

    for i in range(1, number):
        fibonacciSequence.append(b)
        a, b = b, a + b

    logging.debug("%d: %s", number, fibonacciSequence)
    return fibonacciSequence