import heapq
import data

def count(date):
    count = 0
    for key, values in data.data.items():
        if values[0][:len(date)] > date:
            break
        for value in values:
            if value.startswith(date):
                count += 1
                break
    return json_count(count)

def json_count(count):
    return "{ count: " + str(count) + " }"


def popular(date, size):
    if size == 0:
        return None
    popular = []
    for key, values in data.data.items():
        count = 0
        if values[0][:len(date)] > date:
            break
        for value in values:
            if value.startswith(date):
                count += 1
            elif value[:len(date)] > date:
                break
        if count == 0:
            continue
        if len(popular) < size:
            heapq.heappush(popular, (count, key))
        elif count > heapq.nsmallest(1, popular)[0][0]:
            heapq.heapreplace(popular, (count, key))
    popular = sorted(popular, key=lambda tup: tup[0])[::-1]
    return json_pop(popular)

def json_pop(heap):
    json = "{\n  queries: [\n    "
    for values in heap:
        json += "{ query: \"" + values[1] + "\", count: " + str(values[0]) + " },\n    "
    json = json[:-2]
    json += "]\n}"
    print(json)
    return json

