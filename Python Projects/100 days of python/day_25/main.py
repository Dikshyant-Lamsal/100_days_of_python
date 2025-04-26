import pandas
data=pandas.read_csv("weather_data.csv")
<<<<<<< HEAD
# print(data)
# print(data.columns)

# data_dict = data.to_dict()

# print(data_dict)

# print(data[data.temp>=data.temp.mean()].condition)

# monday=data[data.day=="Monday"]
# print((monday.temp[0]*1.8)+32)

data_dict={
    "students":["a","b","c"],
    "score":[10,12,15]
}

d=pandas.DataFrame(data_dict)
print(d)
d.to_csv("newdata.csv")
=======
print(data["temp"])
>>>>>>> fb7a3bafb62c27db8bfc9a031a13495bd379f315
