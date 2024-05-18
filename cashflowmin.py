from collections import defaultdict


class CashFlowMinimizer:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(int))

    def add_transaction(self, from_person, to_person, amount):
        self.graph[from_person][to_person] += amount

    def minimize_cash_flow(self):
        net_amounts = defaultdict(int)

        # Calculate net amounts
        for person in self.graph:
            for to_person in self.graph[person]:
                net_amounts[person] -= self.graph[person][to_person]
                net_amounts[to_person] += self.graph[person][to_person]

        net_list = []
        for person, amount in net_amounts.items():
            if amount != 0:
                net_list.append((person, amount))

        net_list.sort(key=lambda x: x[1])

        while net_list:
            creditor = net_list.pop()
            debtor = net_list.pop(0)

            min_amount = min(-debtor[1], creditor[1])
            net_amounts[creditor[0]] -= min_amount
            net_amounts[debtor[0]] += min_amount

            print(f"{debtor[0]} pays {min_amount} to {creditor[0]}")

            if net_amounts[creditor[0]] != 0:
                net_list.append((creditor[0], net_amounts[creditor[0]]))
            if net_amounts[debtor[0]] != 0:
                net_list.insert(0, (debtor[0], net_amounts[debtor[0]]))

            net_list.sort(key=lambda x: x[1])


if __name__ == "__main__":
    cash_flow_minimizer = CashFlowMinimizer()

    cash_flow_minimizer.add_transaction("Friend 1", "Friend 3", 4000)
    cash_flow_minimizer.add_transaction("Friend 1", "Friend 2", 2000)
    cash_flow_minimizer.add_transaction("Friend 2", "Friend 3", 3000)

    print("Original transactions:")
    for from_person in cash_flow_minimizer.graph:
        for to_person in cash_flow_minimizer.graph[from_person]:
            amount = cash_flow_minimizer.graph[from_person][to_person]
            if amount != 0:
                print(f"{from_person} owes {to_person}: {amount}")

    print("\nMinimized cash flow:")
    cash_flow_minimizer.minimize_cash_flow()
