import matplotlib.pyplot as plt
import pandas

data=pandas.read_csv('modified_test.csv')
plt.plot(data.id,data.salary)
plt.xlabel('emp_id')
plt.ylabel('salary_range')
plt.title('Emp id vs salary')
plt.show()

# show in bar chart
plt.bar(data.id,data.salary)
plt.xlabel('emp_id')
plt.ylabel('salary_range')
plt.title('Emp id vs salary')
plt.show()


# since the above charts are really messy so we can club some data to get the idea
city_count=data.country.value_counts()

plt.bar(city_count.index,city_count.values)

plt.xlabel('id')
plt.ylabel('Users')
plt.title('country vs no. of users')

plt.show()
