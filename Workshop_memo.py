# print("******WORKSHOP*************")
# bill_item = []
# while True:
#     service_name = input("Enter the service name (Done for complete)")
#     if service_name.lower=='done':
#         break
#     try:
#         cost= (input("Enter the cost of '{service_name}': in $"))
#     except:
#         print("❌Value erorr")
#     item ={"service":service_name,"price":cost}
#     bill_item.append(item)
#     #print(f"✅added: {service_name} - ${cost:.2f}\n")
#     print(f"✅ Added: {service_name} - ${cost:.2f}\n")
#     print("################################")
#     print("#########FINAL MEMOMO##########")
#     print("################################")
#     total_bill=0
#     for item in bill_item:
#         print("---------------------------")
#         print(f"total wages and bill       ${total_bill:.2f}")
#         print("==================================")
#         print("Thank you for your bussiness")
# print("====================================")
# print("     CAR WORKSHOP BILLING SYSTEM    ")
# print("====================================\n")

# Create an empty list to store all the services added by the mechanic
bill_items = []

while True:
    # 1. Get the service name
    service_name = input("Enter service/part name (or type 'done' to calculate bill): ")
    
    # Check if the mechanic is finished entering items
    if service_name.lower() == 'done':
        break
        
    # 2. Get the cost for that specific service
    try:
        cost = float(input(f"Enter cost for '{service_name}': $"))
    except ValueError:
        print("❌ Invalid price. Please enter numbers only.\n")
        continue # Restarts the loop to ask for the service again
        
    # 3. Store the service and cost together as a dictionary inside our list
    item = {"service": service_name, "price": cost}
    bill_items.append(item)
    print(f"✅ Added: {service_name} - ${cost:.2f}\n")

# ----------------------------------------------------
# FINAL BILL GENERATION (Runs after 'done' is typed)
# ----------------------------------------------------
print("\n====================================")
print("             FINAL MEMO             ")
print("====================================")

total_bill = 0

# Use a for loop to iterate through all stored services and add up the costs
for item in bill_items:
    print(f"- {item['service']:<25} ${item['price']:>7.2f}")
    total_bill += item['price']

print("------------------------------------")
print(f"TOTAL WAGES & PARTS:        ${total_bill:.2f}")
print("====================================")
print("Thank you for your business!")

