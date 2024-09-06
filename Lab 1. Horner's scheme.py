def solving_of_horners_scheme(n, ksi, *a):
    list_of_coefficient = list(a)
    result = list_of_coefficient[0]
    for i in range(1, n + 1):
        result = result * ksi + list_of_coefficient[i]
    return result


ans = solving_of_horners_scheme(4, 4, 3, 6, 7, 2, - 10)
print(ans)



