def solve(s):
#     # l = s.split(" ")
#     # for i in l:
#     #     x=(i.capitalize())
#     #     y = " ".join(x)
#     #     print(y)
#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

    y = " ".join((i.capitalize() for i in s.split(" ")))
    print(y)

# def solve(s):
#     return " ".join([name.capitalize() for name in s.split(" ")])
str = input("Enter any string: ")
solve(str)

