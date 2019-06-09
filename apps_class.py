import csv


def normalize(table):
    for i, argument in enumerate(table):
        if type(argument[0]) != str:
            mini = min(argument)
            maxi = max(argument)
            for j, x in enumerate(argument):
                table[i][j] = (x - mini) / (maxi - mini)
    return table


class App:
    name = ""
    size = 0
    price = 0
    rating = 0
    numberOfRatings = 0
    ageAllowed = 0

    def __init__(self, name, price, size, rating, numRating, ageAllowed):
        self.name = name
        self.size = float(size)
        self.price = float(price)
        self.rating = float(rating)
        self.numberOfRatings = int(numRating)
        self.ageAllowed = float(ageAllowed[:-1])

    def print_app(self):
        print(self.name + "\nPrice: " + str(self.price) +
              "\nSize: " + str(self.size) +
              "\nRating: " + str(self.rating) +
              "\nNumber of reviews: " + str(self.numberOfRatings) +
              "\nMinimal Age: " + str(self.ageAllowed) + "\n")


class AppList:
    appList = []

    def __init__(self):
        self.appList = []

    def print_app_list(self):
        for app in self.appList:
            app.print_app()

    def get_data(self, path, maxLines):
        file = csv.reader(open(path, "r"), delimiter=';')

        index = 0
        for line in file:
            if index > 0:
                self.appList.append(App(line[2], line[5], line[3], line[8], line[6], line[11]))
            index += 1
            if index == maxLines:
                break

    def retrieve_table(self, ifNorm):
        table = [[], [], [], [], [], []]
        for app in self.appList:
            table[0].append(app.name)
            table[1].append(app.size)
            table[2].append(app.price)
            table[3].append(app.rating)
            table[4].append(app.numberOfRatings)
            table[5].append(app.ageAllowed)
        if ifNorm == True:
            return normalize(table)
        elif ifNorm == False:
            return table
