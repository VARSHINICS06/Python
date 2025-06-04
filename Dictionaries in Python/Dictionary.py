my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
print(karnataka_food["Mysuru"])  # Output: Mysore Pak
print(karnataka_food.get("Mangaluru"))  # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found"))  # Output: Not Found

karnataka_food["Shivamogga"] = "Kadubu"
print(karnataka_food)

karnataka_food["Bengaluru"] = "Ragi Mudde"

# pop()

mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)  # Output: Mysore Pak

del karnataka_food["Mangaluru"]
karnataka_food.clear()
