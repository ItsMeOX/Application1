from typing import List

# Iterate through orders and 
# 1. get all the unique foods and sort the foods alphabatically.
# 2. get all the table numbers.
# Initialize a food_mapper dictionary which food_mapper[food] = index.
# Iterate through orders and populate the count of food for each table number.
# Sort the table numbers by in increasing manner.
# Initialize 'res' array, 
# 1. for the header, append ['table'] + [list of foods]
# 2. for the data  , append [table number] + [list of counter of foods]

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = {}

        for _, table, food in orders:
            foods.add(food)
            tables[table] = 1
        
        foods = sorted(foods)
        food_mapper = {food: i for i, food in enumerate(foods)}

        for table in tables:
            tables[table] = [0] * len(foods)
        
        for _, table, food in orders:
            food_idx = food_mapper[food]
            tables[table][food_idx] += 1
        
        keys = sorted(map(int, tables.keys()))

        res = [['Table']]
        for food in foods:
            res[0].append(food)
        for key in keys:
            res.append([str(key)]+list(map(str, tables[str(key)])))       

        return res 
    
# Optimization: 
# Instead of creating list containing many '0', we will use a dictionary to store all the counts of foods.
# If a food does is not in tables[table], just append '0',
# otherwise append the count.

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = {}

        for _, table, food in orders:
            foods.add(food)
            if table not in tables:
                tables[table] = {}
            tables[table][food] = tables[table].get(food, 0) + 1
        
        foods = sorted(foods)

        res = [['Table']]
        for food in foods:
            res[0].append(food)
        for table in sorted(tables.keys(), key=int):
            table = str(table)
            temp = [table]
            for food in foods:
                if food in tables[table]:
                    temp.append(str(tables[table][food]))
                else:
                    temp.append('0')
            res.append(temp)

        return res 