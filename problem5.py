def thickness_of_the_paper_folded(thickness, times):
    list = []
    list.append(thickness)
    a = 1
    for i in range(0, times):
        a = 2 * a
        t =  (thickness*a)/1000
        list.append(t)
    return list

thickness = float(input("Insert the thickness of the paper to be folded: "))
times = int(input("how many times should the paper to be folded?: "))

result: float
list = thickness_of_the_paper_folded(thickness, times)
result = list[-1]

print(f'''The thickness of the paper folded {times} times is {result:.2f}
          The length of the list is {len(list)}
''')
print(result)
