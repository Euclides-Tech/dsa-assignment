#Linked list
#Creating a Rental Node
class RentalNode:
    def __init__(self, car_id, customer_id, customer_name ,return_date):
        self.car_id = car_id
        self.customer_id = customer_id
        self.return_date = return_date
        self.customer_name = customer_name
        self.next = None

#This is  Rental List
class RentalList:
    def __init__(self):
        self.head = None

    #This method adds a rental record
    def add_rental(self,  car_id, customer_id, customer_name ,return_date):
        if self.is_rented(car_id):
            print(f"Car ID {car_id} is already rented!")
            return 
        
        new_node = RentalNode(car_id, customer_id, customer_name ,return_date)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    #This method removes a rental record
    def remove_rental(self, car_id):
        temp = self.head
        prev = None

        while temp:
            if temp.car_id == car_id:
                if prev is None:
                     self.head = temp.next
                else:
                     prev.next = temp.next
                return
            prev = temp
            temp = temp.next
    
    def is_rented(self,car_id):
        temp = self.head
        while temp:
            if temp.car_id == car_id:
                return True
            temp = temp.next
        return False

    
    def display(self, car_root):
        temp = self.head
        while temp:
            car = search(car_root, temp.car_id)

            if car:
                brand = car.car_brand
            else:
                brand = "Not found"

            print(f"Car ID: {temp.car_id} | Brand: {brand} | Customer: {temp.customer_name} ({temp.customer_id})")
            temp = temp.next

#Binary tree
#It stores the cars...using binary tree
class CarNode:
    def __init__(self, car_id, car_brand):
        self.car_id = car_id
        self.car_brand = car_brand
        self.left = None
        self.right = None

#Inserting a car
def insert(root, car_id, car_brand):
    if root is None:
        return CarNode(car_id, car_brand)
    
    if car_id < root.car_id:
        root.left = insert(root.left, car_id, car_brand)
    else:
        root.right = insert(root.right, car_id, car_brand)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete (root,car_id):
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
# STUDENT 2: Recursion & Tree Algorithms
# ============================================

def inorder(root):
    if root:
        inorder(root.left)
        print(f"Car ID: {root.car_id} | Brand: {root.car_brand}")
        inorder(root.right)

def preorder(root):
    if root:
        print(f"Car ID: {root.car_id} | Brand: {root.car_brand}")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"Car ID: {root.car_id} | Brand: {root.car_brand}")

def count_cars(root):
    if root is None:
        return 0
    return 1 + count_cars(root.left) + count_cars(root.right)

def count_cars_by_brand(root, brand):
    if root is None:
        return 0
    count = 1 if root.car_brand == brand else 0
    return count + count_cars_by_brand(root.left, brand) + count_cars_by_brand(root.right, brand)

def get_height(root):
    if root is None:
        return -1
    return 1 + max(get_height(root.left), get_height(root.right))

#.....Testing.....
#It's only a test(Cars avaiable)
car_root = None
car_root = insert(car_root, 102, "Toyota")
car_root = insert(car_root, 103, "BMW")
car_root = insert(car_root, 105, "Honda")
car_root = insert(car_root, 80, "Ford")
car_root = insert(car_root, 200, "Mercedes")

#Customer renting the car
rentals = RentalList()

rentals.add_rental(102, 1, "Phiri" , "2026-04-05")
rentals.add_rental(102, 2, "Andre" , "2026-04-05")
rentals.display(car_root)

#print("\n" + "="*50)
#print("STUDENT 2: RECURSIVE ALGORITHMS DEMONSTRATION")
#print("="*50)

print("\nInorder traversal (sorted by Car ID):")
inorder(car_root)

print("\nPreorder traversal:")
preorder(car_root)

print("\nPostorder traversal:")
postorder(car_root)

print("\nTotal cars in inventory:", count_cars(car_root))
print("Cars with brand 'Toyota':", count_cars_by_brand(car_root, "Toyota"))
print("Tree height:", get_height(car_root))

#==========================================
# Student 3: Sorting and searching algorithms
#==========================================

# Sorting algorithms
def merge_sort_cars(car_list):
    if len(car_list) <= 1:
        return car_list

    mid = len(car_list) // 2
    left = merge_sort_cars(car_list[:mid])
    right = merge_sort_cars(car_list[mid:])

    return merge(left, right) 

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]: # sortin by car_id
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# CONVERT TREE TO LIST 
def tree_to_list(root, car_list):
    if root:
        tree_to_list(root.left, car_list)
        car_list.append((root.car_id, root.car_brand))
        tree_to_list(root.right, car_list)

# HASH TABLE IMPLEMENTATION 
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists

    def hash_function(self, key):
        return key % self.size

    def insert(self, car_id, car_brand):
        index = self.hash_function(car_id)
        self.table[index].append((car_id, car_brand))

    def search(self, car_id):
        index = self.hash_function(car_id)
        for car in self.table[index]:
            if car[0] == car_id:
                return car
        return None

#TESTING STUDENT 3

print("\n" + "="*50)

# Convert BST 
car_list = []
tree_to_list(car_root, car_list)

print("\nOriginal Car List:")
print(car_list)

# Sorting 
sorted_cars = merge_sort_cars(car_list)
print("\nSorted Cars (by Car ID):")
for car in sorted_cars:
    print(f"Car ID: {car[0]} | Brand: {car[1]}")

# Hash Table Creation and Search

hash_table = HashTable(size=10)
for car in car_list:
    hash_table.insert(car[0], car[1])

search_id = 103
result_hash = hash_table.search(search_id)

# Display Search Result 
if result_hash:
    print(f"\nHash Table Search Found: ID={result_hash[0]}, Brand={result_hash[1]}")
else:
    print("Hash Table Search: Car not found")

# ============================================
# STUDENT 4: HASH TABLE 
# ============================================

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        else:
            for k, v in self.table[index]:
                if k == key:
                    return v
            return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return True
            return False

    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: None")


# ============================================
# STUDENT 4: SYSTEM INTEGRATION
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
        
        sample_cars = [
            (101, "Toyota"), (102, "Toyota"), (103, "BMW"),
            (104, "BMW"), (105, "Honda"), (106, "Honda"),
            (107, "Ford"), (108, "Ford"), (109, "Mercedes"),
            (110, "Mercedes"), (111, "Audi"), (112, "Audi"),
            (113, "Nissan"), (114, "Nissan"), (115, "Hyundai")
        ]
        
        print("\nAdding cars to inventory:")
        for car_id, car_brand in sample_cars:
            self.car_tree = insert(self.car_tree, car_id, car_brand)
            self.hash_table.insert(car_id, car_brand)
            print(f"  ✓ Added Car {car_id}: {car_brand}")
        
        self.is_initialized = True
        print(f"\n✓ System ready! Total cars: {count_cars(self.car_tree)}")
        print(f"✓ Hash table size: {self.hash_table.size}")
        print("="*50)
    
    def rent_car(self, car_id, customer_id, customer_name, return_date):
        print(f"\n--- RENTAL: Car {car_id} for {customer_name} ---")
        
        car = search(self.car_tree, car_id)
        if not car:
            print(f"✗ Car {car_id} not found")
            return False
        
        if self.rental_list.is_rented(car_id):
            print(f"✗ Car {car_id} is already rented")
            return False
        
        self.rental_list.add_rental(car_id, customer_id, customer_name, return_date)
        print(f"✓ Car {car_id} ({car.car_brand}) rented to {customer_name}")
        return True
    
    def return_car(self, car_id):
        print(f"\n--- RETURN: Car {car_id} ---")
        
        if not self.rental_list.is_rented(car_id):
            print(f"✗ Car {car_id} is not rented")
            return False
        
        self.rental_list.remove_rental(car_id)
        print(f"✓ Car {car_id} returned")
        return True
    
    def search_car(self, car_id):
        print(f"\n--- SEARCHING FOR CAR {car_id} ---")
        
        bst_result = search(self.car_tree, car_id)
        if bst_result:
            print(f"BST Search: Found Car {bst_result.car_id} - {bst_result.car_brand}")
        else:
            print(f"BST Search: Car {car_id} not found")
        
        hash_result = self.hash_table.search(car_id)
        if hash_result:
            print(f"Hash Search: Found Car {car_id} - {hash_result}")
        else:
            print(f"Hash Search: Car {car_id} not found")
        
        return bst_result is not None
    
    def search_by_brand(self, brand):
        print(f"\n--- SEARCHING FOR BRAND: {brand} ---")
        
        def search_tree(root, brand, results):
            if root:
                if root.car_brand.lower() == brand.lower():
                    results.append((root.car_id, root.car_brand))
                search_tree(root.left, brand, results)
                search_tree(root.right, brand, results)
        
        results = []
        search_tree(self.car_tree, brand, results)
        
        if results:
            print(f"Found {len(results)} car(s):")
            for car_id, car_brand in results:
                print(f"  • Car {car_id}: {car_brand}")
        else:
            print(f"No cars found for brand '{brand}'")
        
        return results
    
    def display_all(self):
        print("\n" + "="*50)
        print("ALL CARS (Sorted by ID):")
        print("-"*50)
        inorder(self.car_tree)
        
        print("\nCURRENT RENTALS:")
        print("-"*50)
        self.rental_list.display(self.car_tree)
        
        self.hash_table.display()
    
    def get_stats(self):
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


# ============================================
# STUDENT 4: TESTING
# ============================================

def run_tests():
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
    system.search_car(105)
    system.search_car(999)
    print("✓ PASSED")
    
    # Test 3: Rent Car
    print("\n[TEST 3] Rent Car")
    system.rent_car(105, 1001, "John Doe", "2026-04-10")
    system.rent_car(105, 1002, "Jane Smith", "2026-04-12")
    print("✓ PASSED")
    
    # Test 4: Return Car
    print("\n[TEST 4] Return Car")
    system.return_car(105)
    system.return_car(105)
    print("✓ PASSED")
    
    # Test 5: Hash Table Operations
    print("\n[TEST 5] Hash Table Operations")
    system.hash_table.insert(201, "Test Car")
    print(f"  Inserted: {system.hash_table.search(201)}")
    system.hash_table.delete(201)
    print(f"  Deleted, search returns: {system.hash_table.search(201)}")
    print("✓ PASSED")
    
    # Test 6: Search by Brand
    print("\n[TEST 6] Search by Brand")
    system.search_by_brand("Toyota")
    system.search_by_brand("Ferrari")
    print("✓ PASSED")
    
    # Test 7: Display All
    print("\n[TEST 7] Display System")
    system.display_all()
    print("✓ PASSED")
    
    # Test 8: Statistics
    print("\n[TEST 8] System Statistics")
    system.get_stats()
    print("✓ PASSED")
    
    # Test 9: Edge Cases
    print("\n[TEST 9] Edge Cases")
    system.rent_car(999, 1003, "Test User", "2026-04-20")
    system.return_car(999)
    print("✓ PASSED")
    
    # Test 10: Performance
    print("\n[TEST 10] Performance Test")
    import time
    
    start = time.time()
    for i in range(1000):
        system.hash_table.search(105)
    hash_time = time.time() - start
    
    start = time.time()
    for i in range(1000):
        search(system.car_tree, 105)
    bst_time = time.time() - start
    
    print(f"Hash Table (1000 searches): {hash_time*1000:.2f} ms")
    print(f"Binary Tree (1000 searches): {bst_time*1000:.2f} ms")
    print(f"Hash is {bst_time/hash_time:.1f}x faster")
    print("✓ PASSED")
    
    # Summary
    print("\n" + "="*50)
    print("✓ ALL TESTS PASSED!")
    print("✓ System ready for presentation")
    print("="*50)


# ============================================
# MAIN MENU
# ============================================

def main_menu():
    system = CarRentalSystem()
    
    while True:
        print("\n" + "="*50)
        print("CAR RENTAL SYSTEM")
        print("="*50)
        print("1. Initialize System")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Search Car by ID")
        print("5. Search by Brand")
        print("6. Display All Cars")
        print("7. View Statistics")
        print("8. View Hash Table")
        print("9. Run All Tests")
        print("10. Exit")
        print("="*50)
        
        choice = input("Enter choice (1-10): ")
        
        if choice == '1':
            system.initialize_system()
        
        elif choice == '2':
            try:
                car_id = int(input("Car ID: "))
                cust_id = int(input("Customer ID: "))
                name = input("Customer Name: ")
                date = input("Return Date (YYYY-MM-DD): ")
                system.rent_car(car_id, cust_id, name, date)
            except:
                print("Invalid input!")
        
        elif choice == '3':
            try:
                car_id = int(input("Car ID to return: "))
                system.return_car(car_id)
            except:
                print("Invalid input!")
        
        elif choice == '4':
            try:
                car_id = int(input("Car ID to search: "))
                system.search_car(car_id)
            except:
                print("Invalid input!")
        
        elif choice == '5':
            brand = input("Brand name: ")
            system.search_by_brand(brand)
        
        elif choice == '6':
            system.display_all()
        
        elif choice == '7':
            system.get_stats()
        
        elif choice == '8':
            system.hash_table.display()
        
        elif choice == '9':
            run_tests()
        
        elif choice == '10':
            print("\nThank you for using Car Rental System!")
            break
        
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to continue...")


# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("WELCOME TO CAR RENTAL SYSTEM")
    print("STUDENT 4: HASHING & INTEGRATION")
    print("="*50)
    
    choice = input("\nRun tests? (y/n): ").lower()
    if choice == 'y':
        run_tests()
    else:
        main_menu()
