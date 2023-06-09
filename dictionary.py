import gametext

# main room dictionary - contains details of room state
# and possible travel directions
room_map = {
    'a1': {
        'room_name': 'Study',
        'description': (f"{gametext.room_descriptions['a1']}"),
        'details': (f"{gametext.room_details['a1']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'a2': {
        'room_name': 'Black Chasm',
        'description': (f"{gametext.room_descriptions['a2']}"),
        'details': (f"{gametext.room_details['a2']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a3',
        'west': False
    },
    'a3': {
        'room_name': 'Library',
        'description': (f"{gametext.room_descriptions['a3']}"),
        'details': (f"{gametext.room_details['a3']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a4',
        'west': 'a2'
    },
    'a4': {
        'room_name': 'Dining room',
        'description': (f"{gametext.room_descriptions['a4']}"),
        'details': (f"{gametext.room_details['a4']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b4',
        'east': False,
        'west': 'a3'
    },
    'b1': {
        'room_name': 'Upstairs Corridor',
        'description': (f"{gametext.room_descriptions['b1']}"),
        'details': (f"{gametext.room_details['b1']}"),
        'entered': False,
        'completed': False,
        'north': 'a1',
        'south': 'c1',
        'east': 'b2',
        'west': False
    },
    'b2': {
        'room_name': 'Arena',
        'description': (f"{gametext.room_descriptions['b2']}"),
        'details': (f"{gametext.room_details['b2']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': False,
        'west': 'b1'
    },
    'b3': {
        'room_name': 'Storage Room',
        'description': (f"{gametext.room_descriptions['b3']}"),
        'details': (f"{gametext.room_details['b3']}"),
        'entered': False,
        'looked': False,
        'lantern_looked': False,
        'completed': False,
        'north': False,
        'south': 'c3',
        'east': 'b4',
        'west': False
    },
    'b4': {
        'room_name': 'Grand Hall',
        'description': (f"{gametext.room_descriptions['b4']}"),
        'details': (f"{gametext.room_details['b4']}"),
        'entered': False,
        'completed': False,
        'north': 'a4',
        'south': 'c4',
        'east': False,
        'west': 'b3'
    },
    'c1': {
        'room_name': 'Final Door',
        'description': (f"{gametext.room_descriptions['c1']}"),
        'details': (f"{gametext.room_details['c1']}"),
        'entered': False,
        'completed': False,
        'north': 'b1',
        'south': False,
        'east': False,
        'west': False
    },
    'c2': {
        'room_name': 'Alcove',
        'description': (f"{gametext.room_descriptions['c2']}"),
        'details': (f"{gametext.room_details['c2']}"),
        'entered': False,
        'completed': False,
        'north': 'b2',
        'south': False,
        'east': False,
        'west': False
    },
    'c3': {
        'room_name': 'Prison Cell',
        'description': (f"{gametext.room_descriptions['c3']}"),
        'details': (f"{gametext.room_details['c3']}"),
        'entered': True,
        'completed': False,
        'north': 'b3',
        'south': False,
        'east': False,
        'west': False
    },
    'c4': {
        'room_name': 'Stone Corridor',
        'description': (f"{gametext.room_descriptions['c4']}"),
        'details': (f"{gametext.room_details['c4']}"),
        'entered': False,
        'completed': False,
        'north': 'b4',
        'south': 'd4',
        'east': False,
        'west': False
    },
    'd1': {
        'room_name': 'Final Room',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': 'c1',
        'south': False,
        'east': False,
        'west': False
    },
    'd2': {
        'room_name': 'Altar',
        'description': (f"{gametext.room_descriptions['d2']}"),
        'details': (f"{gametext.room_details['d2']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'd3',
        'west': False
    },
    'd3': {
        'room_name': 'Goblin cave',
        'description': (f"{gametext.room_descriptions['d3']}"),
        'details': (f"{gametext.room_details['d3']}"),
        'entered': False,
        'completed': False,
        'sneaked': False,
        'north': False,
        'south': False,
        'east': 'd4',
        'west': False,
    },
    'd4': {
        'room_name': 'Riddle Room',
        'description': (f"{gametext.room_descriptions['d4']}"),
        'details': (f"{gametext.room_details['d4']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': False,
        'west': False
    },
}
