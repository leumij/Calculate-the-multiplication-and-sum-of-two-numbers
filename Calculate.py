# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

#pseudocode

# Calculate for user output
def multiplication_or_sum(number_1, number_2):
    product = number_1 * number_2

# If product is equal 1000 return product
    if product <= 1000:
     return product

    else:
        return number_1 + number_2


