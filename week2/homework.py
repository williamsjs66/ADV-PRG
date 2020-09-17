import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    return_value = [threes * threes for threes in range(100) if threes % 3 == 0]
    return return_value
    
if __name__ == "__main__":
   for x in squared_threes():
       print(x)
