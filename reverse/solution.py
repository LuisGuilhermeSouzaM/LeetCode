class Solution(object):
    def reverse(x):
        x = str(x)
        if x[0] == '-':
            x = x.replace('-',"")
            x = x[::-1]
            x = "-"+ x
        else:
            x = x[::-1]
        x = int(x)
        if (x > (2**31 - 1) or x < -2**31):
            x = 0
        return x
    if __name__ == "__main__":
        print(reverse(
1534236469))
    print()