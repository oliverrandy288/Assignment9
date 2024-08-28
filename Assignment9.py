# Task 1: Restaurant Menu Update

# Initial menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category "Beverages"
restaurant_menu["Beverages"] = {"Coffee": 2.99, "Tea": 1.99}

# Update the price of "Steak"
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

# Print the updated menu to verify changes
print("Updated Restaurant Menu:")
for category, items in restaurant_menu.items():
    print(f"{category}:")
    for item, price in items.items():
        print(f"  {item}: ${price:.2f}")
    print()  # Blank line for readability

# Task 2: Customer Service Ticket Tracker

# Initialize with some sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    """Open a new service ticket."""
    if ticket_id in service_tickets:
        print("Ticket ID already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened.")

def update_ticket_status(ticket_id, new_status):
    """Update the status of an existing ticket."""
    if ticket_id in service_tickets:
        if new_status in ["open", "closed"]:
            service_tickets[ticket_id]["Status"] = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
        else:
            print("Invalid status. Use 'open' or 'closed'.")
    else:
        print("Ticket ID not found.")

def display_tickets(status_filter=None):
    """Display all tickets or filter by status."""
    print("Service Tickets:")
    for ticket_id, details in service_tickets.items():
        if status_filter is None or details["Status"] == status_filter:
            print(f"ID: {ticket_id}")
            print(f"  Customer: {details['Customer']}")
            print(f"  Issue: {details['Issue']}")
            print(f"  Status: {details['Status']}")
            print()  # Blank line for readability

# Test the functions
open_ticket("Ticket003", "Charlie", "Feature request")
update_ticket_status("Ticket001", "closed")
display_tickets()
display_tickets("open")
