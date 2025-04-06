def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract discount from original price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    print(f"The final price after applying discount is: {final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")