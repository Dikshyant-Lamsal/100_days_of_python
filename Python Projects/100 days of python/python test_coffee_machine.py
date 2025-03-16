from menu_day_15 import MENU, resources
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def capture_output():
    """Capture stdout output into a StringIO object"""
    old_stdout = sys.stdout
    stdout_buffer = StringIO()
    sys.stdout = stdout_buffer
    try:
        yield stdout_buffer
    finally:
        sys.stdout = old_stdout

def simulate_input(inputs):
    """Simulate user input with a predefined list of inputs"""
    def mock_input(prompt):
        print(prompt, end='')
        next_input = inputs.pop(0)
        print(next_input)
        return next_input
    return mock_input

def run_test_scenario(scenario_name, inputs, expected_outputs=None):
    """Run a test scenario with the given inputs"""
    print(f"\n=== Testing scenario: {scenario_name} ===")
    
    # Reset resources and money
    global resources, money
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    money = 0
    
    # Save the original input function
    original_input = __builtins__.input
    
    # Mock the input function
    __builtins__.input = simulate_input(inputs)
    
    # Capture the output
    with capture_output() as output:
        try:
            # Import the module again to reset all global variables
            exec(open('day15.py').read(), globals())
        except SystemExit:
            print("Program exited")
            raise
        except Exception as e:
            print(f"Error occurred: {e}")
    
    # Restore the original input function
    __builtins__.input = original_input
    
    # Get the captured output
    result = output.getvalue()
    print("Output:")
    print(result)
    
    # Check if expected outputs are in the actual output
    if expected_outputs:
        print("\nChecking expected outputs:")
        all_found = True
        for expected in expected_outputs:
            if expected in result:
                print(f"✓ Found: '{expected}'")
            else:
                print(f"✗ Missing: '{expected}'")
                all_found = False
        
        if all_found:
            print("All expected outputs found!")
        else:
            print("Some expected outputs are missing.")
    
    return result

# Test scenarios
print("Coffee Machine Test Suite")

# Test 1: Buy an espresso with exact change
run_test_scenario(
    "Buy espresso with exact change",
    ["espresso", "6", "0", "0", "0", "off"],
    ["Please insert coins", "Here is your espresso ☕️. Enjoy!"]
)

# Test 2: Buy a latte with extra money
run_test_scenario(
    "Buy latte with extra money",
    ["latte", "12", "0", "0", "0", "off"],
    ["Please insert coins", "Here is $0.50 in change", "Here is your latte ☕️. Enjoy!"]
)

# Test 3: Try to buy with insufficient funds
run_test_scenario(
    "Buy cappuccino with insufficient funds",
    ["cappuccino", "4", "0", "0", "0", "off"],
    ["Please insert coins", "Sorry that's not enough money. Money refunded."]
)

# Test 4: Check report after purchase
run_test_scenario(
    "Check report after purchase",
    ["latte", "10", "0", "0", "0", "report", "off"],
    ["Water: 100ml", "Milk: 50ml", "Coffee: 76g", "Money $2.5"]
)

# Test 5: Try to make coffee with insufficient resources
run_test_scenario(
    "Insufficient resources",
    ["latte", "10", "0", "0", "0", "latte", "10", "0", "0", "0", "off"],
    ["Not enough water!"]
)

# Test 6: Test invalid input
run_test_scenario(
    "Invalid input",
    ["mocha", "off"],
    ["INVALID INPUT!"]
)

print("\nTest suite completed!")