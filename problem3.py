def thickness_of_the_paper_folded(thickness, times):
    a = 1
    for i in range(0, times):
        a = 2 * a
    return (thickness*a)/1000

thickness = float(input("Insert the thickness of the paper to be folded: "))
times = int(input("how many times should the paper to be folded?: "))

result: float
result = thickness_of_the_paper_folded(thickness, times)

print(f"The thickness of the paper folded {times} times is {result:.2f}")
print(result)
