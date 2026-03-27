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
