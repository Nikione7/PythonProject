immutable_var = 1, 7.7, "apple", True
print(immutable_var)
# immutable_var[0] = 2
# Ошибка буквально сообщает нам, что кортеж не поддерживает обращение по элементам.
mutable_list = ["footbal", "voleyball", "basketball"]
mutable_list[0] = "tennis"
print(mutable_list)