def paginate(data, limit):
    return data[:limit]

def filter_by_price(data, min_price):
    return [p for p in data if int(p["price"]) >= min_price]