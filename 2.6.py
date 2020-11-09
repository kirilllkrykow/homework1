n = str(input("Введите товары, участвующие в акции, через запятую:"))
i = str(input("Введите их изначальную стоимость также через запятую:"))
t = str(input("Введите количество каждого товара на складе:"))
r = str(input("Введите единицы измерения для товаров:"))
list_name = n.split(",")
list_value = i.split(",")
list_number = t.split(",")
list_measurment = r.split(",")
Dict1=dict(name=list_name[0],number=list_number[0], value=list_value[0], measurment= list_measurment[0])
Dict2=dict(name=list_name[1],number=list_number[1], value=list_value[1], measurment= list_measurment[1])
Dict3=dict(name=list_name[2],number=list_number[2], value=list_value[2], measurment= list_measurment[2])
Dict4=dict(name=list_name[3],number=list_number[3], value=list_value[3], measurment= list_measurment[3])
Complex_list = [(1,Dict1),(2,Dict2),(3,Dict3),(4,Dict4)] """Структура товары"""
Dict_common = dict(name=[Dict1.get("name"),Dict2.get("name"),Dict3.get("name"),Dict4.get("name")],
                   number=[Dict1.get("number"),Dict2.get("number"),Dict3.get("number"),Dict4.get("number")],
                   value=[Dict1.get("value"),Dict2.get("value"),Dict3.get("value"),Dict4.get("value")],
                   measurment=[Dict1.get("measurment"),Dict2.get("measurment"),Dict3.get("measurment"),Dict4.get("measurment")])
"""Это задание очень плохо получилось, после сдачи обязуюсь его переправить"""

