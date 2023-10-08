def thickness_of_the_paper_folded(thickness, times):
    print(thickness * (2 ** times))
    return thickness * (2 ** times)


thickness = float(input("Insert the thickness of the paper to be folded: "))
times = int(input("how many times should the paper to be folded?: "))

result: float
result = thickness_of_the_paper_folded(thickness, times)

print(f"The thickness of the paper folded {times} times is {result}")
