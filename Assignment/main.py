
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
    def add_rental(self, car_id, customer_id):
        new_node = RentalNode(car_id, customer_id)

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

    
    def display(self):
        temp = self.head
        while temp:
            print(f"Car {temp.car_id} rented by custormer {temp.customer_id}") 
            temp = temp.next

#Binary tree
#It stores the cars...using binary tree
class CarNode:
    def __init__(self, car_id):
        self.car_id = car_id
        self.left = None
        self.right = None
#Inserting a car
def insert(root, car_id):
    if root is None:
        return CarNode(car_id)
    
    if car_id < root.car_id:
        root.left + insert(root.left, car_id)
    else:
        root.right = insert(root.right, car_id)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return

def delete (root,car_id):
    if root is None:
        return root
    
    if car_id < root.car_id:
        root.left = delete(root.left, car_id)
    elif car_id < root.car_id:
        root.right = delete(root.right, car_id)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = find_min(root.right)
        root.car_id = temp.car_id
        root.right = delete(root.righ, temp.car_id)
    return root


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

def posteroder(root):
    if root:
        posteroder(root.left)
        posteroder(root.right)
        print(root.car_id)   
