import pandas as pd
vet_visits = pd.read_csv("vet_visits.csv", parse_dates=["date"])
vet_visits.drop_duplicates(subset="name") #drop duplicates names

unique_dogs= vet_visits.drop_duplicates(subset=["name","breed"]) 
unique_dogs["breed"].value_counts()
unique_dogs["breed"].value_counts(sort=True)
unique_dogs["breed"].value_counts(normalize =True)



# Drop duplicate store/type combinations

sales = pd.read_csv("sales.csv", parse_dates=["date"])

print(sales.head())
store_types = sales.drop_duplicates(subset=["store","type"]) 
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store","department"]) 
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates["date"])



# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize =True)
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)