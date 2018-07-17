class Node:
    def __init__(self, data):
        self.left,self.right = None,None
        self.data = data

    def insert(self, data):
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data,end = " ")
        if self.right:
            self.right.PrintTree()

def main():
    root = None
    while True:
        Data = input().strip()
        if Data == "p":
            if not root:
                print("null")
            else:
                root.PrintTree()
                print("")
        elif Data == "i":
            Data = int(input().strip())
            if not root:
                root = Node(Data)
            else:
                root.insert(Data)
        elif Data == "e":
            break
if __name__ == "__main__":
    main()