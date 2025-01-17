print(" === Task 1 === ")


def find_and_print(messages, current_station):
    mrt_stations = [
        "Songshan",
        "Nanjing Sanmin",
        "Taipei Arena",
        "Nanjing Fuxing",
        "Songjiang Nanjing",
        "Zhongshan",
        "Beimen",
        "Ximen",
        "Xiaonanmen",
        "Chiang Kai-Shek Memorial Hall",
        "Guting",
        "Taipower Building",
        "Gongguan",
        "Wanlong",
        "Jingmei",
        "Dapinglin",
        "Qizhang",
        "Xindian City Hall",
        "Xindian",
    ]
    if current_station not in mrt_stations and current_station != "Xiaobitan":
        print("Invalid station")
        return

    is_Xiaobitan = 0
    if current_station == "Xiaobitan":
        current_index = mrt_stations.index("Qizhang")
        is_Xiaobitan = 1
    else:
        current_index = mrt_stations.index(current_station)
    min_distance = float("inf")
    nearest_friend = None

    for name, msg in messages.items():
        for station in mrt_stations:
            if station in msg:
                distance = (
                    abs(current_index - mrt_stations.index(station)) + is_Xiaobitan
                )
                if distance < min_distance:
                    min_distance = distance
                    nearest_friend = name
        if "Xiaobitan" in msg:
            if is_Xiaobitan == 1:
                distance = 0
            else:
                distance = abs(current_index - mrt_stations.index("Qizhang")) + 1
            if distance < min_distance:
                min_distance = distance
                nearest_friend = name

    print(nearest_friend)


messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you.",
}
find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")  # print Leslie
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian

print(" === Task 2 === ")


# your code here, maybe
def book(consultants, hour, duration, criteria):

    for consultant in consultants:
        if "booked_time" not in consultant:
            consultant["booked_time"] = []

    best_consultant = None

    for consultant in consultants:
        available = True

        for booked_time in consultant["booked_time"]:
            booked_start, booked_end = booked_time
            if hour < booked_end and (hour + duration) > booked_start:
                available = False
                break

        if available:
            if best_consultant is None:
                best_consultant = consultant
            elif criteria == "price" and consultant["price"] < best_consultant["price"]:
                best_consultant = consultant
            elif criteria == "rate" and consultant["rate"] > best_consultant["rate"]:
                best_consultant = consultant

    if best_consultant:
        best_consultant["booked_time"].append((hour, hour + duration))
        print(best_consultant["name"])
    else:
        print("No Service")


consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800},
]
book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John

print(" === Task 3 === ")


def func(*data):
    middle_names = {}

    for name in data:
        words = list(name)
        if len(words) == 2:
            middle_name = words[1]
        elif len(words) == 3:
            middle_name = words[1]
        elif len(words) == 4:
            middle_name = words[2]
        elif len(words) == 5:
            middle_name = words[2]

        if middle_name not in middle_names:
            middle_names[middle_name] = []
        middle_names[middle_name].append(name)

    for middle_name, names in middle_names.items():
        if len(names) == 1:
            print(names[0])
            return

    print("沒有")


func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安

print(" === Task 4 === ")


def get_number(index):
    result = 0  # 初始值
    for i in range(1, index + 1):
        if i % 3 == 0:
            result -= 1
        else:
            result += 4
    print(result)


get_number(1)  # print 4
get_number(5)  # print 15
get_number(10)  # print 25
get_number(30)  # print 70

print(" === Task 5 === ")


def find(spaces, stat, n):

    most_fitted_index = -1
    min_unused_space = float("inf")

    for i in range(len(spaces)):

        if stat[i] == 1 and spaces[i] >= n:

            unused_space = spaces[i] - n

            if unused_space < min_unused_space:
                min_unused_space = unused_space
                most_fitted_index = i

    print(most_fitted_index)


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2)  # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)  # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4)  # print 2
