# Object-Oriented Programming

## Practical Exercise 2

## Exercise instructions:


1.  Import the pandas library, which you'll use to load the CSV dataset.
2.  Define the base class called Customer. This class should have an \__init__ method that initializes the email, total_spent, and membership_length attributes when a new instance of the class is created. Include two methods: get_customer_info and get_membership_level. The get_customer_info method should return a string containing the customer's email, total amount spent, and membership level. The get_membership_level method should determine the customer's membership level based on their membership length.
3.  Create a subclass called PreferredCustomer that inherits from the Customer class. This means that the PreferredCustomer class will have all the attributes and methods of the Customer class, plus any additional attributes and methods you define in the PreferredCustomer class.
4.  In the PreferredCustomer class, define the \__init__ method. Use Customer.\__init__(self, email, total_spent, membership_length) to call the \__init__ method of the parent Customer class and initialize the inherited attributes. Add a new attribute called preferred_status and set it to True.
5.  Override the get_customer_info method in the PreferredCustomer class. Call the get_customer_info method of the parent Customer class using Customer.get_customer_info(self) and store the result in a variable called info. Append the preferred_status to the info string and return the updated string.
6.  Add a new method called get_preferred_gift in the PreferredCustomer class. This method should return a string representing a gift for preferred customers.
7.  Create another subclass called VIPCustomer that also inherits from the Customer class.
8.  In the VIPCustomer class, define the \__init__ method similarly to the PreferredCustomer class. Call the \__init__ method of the parent Customer class and add a new attribute called vip_status, which you should set to True.
9.  Override the get_customer_info method in the VIPCustomer class. Call the get_customer_info method of the parent Customer class, store the result in the info variable, append the vip_status to the info string, and return the updated string.
10. Add a new method called get_vip_gift in the VIPCustomer class. This method should return a string representing a gift for VIP customers.
11. Load the "Ecommerce Customers.csv" dataset using pd.read_csv(). This dataset contains information about customers, including their email, total amount spent, and membership length.
12. Create an empty list called customers to store instances of different customer types.
13. Iterate over each row of the dataset using iterrows(). For each row, extract the email, total amount spent, and membership length.
14. Use conditional statements to determine the type of customer based on the total amount spent and membership length. If the total amount spent is greater than 5000, create a VIPCustomer instance. If the membership length is greater than 2, create a PreferredCustomer instance. Otherwise, create a regular Customer instance.
15. Append each customer instance to the customers list.
16. **(Stretch Goal)** Use a for loop to iterate over each customer in the customers list. For each customer, call the get_customer_info method, which will automatically use the appropriate implementation based on the actual type of the customer object (polymorphism).
17. **(Stretch Goal)** Use another for loop to determine and print the gift for each customer. Use isinstance() to check the type of each customer object. If the customer is a PreferredCustomer, call the get_preferred_gift method and print the result along with the customer's email and membership level. If the customer is a VIPCustomer, call the get_vip_gift method and print the result along with the customer's email and membership level. If the customer is a regular Customer, print a message indicating that no special gift is available, along with the customer's email and membership level.