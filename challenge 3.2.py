#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students

def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product = "Apple"

result = linear_search_product(products, target_product)

    print(result)