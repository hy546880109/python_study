class Permutations(object):

    def is_permutation(self, str1, str2):

        ### 补充代码 ###
        if str1 is None or str2 is None:
            return False
        list(str1).sort
        str1 = ''.join(str1)
        return str1 == str2
        

p = Permutations()
a = p.is_permutation('123','321')
print(a)