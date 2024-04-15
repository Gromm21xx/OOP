import pandas as pd

class Customer:
    def __init__(self, email, total_spent, membership_length):
        self.email = email
        self.total_spent = total_spent
        self.membership_length = membership_length

    def get_customer_info(self):
        membership_level = self.get_membership_level()
        return f"Email: {self.email}, Total Spent: £{self.total_spent}, Membership Level: {membership_level}"

    def get_membership_level(self):
        if self.membership_length >= 5:
            return "Gold"
        elif self.membership_length >= 2:
            return "Silver"
        else:
            return "Bronze"

# Creating instances of the Customer class with different membership lengths
customer1 = Customer("john@example.com", 1500, 2)
customer2 = Customer("sarah@example.com", 5000, 7)
customer3 = Customer("mike@example.com", 1000, 1)

# Calling the get_customer_info method for each customer
print(customer1.get_customer_info())
print(customer2.get_customer_info())
print(customer3.get_customer_info())










class PreferredCustomer(Customer):
    def __init__(self, email, total_spent, membership_length):
        Customer.__init__(self, email, total_spent, membership_length)
        self.preferred_status = True

    def get_customer_info(self):
        info = Customer.get_customer_info(self)
        return f"{info}, Preferred Status: {self.preferred_status}"

    def get_preferred_gift(self):
        return "Free shipping coupon"

class VIPCustomer(Customer):
    def __init__(self, email, total_spent, membership_length):
        Customer.__init__(self, email, total_spent, membership_length)
        self.vip_status = True

    def get_customer_info(self):
        info = Customer.get_customer_info(self)
        return f"{info}, VIP Status: {self.vip_status}"

    def get_vip_gift(self):
        return "Exclusive VIP gift"

# Load the dataset
data = pd.read_csv("Ecommerce Customers.csv")

# Create instances of different customer types based on the dataset
customers = []
for _, row in data.iterrows():
    email = row['Email']
    total_spent = row['Yearly Amount Spent']
    membership_length = row['Length of Membership']
    
    if total_spent > 5000:
        customer = VIPCustomer(email, total_spent, membership_length)
    elif membership_length > 2:
        customer = PreferredCustomer(email, total_spent, membership_length)
    else:
        customer = Customer(email, total_spent, membership_length)
    
    customers.append(customer)

# Using polymorphism to call the get_customer_info method for each customer
for customer in customers:
    print(customer.get_customer_info())

# Using polymorphism to determine and print the gift for each customer
for customer in customers:
    if isinstance(customer, PreferredCustomer):
        gift = customer.get_preferred_gift()
        print(f"Customer: {customer.email}, Membership Level: {customer.get_membership_level()}")
        print(f"Preferred Customer Gift: {gift}")
        print()  # Add an empty line for readability
    elif isinstance(customer, VIPCustomer):
        gift = customer.get_vip_gift()
        print(f"Customer: {customer.email}, Membership Level: {customer.get_membership_level()}")
        print(f"VIP Customer Gift: {gift}")
        print()  # Add an empty line for readability
    else:
        print(f"Customer: {customer.email}, Membership Level: {customer.get_membership_level()}")
        print("No special gift for regular customers.")
        print()  # Add an empty line for readability