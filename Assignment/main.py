
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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.car_id)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.car_id)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.car_id)   


#.....Testing.....
#It's only a test(Cars avaiable)
car_root = None
car_root = insert(car_root, 102, "Toyota")
car_root = insert(car_root, 103, "BMW")

#Customer renting the car
rentals = RentalList()


rentals.add_rental(102, 1, "Phiri" , "2026-04-05" )
#....It CHECKS IF THE CAR IS ALREADY RENTED......
rentals.add_rental(102, 2, "Andre" , "2026-04-05" )
#Displays the rental
rentals.display(car_root)
