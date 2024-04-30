class Tree:
    def __init__(self):
        self.num, self.solution = None, {}

    def fit(self, ans):
        for data, res in ans.items():
            node = self
            for decision in data:
                node = node.solution.setdefault(decision, Tree())
            node.num = res

    def predict(self, data):
        node = self
        for decision in data:
            node = node.solution[decision]
        return node.num


def main(arr):
    ans = {
        ('GO', 'GAMS', 'EC', 'LOGOS'): 8,
        ('EJS', 'SCALA', 'EC', 'OX'): 7,
        ('EJS', 'SCALA', 'SAS', 'LOGOS'): 5,
        ('GO', 'GAMS', 'EC', 'OX'): 6,
        ('GO', 'GAMS', 'SAS', 'LOGOS'): 0,
        ('HCL', 'GAMS', 'GN', 'OX'): 9,
        ('HCL', 'SCALA', 'SAS', 'OX'): 2,
        ('GO', 'SCALA', 'SAS', 'OX'): 1,
        ('HCL', 'SCALA', 'SAS', 'LOGOS'): 3,
        ('EJS', 'SCALA', 'SAS', 'OX'): 4
    }
    tree = Tree()
    tree.fit(ans)
    return tree.predict(arr)
