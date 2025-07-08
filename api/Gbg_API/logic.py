# api/gbg/logic.py

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class GothenburgPortDataCollector:
    def __init__(self):
        self.api_key = os.getenv('PORT_API_KEY', 'demo_key')

    def get_container_availability(self):
        return {
            'availability': 85,
            'in_use': 892,
            'maintenance': 156,
            'total': 1247,
            'timestamp': datetime.now().isoformat()
        }

    def get_port_queue(self):
        return {
            'ships_in_queue': 14,
            'avg_wait_time': 4.2,
            'max_wait_time': 12.5,
            'min_wait_time': 1.8,
            'timestamp': datetime.now().isoformat()
        }

    def get_ships_in_port(self):
        return {
            'ships_in_port': 7,
            'capacity_used': 78,
            'capacity_available': 22,
            'timestamp': datetime.now().isoformat()
        }

    def calculate_stress_index(self, container_data, queue_data, ships_data):
        availability_score = (container_data['availability'] / 100) * 30
        queue_score = max(0, (30 - queue_data['ships_in_queue']) / 30) * 30
        capacity_score = (ships_data['capacity_used'] / 100) * 40
        stress_index = 100 - (availability_score + queue_score + capacity_score)
        return max(0, min(100, stress_index))

    def get_weekly_data(self):
        days = ['Mån', 'Tis', 'Ons', 'Tor', 'Fre', 'Lör', 'Sön']
        return {
            'container_availability': {'labels': days, 'data': [85, 72, 68, 90, 78, 82, 88], 'trend': 'up'},
            'port_queue': {'labels': days, 'data': [12, 18, 25, 15, 22, 19, 14], 'trend': 'down'},
            'ships_in_port': {'labels': days, 'data': [8, 12, 15, 11, 14, 9, 7], 'trend': 'up'},
            'stress_index': {'labels': days, 'data': [65, 78, 85, 72, 80, 75, 68], 'trend': 'down'}
        }

    def collect_all_data(self):
        container = self.get_container_availability()
        queue = self.get_port_queue()
        ships = self.get_ships_in_port()
        if all([container, queue, ships]):
            return {
                'current': {
                    'container_availability': container,
                    'port_queue': queue,
                    'ships_in_port': ships,
                    'stress_index': self.calculate_stress_index(container, queue, ships)
                },
                'weekly': self.get_weekly_data(),
                'timestamp': datetime.now().isoformat()
            }
        return None
