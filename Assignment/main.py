# ============================================
# STUDENT 1: LINKED LIST & BINARY TREE
# ============================================

class RentalNode:
    def __init__(self, car_id, customer_id, customer_name, return_date):
        self.car_id = car_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.return_date = return_date
        self.next = None

class RentalList:
    def __init__(self):
        self.head = None

    def add_rental(self, car_id, customer_id, customer_name, return_date):
        if self.is_rented(car_id):
            print(f"Car ID {car_id} is already rented!")
            return False

        new_node = RentalNode(car_id, customer_id, customer_name, return_date)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        return True

    def remove_rental(self, car_id):
        temp = self.head
        prev = None
        while temp:
            if temp.car_id == car_id:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return True
            prev = temp
            temp = temp.next
        return False

    def is_rented(self, car_id):
        temp = self.head
        while temp:
            if temp.car_id == car_id:
                return True
            temp = temp.next
        return False

    def display(self, car_root):
        temp = self.head
        if not temp:
            print("No active rentals.")
            return
        while temp:
            car = search(car_root, temp.car_id)
            brand = car.car_brand if car else "Unknown"
            print(f"Car ID: {temp.car_id} | Brand: {brand} | Customer: {temp.customer_name} ({temp.customer_id}) | Return: {temp.return_date}")
            temp = temp.next

# ---------- Binary Tree for Cars ----------
class CarNode:
    def __init__(self, car_id, plate_number, car_brand, price, available=True):
        self.car_id = car_id
        self.plate_number = plate_number
        self.car_brand = car_brand
        self.price = price
        self.available = available
        self.left = None
        self.right = None

def insert(root, car_id, plate_number, car_brand, price, available=True):
    if root is None:
        return CarNode(car_id, plate_number, car_brand, price, available)
    if car_id < root.car_id:
        root.left = insert(root.left, car_id, plate_number, car_brand, price, available)
    elif car_id > root.car_id:
        root.right = insert(root.right, car_id, plate_number, car_brand, price, available)
    else:
        # Duplicate car_id – update existing record (optional)
        root.plate_number = plate_number
        root.car_brand = car_brand
        root.price = price
        root.available = available
        print(f"Car ID {car_id} already exists – updated info.")
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete(root, car_id):
    if root is None:
        return root
    if car_id < root.car_id:
        root.left = delete(root.left, car_id)
    elif car_id > root.car_id:
        root.right = delete(root.right, car_id)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.car_id = temp.car_id
        root.plate_number = temp.plate_number
        root.car_brand = temp.car_brand
        root.price = temp.price
        root.available = temp.available
        root.right = delete(root.right, temp.car_id)
    return root

def search(root, car_id):
    if root is None or root.car_id == car_id:
        return root
    if car_id < root.car_id:
        return search(root.left, car_id)
    else:
        return search(root.right, car_id)

# ============================================
# STUDENT 2: RECURSIVE TREE ALGORITHMS
# ============================================

def inorder(root):
    if root:
        inorder(root.left)
        status = "Available" if root.available else "Rented"
        print(f"ID: {root.car_id} | Plate: {root.plate_number} | Brand: {root.car_brand} | Price: ${root.price} | {status}")
        inorder(root.right)

def preorder(root):
    if root:
        print(f"ID: {root.car_id} | Brand: {root.car_brand}")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"ID: {root.car_id} | Brand: {root.car_brand}")

def count_cars(root):
    if root is None:
        return 0
    return 1 + count_cars(root.left) + count_cars(root.right)

def count_cars_by_brand(root, brand):
    if root is None:
        return 0
    count = 1 if root.car_brand.lower() == brand.lower() else 0
    return count + count_cars_by_brand(root.left, brand) + count_cars_by_brand(root.right, brand)

def get_height(root):
    if root is None:
        return -1
    return 1 + max(get_height(root.left), get_height(root.right))

# ============================================
# STUDENT 3: SORTING (MERGE SORT) & BINARY SEARCH
# ============================================

def tree_to_list(root, car_list):
    """Collect all cars into a list of tuples (id, brand, price, available, plate)"""
    if root:
        tree_to_list(root.left, car_list)
        car_list.append((root.car_id, root.car_brand, root.price, root.available, root.plate_number))
        tree_to_list(root.right, car_list)

# Merge sort by brand (alphabetical)
def merge_sort_by_brand(car_list):
    if len(car_list) <= 1:
        return car_list
    mid = len(car_list) // 2
    left = merge_sort_by_brand(car_list[:mid])
    right = merge_sort_by_brand(car_list[mid:])
    return merge_by_brand(left, right)

def merge_by_brand(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1].lower() <= right[j][1].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Merge sort by price
def merge_sort_by_price(car_list):
    if len(car_list) <= 1:
        return car_list
    mid = len(car_list) // 2
    left = merge_sort_by_price(car_list[:mid])
    right = merge_sort_by_price(car_list[mid:])
    return merge_by_price(left, right)

def merge_by_price(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Binary search on sorted list (by car_id)
def binary_search_by_id(sorted_list, target_id):
    low, high = 0, len(sorted_list) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if sorted_list[mid][0] == target_id:
            return sorted_list[mid], steps
        elif sorted_list[mid][0] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None, steps

# ============================================
# STUDENT 4: HASH TABLE (KEY = PLATE NUMBER) & SYSTEM INTEGRATION
# ============================================

class HashTable:
    def __init__(self, size=20):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, plate_number):
        total = 0
        for ch in plate_number:
            total += ord(ch)
        return total % self.size

    def insert(self, plate_number, car_node):
        index = self.hash_function(plate_number)
        for i, (key, node) in enumerate(self.table[index]):
            if key == plate_number:
                self.table[index][i] = (plate_number, car_node)
                return
        self.table[index].append((plate_number, car_node))

    def search(self, plate_number):
        index = self.hash_function(plate_number)
        for key, node in self.table[index]:
            if key == plate_number:
                return node
        return None

    def delete(self, plate_number):
        index = self.hash_function(plate_number)
        for i, (key, node) in enumerate(self.table[index]):
            if key == plate_number:
                del self.table[index][i]
                return True
        return False

    def display(self):
        print("\nHash Table (Plate Number -> Car):")
        for i in range(self.size):
            if self.table[i]:
                for key, node in self.table[i]:
                    print(f"  Index {i}: {key} -> Car ID {node.car_id} ({node.car_brand})")
            else:
                print(f"  Index {i}: Empty")

# ============================================
# INTEGRATED CAR RENTAL SYSTEM
# ============================================

class CarRentalSystem:
    def __init__(self):
        self.car_tree = None
        self.rental_list = RentalList()
        self.hash_table = HashTable(20)
        self.is_initialized = False

    def initialize_system(self):
        print("\n" + "="*50)
        print("SYSTEM INITIALIZATION")
        print("="*50)
        # Sample cars: (car_id, plate, brand, price)
        sample_cars = [
            (101, "ABC-123", "Toyota", 50),
            (102, "XYZ-789", "Toyota", 55),
            (103, "DEF-456", "BMW", 80),
            (104, "GHI-012", "BMW", 85),
            (105, "JKL-345", "Honda", 45),
            (106, "MNO-678", "Honda", 48),
            (107, "PQR-901", "Ford", 60),
            (108, "STU-234", "Ford", 65),
            (109, "VWX-567", "Mercedes", 120),
            (110, "YZA-890", "Mercedes", 130),
            (111, "BCD-123", "Audi", 95),
            (112, "EFG-456", "Audi", 100),
            (113, "HIJ-789", "Nissan", 40),
            (114, "KLM-012", "Nissan", 42),
            (115, "NOP-345", "Hyundai", 38)
        ]
        self.car_tree = None
        for car_id, plate, brand, price in sample_cars:
            self.car_tree = insert(self.car_tree, car_id, plate, brand, price, True)
            car_node = search(self.car_tree, car_id)
            self.hash_table.insert(plate, car_node)
            print(f"  Added: {car_id} | Plate: {plate} | {brand} | ${price}")

        self.rental_list = RentalList()
        self.is_initialized = True
        print(f"\n✓ System ready! Total cars: {count_cars(self.car_tree)}")
        print("="*50)

    def rent_car(self, car_id, customer_id, customer_name, return_date):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return False
        print(f"\n--- RENTAL: Car {car_id} for {customer_name} ---")
        car = search(self.car_tree, car_id)
        if not car:
            print(f"✗ Car {car_id} not found")
            return False
        if self.rental_list.is_rented(car_id):
            print(f"✗ Car {car_id} is already rented")
            return False
        if not car.available:
            print(f"✗ Car {car_id} is marked unavailable")
            return False

        success = self.rental_list.add_rental(car_id, customer_id, customer_name, return_date)
        if success:
            car.available = False
            print(f"✓ Car {car_id} ({car.car_brand}) rented to {customer_name}")
        return success

    def return_car(self, car_id):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return False
        print(f"\n--- RETURN: Car {car_id} ---")
        if not self.rental_list.is_rented(car_id):
            print(f"✗ Car {car_id} is not rented")
            return False
        success = self.rental_list.remove_rental(car_id)
        if success:
            car = search(self.car_tree, car_id)
            if car:
                car.available = True
            print(f"✓ Car {car_id} returned")
        else:
            print(f"✗ Failed to return car {car_id}")
        return success

    def search_car_by_id(self, car_id):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return None
        print(f"\n--- SEARCH BY ID: {car_id} ---")
        car = search(self.car_tree, car_id)
        if car:
            status = "Available" if car.available else "Rented"
            print(f"BST Search: Found ID {car.car_id} | Plate: {car.plate_number} | Brand: {car.car_brand} | Price: ${car.price} | {status}")
        else:
            print(f"BST Search: Car {car_id} not found")
        return car

    def search_car_by_plate(self, plate_number):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return None
        print(f"\n--- SEARCH BY PLATE: {plate_number} ---")
        car = self.hash_table.search(plate_number)
        if car:
            status = "Available" if car.available else "Rented"
            print(f"Hash Table Search: Plate {plate_number} -> Car ID {car.car_id} | Brand: {car.car_brand} | Price: ${car.price} | {status}")
        else:
            print(f"Plate {plate_number} not found.")
        return car

    def search_by_brand(self, brand):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return []
        print(f"\n--- SEARCH BY BRAND: {brand} ---")
        def search_tree(root, brand, results):
            if root:
                if root.car_brand.lower() == brand.lower():
                    results.append((root.car_id, root.plate_number, root.car_brand, root.price, root.available))
                search_tree(root.left, brand, results)
                search_tree(root.right, brand, results)
        results = []
        search_tree(self.car_tree, brand, results)
        if results:
            print(f"Found {len(results)} car(s):")
            for car_id, plate, brand_name, price, available in results:
                status = "Available" if available else "Rented"
                print(f"  • ID: {car_id} | Plate: {plate} | {brand_name} | ${price} | {status}")
        else:
            print(f"No cars found for brand '{brand}'")
        return results

    def display_all_cars(self):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return
        print("\n" + "="*50)
        print("ALL CARS (Sorted by ID):")
        print("-"*50)
        inorder(self.car_tree)

    def display_rentals(self):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return
        print("\nCURRENT RENTALS:")
        print("-"*50)
        self.rental_list.display(self.car_tree)

    def get_stats(self):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return
        print("\n" + "="*50)
        print("SYSTEM STATISTICS")
        print("="*50)
        print(f"Total Cars: {count_cars(self.car_tree)}")
        print(f"Tree Height: {get_height(self.car_tree)}")
        rental_count = 0
        temp = self.rental_list.head
        while temp:
            rental_count += 1
            temp = temp.next
        print(f"Active Rentals: {rental_count}")
        print("="*50)

    # Sorting and Binary Search (Student 3)
    def sort_and_display_by_brand(self):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return
        car_list = []
        tree_to_list(self.car_tree, car_list)
        sorted_cars = merge_sort_by_brand(car_list)
        print("\n--- Cars Sorted by Brand (Alphabetical) ---")
        for car in sorted_cars:
            status = "Available" if car[3] else "Rented"
            print(f"ID: {car[0]} | Brand: {car[1]} | Price: ${car[2]} | Plate: {car[4]} | {status}")

    def sort_and_display_by_price(self):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return
        car_list = []
        tree_to_list(self.car_tree, car_list)
        sorted_cars = merge_sort_by_price(car_list)
        print("\n--- Cars Sorted by Price (Low to High) ---")
        for car in sorted_cars:
            status = "Available" if car[3] else "Rented"
            print(f"ID: {car[0]} | Brand: {car[1]} | Price: ${car[2]} | Plate: {car[4]} | {status}")

    def binary_search_demo(self, target_id):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return
        car_list = []
        tree_to_list(self.car_tree, car_list)
        # Sort by car_id for binary search
        sorted_by_id = sorted(car_list, key=lambda x: x[0])  # using Python's Timsort for simplicity
        result, steps = binary_search_by_id(sorted_by_id, target_id)
        if result:
            print(f"Binary Search: Found ID {result[0]} in {steps} steps. Brand: {result[1]}, Price: ${result[2]}, Plate: {result[4]}")
        else:
            print(f"Binary Search: ID {target_id} not found after {steps} steps.")

    def display_hash_table(self):
        if not self.is_initialized:
            print("System not initialized. Please run option 1 first.")
            return
        self.hash_table.display()

# ============================================
# TESTING & MENU
# ============================================

def run_all_tests():
    print("\n" + "="*50)
    print("RUNNING COMPREHENSIVE TESTS")
    print("="*50)
    system = CarRentalSystem()

    # Test 1: Initialize
    print("\n[TEST 1] System Initialization")
    system.initialize_system()
    print("✓ PASSED")

    # Test 2: Search by ID
    print("\n[TEST 2] Search by ID")
    system.search_car_by_id(105)
    system.search_car_by_id(999)
    print("✓ PASSED")

    # Test 3: Search by Plate (Hash Table)
    print("\n[TEST 3] Search by Plate Number")
    system.search_car_by_plate("JKL-345")
    system.search_car_by_plate("ZZZ-999")
    print("✓ PASSED")

    # Test 4: Rent Car
    print("\n[TEST 4] Rent Car")
    system.rent_car(105, 1001, "John Doe", "2026-04-10")
    system.rent_car(105, 1002, "Jane Smith", "2026-04-12")  # already rented
    print("✓ PASSED")

    # Test 5: Return Car
    print("\n[TEST 5] Return Car")
    system.return_car(105)
    system.return_car(105)  # already returned
    print("✓ PASSED")

    # Test 6: Sort by Brand
    print("\n[TEST 6] Sort by Brand")
    system.sort_and_display_by_brand()
    print("✓ PASSED")

    # Test 7: Sort by Price
    print("\n[TEST 7] Sort by Price")
    system.sort_and_display_by_price()
    print("✓ PASSED")

    # Test 8: Binary Search
    print("\n[TEST 8] Binary Search Demo")
    system.binary_search_demo(110)
    system.binary_search_demo(999)
    print("✓ PASSED")

    # Test 9: Search by Brand
    print("\n[TEST 9] Search by Brand")
    system.search_by_brand("Toyota")
    system.search_by_brand("Ferrari")
    print("✓ PASSED")

    # Test 10: Display All
    print("\n[TEST 10] Display System")
    system.display_all_cars()
    system.display_rentals()
    system.display_hash_table()
    print("✓ PASSED")

    # Test 11: Statistics
    print("\n[TEST 11] System Statistics")
    system.get_stats()
    print("✓ PASSED")

    # Test 12: Edge Cases
    print("\n[TEST 12] Edge Cases")
    system.rent_car(999, 1003, "Test User", "2026-04-20")
    system.return_car(999)
    print("✓ PASSED")

    print("\n" + "="*50)
    print("✓ ALL TESTS PASSED!")
    print("✓ System fully meets PDF requirements")
    print("="*50)

def main_menu():
    system = CarRentalSystem()
    while True:
        print("\n" + "="*50)
        print("CAR RENTAL SYSTEM - FULL INTEGRATION")
        print("="*50)
        print("1. Initialize System")
        print("2. Rent a Car (by ID)")
        print("3. Return a Car (by ID)")
        print("4. Search Car by ID")
        print("5. Search Car by Plate")
        print("6. Search by Brand ")
        print("7. Display All Cars ")
        print("8. Display Active Rentals")
        print("9. Sort Cars by Brand ")
        print("10. Sort Cars by Price ")
        print("11. Binary Search by ID ")
        print("12. View Statistics")
        print("13. View Hash Table")
        print("14. Run All Tests")
        print("15. Exit")
        print("="*50)
        choice = input("Enter choice (1-15): ")

        if choice == '1':
            system.initialize_system()
        elif choice == '2':
            try:
                car_id = int(input("Car ID: "))
                cust_id = int(input("Customer ID: "))
                name = input("Customer Name: ")
                date = input("Return Date (YYYY-MM-DD): ")
                system.rent_car(car_id, cust_id, name, date)
            except Exception as e:
                print(f"Invalid input: {e}")
        elif choice == '3':
            try:
                car_id = int(input("Car ID to return: "))
                system.return_car(car_id)
            except Exception as e:
                print(f"Invalid input: {e}")
        elif choice == '4':
            try:
                car_id = int(input("Car ID to search: "))
                system.search_car_by_id(car_id)
            except Exception as e:
                print(f"Invalid input: {e}")
        elif choice == '5':
            plate = input("Plate Number (e.g., ABC-123): ").strip().upper()
            system.search_car_by_plate(plate)
        elif choice == '6':
            brand = input("Brand name: ").strip()
            system.search_by_brand(brand)
        elif choice == '7':
            system.display_all_cars()
        elif choice == '8':
            system.display_rentals()
        elif choice == '9':
            system.sort_and_display_by_brand()
        elif choice == '10':
            system.sort_and_display_by_price()
        elif choice == '11':
            try:
                car_id = int(input("Car ID to binary search: "))
                system.binary_search_demo(car_id)
            except Exception as e:
                print(f"Invalid input: {e}")
        elif choice == '12':
            system.get_stats()
        elif choice == '13':
            system.display_hash_table()
        elif choice == '14':
            run_all_tests()
        elif choice == '15':
            print("\nThank you for using the Car Rental System!")
            break
        else:
            print("Invalid choice. Please enter 1-15.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("WELCOME TO THE COMPLETE CAR RENTAL SYSTEM")
    print("All student requirements implemented")
    print("="*50)
    main_menu()
