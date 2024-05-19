import pandas as pd
import heapq


class MetroMap:
    def __init__(self):
        self.graph = {}

    def add_station(self, station):
        if station not in self.graph:
            self.graph[station] = {}

    def add_connection(self, from_station, to_station, distance):
        self.add_station(from_station)
        self.add_station(to_station)
        self.graph[from_station][to_station] = distance
        self.graph[to_station][from_station] = distance  

    def dijkstra(self, start, end):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))
        distances = {station: float('inf') for station in self.graph}
        distances[start] = 0
        previous_stations = {station: None for station in self.graph}

        while priority_queue:
            current_distance, current_station = heapq.heappop(priority_queue)

            if current_station == end:
                break

            for neighbor, weight in self.graph[current_station].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_stations[neighbor] = current_station
                    heapq.heappush(priority_queue, (distance, neighbor))

        path, current_station = [], end
        while previous_stations[current_station] is not None:
            path.insert(0, current_station)
            current_station = previous_stations[current_station]
        if path:
            path.insert(0, current_station)
        return path, distances[end]


def main():
    # Load Excel data
    data = pd.read_excel('7_detail_table_cust_cust_distances.xls')

    # Create metro map instance
    metro_map = MetroMap()

    # Populate the graph with stations and connections
    for _, row in data.iterrows():
        from_station = row['CUSTOMER_CODE_FROM']
        to_station = row['CUSTOMER_CODE_TO']
        distance = row['DISTANCE_KM']
        metro_map.add_connection(from_station, to_station, distance)

        # Define start station
        start_station = 136500

        # List of end stations for 20 instances
        end_stations = [ 15110, 139621, 924681, 140660, 138096, 923079, 136590, 139645, 142817,
            924138, 144739, 924016, 139661, 921471, 920120, 920296, 141028, 941139,
            1408, 923163]

    for end_station in end_stations:
        path, distance = metro_map.dijkstra(start_station, end_station)
        print(
            f"The shortest path from {start_station} to {end_station} is: {' -> '.join(map(str, path))} with a total distance of {distance} km")


if __name__ == "__main__":
    main()
