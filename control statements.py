#create a function
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        discounted_price = price - discount_amount
        return discounted_price
    else:
        # Return the original price if no discount is applied
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the Marked price of the item: ksh"))
discount_percent = float(input("Enter the discount rate : "))

# Calculate the final price
discounted_price = calculate_discount(price, discount_percent)

# Print the final price or the original price
if discounted_price == price:
    print(f"The original price is: ksh{price:.2f}")
else:
    print(f"The final price after applying the discount is: ksh{discounted_price:.2f}")
