def number_pattern(n):
    if not isinstance(n, int):
            return "Argument must be an integer value."
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    numbers = range(1, n+1)
    collector = ''
    for index, number in enumerate(numbers):
        if index > 0:
            collector += ' '
        collector += str(number)
    return collector  
        
if __name__ == "__main__":
    print(number_pattern(4))
