from Buffer import Buffer

buffer = Buffer()
buffer.add(5, 46, 23)
print(buffer.get_current_part())
buffer.add(12, 34, 3)
print(buffer.get_current_part())
buffer.add(754, 83, 932, 101)
print(buffer.get_current_part())