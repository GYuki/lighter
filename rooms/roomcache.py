from rooms.room import Room


class RoomCache(object):
    def __init__(self):
        self._rooms = {}

    def get_room_by_id(self, _id):
        if _id in self._rooms:
            print('Return room with id', _id)
            return self._rooms[_id]
        return None

    def try_create_room(self, _id):
        if _id in self._rooms:
            print('Cant create room with existing id')
            return None
        self._rooms[_id] = Room(_id)
        print('Room', _id, 'created!')
        return self._rooms[_id]
