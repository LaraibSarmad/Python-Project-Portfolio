num_of_people = int(input("Number of people attending the cookout:"))

hotdog_order =  int(input("Number of hotdog order:"))


dog = 10

bun = 8

People_Order = num_of_people * hotdog_order


Hotdog_needed = People_Order // dog

Bun_needed = People_Order // bun

leftover_hotdog = People_Order % dog

leftover_bun = People_Order % bun


print("Hot dogs required =", Hotdog_needed)

print("Buns required =", Bun_needed)

print("Hot dogs left over =", leftover_hotdog)

print("Buns left over =", leftover_bun)
