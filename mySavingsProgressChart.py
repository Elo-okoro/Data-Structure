import matplotlib.pyplot as plt
weeks = ["1", "2", "3", "4"]
savings = [450, 560, 760, 1200]
# plt.plot(weeks, savings, color="yellow", marker="o", linestyle = "dashed",
        #  linewidth = '5')
plt.bar(weeks, savings, color="pink")
plt.title("My Savings Progress Chart")
plt.xlabel("Weeks")
plt.ylabel("Amount Of Saved Money")
plt.grid(axis = "y")
# plt.grid()
plt.ylim(200, 1500)
plt.show()
