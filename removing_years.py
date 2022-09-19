def write_file():
    buffer = []
    with open("cars_exercise.txt", "r") as file:
        for line in file:
            buffer.append(line.strip())
    print(buffer)
    cars = []
    i = 0
    while i < len(buffer):
        make = buffer[i]
        model = buffer[i + 1]
        year = buffer[i + 2]
        cars.append({
            "make": make,
            "model": model
        })
        i += 3
    print(cars)

    j = 0
    
    with open("removing_years.txt", mode="w") as my_file:
        while j < len(cars):
          my_file.write(str(cars[j]["make"]+"\n"+cars[j]["model"]+"\n"))
          j += 1

write_file()
