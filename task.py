import heapq

def calc_cable_connection_costs(cables_length) -> int:
    heapq.heapify(cables_length)
    total_costs = 0

    while len(cables_length) > 1:
        first = heapq.heappop(cables_length)
        second = heapq.heappop(cables_length)
        new_item = first + second

        total_costs += new_item
        heapq.heappush(cables_length, new_item)

    return total_costs

cables = [2, 8, 4, 12, 23, 1, 22, 2]

print(f'cables: {cables}, connection cost: {calc_cable_connection_costs(cables)}')


