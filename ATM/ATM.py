class ATM:

    def __init__(self):
        return

    def solutions(self, values, ammounts, variation, ammount, position):
        res_list = []
        value = self.compute(values, variation)
        if value < ammount:
            for i in range(position, len(values)):
                new_variation = variation.copy()
                new_variation[i] = new_variation[i] + 1
                newList = self.solutions(values, ammounts, new_variation, ammount, i)
                if newList != None:
                    res_list.extend(newList)
        elif value == ammount:
            res_list.append(variation)
        return res_list

    def compute(self, values, variation):
        ret = 0
        for i in range(0, len(variation)):
            ret = ret + values[i]*variation[i]
        return ret


