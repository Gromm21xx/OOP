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
