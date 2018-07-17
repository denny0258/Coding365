class Node:
    def __init__(self, root, L=None, R=None, M=None):
        if L is not None:
            self.left, self.right, self.mid = Node(L), Node(R), Node(M)
        else:
            self.left, self.right, self.mid = None, None, None
        self.root = root

    def insert(self, Main_data, insert_Data):
        if self.root:
            if self.left.root:
                pass
            elif self.left.root != Main_data:
                self.left.insert(Main_data, insert_Data)
            else:
                self.left = Node(insert_Data)
                return None
            # ------------------------------------------
            if self.mid.root:
                pass
            elif self.mid.root != Main_data:
                self.mid.insert(Main_data, insert_Data)
            else:
                self.mid = Node(insert_Data)
                return None
            # -----------------------------------------
            if self.right.root:
                pass
            elif self.right.root != Main_data:
                self.right.insert(Main_data, insert_Data)
            else:
                self.right = Node(insert_Data)
                return None
            # ------------------------------------------
        else:
            self.root = insert_Data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.root, end=" ")
        if self.mid:
            self.mid.PrintTree()
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
            Data = input().strip().split(" ")
            if not root:
                root = Node(Data[0], Data[1], Data[2], Data[3])
            else:
                root.insert(Data[0], Data[1])
        elif Data == "e":
            break


if __name__ == "__main__":
    main()
