def find_pressure(n, T, V, R = 0.082057):
    try:
        P = (n*R*T) / V
        return P
    except ZeroDivisionError as error:
        return "Volume must be greater than 0."

test_n = 10
test_T = 298
test_V = 2
test_R = 62.364 #Torr

result = find_pressure(test_n, test_T, test_V, R = test_R)
print("Result:", result)
