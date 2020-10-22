def spiral_counter(horizontal_length):
    counter = 1
    placeholder = 2
    total = 0
    increment = 0
    while counter <= horizontal_length**2:
        total += counter
        counter += placeholder
        increment += 1
        if increment == 4:
            placeholder += 2
            increment = 0
    return total
if __name__ == "__main__":
    print(spiral_counter(501))
    
