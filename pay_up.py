# Challenge: Create the output display for the PayUp app.

# 1. Check out the example output in `example_output.md`
# 2. Define a variable for each item: event name, cost, service charge,
#    group size, grand total, and total per person. Use made-up values for now —
#    we'll do the math later!
# 3. Build the display line by line using print() and f-strings.
#    Remember: an empty print() creates a blank line.
# 4. Run it and make sure it matches the example.

event_name  = "Matumbo Resturant"
cost =  500
service_charge = 50
group_size = 5
grand_total = cost + service_charge
total_per_person = int(grand_total / group_size)


print(f"Welcome to PayUp!")
print()
print(f"Here's the breakdown for dinner at {event_name}:")
print()
print(f"Cost: ${cost} \nService charges: ${service_charge} \nGroup size: {group_size} \nGrand total: ${grand_total}")
print()
print(f"Each person must PayUp: ${total_per_person}")
