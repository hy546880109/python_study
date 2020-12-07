class UniqueChars(object):

    def has_unique_chars(self, string):

        ### 补充代码 ###
        if string is None:
            return False
        return len(set(string)) == len(string)

q = UniqueChars()
a = q.has_unique_chars(None)
print(a)