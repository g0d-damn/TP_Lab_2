import matplotlib.pyplot as plt

try:
    with open("opendata.txt") as file:
        text = file.readlines()
except FileNotFoundError:
    print("File not found")
    exit()
except Exception as e:
    print(f"Error reading a file: {e}")
    exit()

try:
    data = [line.strip().split(',') for line in text[1:]]
except Exception as e:
    print(f"Error in data processing: {e}")
    exit()

pensions = []
months = []
total = 0
count = 0

for i in data:
    try:
        if (i[0] == 'Средняя пенсия') and (i[1] == 'Забайкальский край') and (i[2][:4] == '2018'):
            pension_value = int(i[3])
            total += pension_value
            count += 1

            pensions.append(pension_value)
            months.append(i[2][5:7])

    except IndexError:
        print(f"Not enough data in the row: {i}")
    except ValueError:
        print(f"Incorrect number format in {i}")
    except Exception as e:
        print(f"Error in data processing: {e}")

if count > 0:
    average = total / count
    print(f"The average pension value is: {average:.2f}")

    plt.figure(figsize=(12, 6))
    plt.plot(months, pensions, marker='o', linestyle='-')
    plt.title('Изменение пенсии в Забайкальском крае за 2018 год')
    plt.xlabel('Месяц')
    plt.ylabel('Пенсия (рублей)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print("No matching data found")