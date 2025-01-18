# Coffee Machine Simulation in Python

This project simulates a coffee machine using Python. Users can order drinks, check resource availability, and view the machine's report. The program handles coin insertion and change calculation, ensuring a smooth and interactive experience.

---

## Features

1. **Menu Options**:
   - Tea
   - Espresso
   - Cappuccino

2. **Functionalities**:
   - Process orders for drinks.
   - Check resource availability for each order.
   - Handle payments with coin insertion.
   - Provide change if payment exceeds the drink cost.
   - Display a report showing available resources and total earnings.
   - Option to turn off the coffee machine.

3. **Error Handling**:
   - Ensures sufficient resources are available before processing an order.
   - Refunds money if the payment is insufficient.

---

## How It Works

1. **Startup**:
   - The machine initializes with predefined resources (water, milk, coffee) and a menu with costs and required ingredients for each drink.

2. **Order Processing**:
   - The user selects a drink or a special command:
     - `Tea`
     - `Espresso`
     - `Cappuccino`
     - `report` (to check resource status and profits)
     - `off` (to exit the program)

3. **Payment**:
   - The user inserts coins (5rs, 10rs, 20rs).
   - The machine calculates the total inserted and verifies if it meets the cost of the selected drink.

4. **Resource Management**:
   - If resources are sufficient, the drink is prepared, and resources are deducted.
   - If insufficient, the machine notifies the user and does not process the order.

5. **Profit Calculation**:
   - Total profit is updated after every successful transaction.

---

## Code Structure

### **Menu Configuration**
The `menu` dictionary stores details of available drinks:
```python
menu = {
    "Tea": {
        "ingredients": {"milk": 100, "water": 200, "coffee": 10},
        "cost": 150,
    },
    "Espresso": {
        "ingredients": {"water": 50, "coffee": 20},
        "cost": 200,
    },
    "Cappuccino": {
        "ingredients": {"milk": 150, "water": 200, "coffee": 50},
        "cost": 350,
    },
}
```

### **Functions**
1. **`check_resource(order_ingredients)`**:
   - Verifies if resources are sufficient for the selected drink.

2. **`process_coins()`**:
   - Calculates the total amount inserted by the user.

3. **`is_payment_successful(money_received, coffee_cost)`**:
   - Checks if the payment is enough and provides change if applicable.

4. **`make_coffee(coffee_name, coffee_ingredients)`**:
   - Deducts the required ingredients from resources and serves the drink.



## How to Run

1. Clone the repository or download the script:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Run the script:
   ```bash
   python coffee_machine.py
   ```

---

## Example Usage

### Sample Input:
```plaintext
What would you like? (Tea/Espresso/Cappuccino)
Enter 'report' for overall report
Enter 'off' to exit
::: Cappuccino
```

### Output:
```plaintext
Plz insert coins
How many 5rs coins?: 10
How many 10rs coins?: 5
How many 20rs coins?: 2
Here is your Cappuccino... enjoy!
```

---

## Customization

### Adding New Drinks:
1. Update the `menu` dictionary with the new drink's ingredients and cost:
   ```python
   menu["Latte"] = {
       "ingredients": {"milk": 200, "water": 150, "coffee": 30},
       "cost": 300,
   }
   ```

### Modifying Resources:
Update the `resources` dictionary as needed:
```python
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 300,
}
```

---

## Dependencies
- Python 3.6 or higher

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bugs.

---

## Contact
For questions or feedback, please contact Shajan J Jacob.

