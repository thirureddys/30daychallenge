    def getHeight(self,root):
        #Write your code here
        if not root:
            return -1
        else:
            a = self.getHeight(root.left)
            b = self.getHeight(root.right)
            if (a>b):
                return 1+a
            else:
                return 1+b
