def fizz_buzz(n):
    # Declare a list of strings to store the results
    result = []

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):

        # Check if i is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:

            # Add "FizzBuzz" to the result list
            result.append("FizzBuzz")

        # Check if i is divisible by 3
        elif i % 3 == 0:

            # Add "Fizz" to the result list
            result.append("Fizz")

        # Check if i is divisible by 5
        elif i % 5 == 0:

            # Add "Buzz" to the result list
            result.append("Buzz")
        else:

            # Add the current number as a string to the
            # result list
            result.append(str(i))

    # Return the result list
    return result


# Driver code
n = 20

# Call the fizz_buzz function to get the result
result = fizz_buzz(n)

# Print the result
print(' '.join(result))
