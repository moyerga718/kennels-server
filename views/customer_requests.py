CUSTOMERS = [
        {
            "id": 1,
            "name": "Jermaine Jangle"
            
        },
        {
            "id": 2,
            "name": "Jeb Bush"
            
        }
    ]

def get_all_customers():
    """
    THIS FUNCTION GETS ALL CUSTOMERS
    """
    return CUSTOMERS

def get_single_customer(id):
    """
    THIS FUNCTION GETS ONE customer BY ITS ID
    """
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    """
    PASS A customer DICTIONARY INTO THE FUNCTION. THIS FUNCTION SEES WHAT THE ID OF 
    THE LAST customer IN CUSTOMERS IS, 
    ADDS THAT ID TO customer DICTIONARY THAT WAS PASSED IN.
    ADD NEW customer DICTIONARY TO LIST.
    """

    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    """DELETE CUSTOMERS FUNCTION
    """

    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """UPDATE CUSTOMERS FUNCTION
    """
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break