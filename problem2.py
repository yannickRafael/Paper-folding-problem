def thickness_of_the_paper_folded(thickness, times):
    return ((thickness * (2 ** times))/1000)


thickness = float(input("Insert the thickness of the paper to be folded: "))
times = int(input("how many times should the paper to be folded?: "))


print(f"The thickness of the paper folded {times} times is {result:.2f}")
print(result)
result: float
result = thickness_of_the_paper_folded(thickness, times)
