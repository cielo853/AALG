def sum_two_numbers(numbre_1 : int, numbre_2 : int ) -> int:
    return numbre_1 + numbre_2
#call function and store the returned value 
result = sum_two_numbers(7, 8)
print(result)
def sum_two_numbersX(numbre_1 : int=3, numbre_2 : int=2 ) -> int:
    return numbre_1 + numbre_2
result = sum_two_numbersX()
print(result)