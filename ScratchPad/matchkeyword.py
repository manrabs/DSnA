def process_data(data):
    match data:
        case {"type": "user", "name": str(name), "age": int(age)} if age >= 18:
            print(f"Adult user: {name}")
        case {"type": "user", "name": str(name)}:
            print(f"Minor user: {name}")
        case {"type": "product", "name": str(name), "price": float(price)}:
            print(f"Product: {name}, Price: ${price:.3f}")
        case [int(x), int(y)]:
            print(f"Point: ({x}, {y})")
        case _:
            print("Unknown data format")

# Usage
process_data({"type": "user", "name": "Alice", "age": 30})
process_data({"type": "user", "name": "Bob", "age": 15})
process_data({"type": "product", "name": "Laptop", "price": 999.99})
process_data([10, 20])
process_data("invalid data")