from datetime import datetime

# ============================================
# STUDENT 1: LINKED LIST & BINARY TREE
# ============================================

class RentalNode:
    def __init__(self, car_id, customer_id, customer_name, return_date):
        self.car_id = car_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.booking_time = datetime.now()
        self.return_time = None
        self.return_date = return_date
        self.car_model = None
        self.next = None


class RentalList:
    def __init__(self):
        self.head = None

    def add_rental(self, car_id, customer_id, customer_name, return_date):
        if self.is_rented(car_id):
            print(f"Car ID {car_id} is already rented!")
            return False

        new_node = RentalNode(car_id, customer_id, customer_name, return_date)

        if not self.head:
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
                temp.return_time = datetime.now()
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
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
            booking = temp.booking_time.strftime("%Y-%m-%d %H:%M:%S")
            ret_time = temp.return_time.strftime("%Y-%m-%d %H:%M:%S") if temp.return_time else "Not returned"
            print(f"Car ID: {temp.car_id} | Brand: {brand} | Model: {temp.car_model}| Customer: {temp.customer_name} ({temp.customer_id}) | Return Date: {temp.return_date} | Booked At: {booking} | Returned At: {ret_time}")
            temp = temp.next
      


# ---------- Binary Tree ----------
class CarNode:
    def __init__(self, car_id, plate_number, car_brand, car_model,  price, available=True):
        self.car_id = car_id
        self.plate_number = plate_number
        self.car_brand = car_brand
        self.car_model = car_model
        self.price = price
        self.available = available
        self.left = None
        self.right = None


def insert(root, car_id, plate_number, car_brand, car_model, price, available=True):
    if root is None:
        return CarNode(car_id, plate_number, car_brand, car_model, price, available)

    if car_id < root.car_id:
        root.left = insert(root.left, car_id, plate_number, car_brand, car_model, price, available)
    elif car_id > root.car_id:
        root.right = insert(root.right, car_id, plate_number, car_brand, car_model, price, available)
    else:
        root.plate_number = plate_number
        root.car_brand = car_brand
        root.car_model = car_model
        root.price = price
        root.available = available
    return root


def find_min(node):
    while node and node.left:
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
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        temp = find_min(root.right)
        root.car_id = temp.car_id
        root.plate_number = temp.plate_number
        root.car_brand = temp.car_brand
        root.car_model = temp.car_model
        root.price = temp.price
        root.available = temp.available

        root.right = delete(root.right, temp.car_id)

    return root


def search(root, car_id):
    if root is None or root.car_id == car_id:
        return root
    if car_id < root.car_id:
        return search(root.left, car_id)
    return search(root.right, car_id)


# ============================================
# STUDENT 2: TREE ALGORITHMS
# ============================================

def inorder(root):
    if root:
        inorder(root.left)
        status = "Available" if root.available else "Rented"
        print(f"ID: {root.car_id} | Plate: {root.plate_number} | Brand: {root.car_brand} | Model: {root.car_model} | Price: ${root.price} | {status}")
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


def get_height(root):
    if root is None:
        return -1
    return 1 + max(get_height(root.left), get_height(root.right))


# ============================================
# STUDENT 3: SORTING & SEARCH
# ============================================

def tree_to_list(root, car_list):
    if root:
        tree_to_list(root.left, car_list)
        car_list.append((root.car_id, root.car_brand, root.car_model, root.price, root.available, root.plate_number))
        tree_to_list(root.right, car_list)


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


def binary_search_by_id(sorted_list, target_id):
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid][0] == target_id:
            return sorted_list[mid]
        elif sorted_list[mid][0] < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None


# ============================================
# STUDENT 4: HASH TABLE
# ============================================

class HashTable:
    def __init__(self, size=20):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, plate):
        return sum(ord(c) for c in plate) % self.size

    def insert(self, plate, car):
        index = self.hash_function(plate)

        for i, (key, _) in enumerate(self.table[index]):
            if key == plate:
                self.table[index][i] = (plate, car)
                return

        self.table[index].append((plate, car))

    def search(self, plate):
        index = self.hash_function(plate)

        for key, car in self.table[index]:
            if key == plate:
                return car
        return None

    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            if bucket:
                for key, car in bucket:
                    print(f"Index {i}: {key} -> {car.car_brand}")
            else:
                print(f"Index {i}: Empty")


# ============================================
# SYSTEM
# ============================================

class CarRentalSystem:
    def __init__(self):
        self.car_tree = None
        self.rental_list = RentalList()
        self.hash_table = HashTable()
        self.is_initialized = False
        self.available_cars()

    #def initialize_system(self):
     #   self.available_cars()

    def available_cars(self):
        cars = [
            (101, "ABC-123", "Toyota"," Corolla", 50),
            (102, "XYZ-789", "Toyota","Mark X", 60),
            (103, "DEF-456", "BMW", "Z3", 70),
            (104, "GHI-012", "BMW", "420i", 80),
            (105, "JKL-345", "HONDA", "Fit", 35),
            (106, "JPL-972", "HONDA", "Civic", 45),
            (107, "LTS-562", "MERCEDES-BENZ", "C-CLASS C200", 120),
            (108, "TDF-726", "MERCEDES-BENZ", "E-CLASS E250", 90)

            

        ]

        for cid, plate, brand, model, price in cars:
            self.car_tree = insert(self.car_tree, cid, plate, brand, model, price)
            self.hash_table.insert(plate, search(self.car_tree, cid))

        self.is_initialized = True
        print("=========================================")
        print("WELCOME TO CAR RENTAL MANAGEMENT SYSTEM")
        print("=========================================")

    def rent_car(self, car_id, customer_id, customer_name, return_date):
        # ... existing checks ...
        car = search(self.car_tree, car_id)
        if not car:
            print(f"Car ID {car_id} not found!")
            return False
        self.rental_list.add_rental(car_id, customer_id, customer_name, return_date)
        car.available = False
        print(f"✓ Car {car_id} {car.car_brand} - {car.car_model} rented to {customer_name} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    def return_car(self, car_id):
        # ... existing checks ...
        self.rental_list.remove_rental(car_id)
        car = search(self.car_tree, car_id)
        if car:
            car.available = True
        print(f"✓ Car {car_id} returned at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True


    def display_all(self):
        inorder(self.car_tree)

    def display_rentals(self):
        self.rental_list.display(self.car_tree)

    def get_stats(self):
        total_rentals = 0
        active_rentals = 0
        temp = self.rental_list.head
        while temp:
            total_rentals += 1
            if not temp.return_time:
                active_rentals += 1
            temp = temp.next

        print("\n--- Rental Statistics ---")
        print(f"Total Rentals Ever: {total_rentals}")
        print(f"Active Rentals: {active_rentals}")


# ============================================
# MENU
# ============================================

def main_menu():
    system = CarRentalSystem()


    while True:
        print("1. Add a Car")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Display Cars")
        print("5. Display Rentals")
        print("6. Display stats")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == '1':
            cid = int(input("Car ID: "))
            plate = input("Plate Number: ")
            brand = input("Brand: ")
            model = input("Model: ")
            price = int(input("Price: "))
            system.car_tree = insert(system.car_tree, cid, plate, brand, model, price)
            system.hash_table.insert(plate, search(system.car_tree, cid))
            print(f"✓ Car {cid} added successfully")

        elif choice == '2':
            system.display_all()
           

            car_id = int(input("Car ID: "))
            cust = int(input("Customer ID: "))
            name = input("Name: ")
            date = input("Return Date: ")
            system.rent_car(car_id, cust, name, date)

        elif choice == '3':
            car_id = int(input("Car ID: "))
            system.return_car(car_id)

        elif choice == '4':
            system.display_all()

        elif choice == '5':
            system.display_rentals()
        
        elif choice == '6':
            system.get_stats()

        elif choice == '0':
            print("Developed by @Euclides, @Andrew, @Tshepo, @Kangala")
            print("GoodBye")
            break


# ============================================
# RUN
# ============================================

if __name__ == "__main__":
    main_menu()
