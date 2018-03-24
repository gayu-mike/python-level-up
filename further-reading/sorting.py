# >>> a = [1, 3, 7, 10, 5, 2]
# >>> b = [2, 3, 5]
# b是a的子集, 请按a的顺序对b进行排序?


def my_sort(n: int)-> int:
    a = [1, 3, 7, 10, 5, 2]
    return a.index(n)


def main():
    b = [2, 3, 5]
    print(sorted(b, key=my_sort))
    print()


if __name__ == '__main__':
    main()
