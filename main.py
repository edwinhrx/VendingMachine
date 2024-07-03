class VendingMachine:
    def __init__(self):
        self.items = {
            'Coke': 2,
            'Pepsi': 2,
            'Sprite': 2,
            '7-Up': 7,
            'Water': 100,
            'Juice': 5
        }
        self.notes = [100, 50, 20, 10, 5, 1]  # Notes available for change

    def display_drinks(self):
        print("Available drinks:\n")
        for item, price in self.items.items():
            print(f"{item}: RM {price}")

    def dispense_drink(self, item):
        print(f"\nDispensing {item}...")

    def complete_transaction(self, amount_inserted, change_amount, change):
        print(f"\nTotal paid: RM {amount_inserted}. Returning: RM {change_amount}")
        if change:
            print(f"Notes dispensed: RM {change}.")
        else:
            print("No change needed.")

    def get_change(self, amount):
        change = []
        for note in self.notes:
            while amount >= note:
                amount -= note
                change.append(note)
                print(f"Dispensing RM {note}.")
        return change

    def buy_item(self):
        self.display_drinks()
        item = input("\nPlease select a drink: ") # Enter item name
#        print("\nPlease select a drink: ")
#        item = 'Coke' # Manually choose Coke
#        item = 'Water' # Manually choose Water
#        item = 'Kickapoo' # Manually choose Kickapoo 


        if item not in self.items:
            print(f"\n{item} not available.")
            return
        
        price = self.items[item]
        print(f"\nYou chose {item}: RM {price}")
        
        amount_inserted = 0
        buy_amount_balance = 0
        
        amount_inserted = int(input(f"Please insert RM {price}: ")) # Money inserted
        print()
#        print(f"Please insert: RM {price}")
#        amount_inserted = 20 # Manually entered 20
#        amount_inserted = 90 # Manually entered 90
#        amount_inserted = 19 # Manually entered 19

        while amount_inserted < price:
            buy_amount_balance = price - amount_inserted
            amount_inserted += int(input(f"\nInserted RM {amount_inserted}, remaining balance: RM {buy_amount_balance}"))
        print()

#            print(f"Inserted RM {amount_inserted}, remaining balance: RM {buy_amount_balance}")
#            amount_inserted += 20 # Manually entered 20

        self.dispense_drink(item)
        change_amount = amount_inserted - price
        change = self.get_change(change_amount)
        self.complete_transaction(amount_inserted, change_amount, change)

vm = VendingMachine()
vm.buy_item()
