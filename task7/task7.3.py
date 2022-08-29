# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]

class triple:
    def triple_num(self):
        input_array = input("Enter the numbers:")
        input_split = input_array.split(',')
        result = []
        for i in range(len(input_split)):
            input_split[i] = int(input_split[i])
        print(input_split)
        for i in range(len(input_split)):
            sum = 0
            for j in range(i + 1, len(input_split)):
                for z in range(j + 1, len(input_split)):
                    sum = input_split[i] + input_split[j] + input_split[z]
                    if sum == 0:
                        temp = [input_split[i], input_split[j], input_split[z]]
                        result.append(temp)
                        break
        return result


a = triple()
print(a.triple_num())
