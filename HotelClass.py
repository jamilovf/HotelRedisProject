import redis
from _datetime import datetime

class HotelClass():

    def __init__(self):
        redis_host = '192.168.0.67'
        redis_port = 6379

        self.r = redis.Redis(host = redis_host,
                         port =redis_port,
                         decode_responses = True)

    def add_company(self, hotel_name, creation_year):
        if self.r.sismember('hotels', hotel_name):
            print('This hotel exists')
        else:
            self.r.sadd('hotels', hotel_name)
            self.r.hmset('hotel_' + hotel_name,
                         {
                             'title': hotel_name,
                             'creation_year': creation_year
                         })

    def add_new_branch(self, hotel_name, branch_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        else:
            if self.r.sismember('branches', hotel_name + '_' + branch_name):
                print('This branch exists')
            else:
                self.r.sadd('branches', hotel_name + '_' + branch_name)
                self.r.hmset('branch_' + hotel_name + '_' + branch_name,
                         {
                             'title': branch_name,
                             'hotel': hotel_name
                         })

    def list_all_branches(self, hotel_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        else:
            print('Branches of ' + hotel_name + ':')
            for i in self.r.smembers('branches'):
                if self.r.hget('branch_' + i, 'hotel') == hotel_name:
                    print(self.r.hget('branch_' + i, 'title'))

    def add_new_room_to_branch(self, hotel_name, branch_name, room_number):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        else:
            if self.r.sismember('rooms', hotel_name + '_' + branch_name + '_' + room_number):
                print('This room exists')
            else:
                self.r.sadd('rooms', hotel_name + '_' + branch_name + '_' + room_number)
                self.r.hmset('room_'+ hotel_name + '_' + branch_name + '_' + room_number,
                         {
                             'number': room_number,
                             'branch': branch_name,
                             'hotel': hotel_name
                         })

    def list_branch_rooms(self, hotel_name, branch_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        else:
            print('Rooms of ' + hotel_name + ' ' + branch_name + ':')
            for i in self.r.smembers('rooms'):
                if self.r.hget('room_' + i, 'hotel') == hotel_name and \
                        self.r.hget('room_' + i, 'branch') == branch_name :
                    print(self.r.hget('room_' + i, 'number'))

    def add_new_guest(self, id, first_name, last_name, hotel_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        else:
            if self.r.sismember('guests', hotel_name + '_' + id):
                print('Guest with this id exists')
            else:
                self.r.sadd('guests', hotel_name + '_' + id)
                self.r.hmset('guest_' + hotel_name + '_' + id,
                         {
                             'id': id,
                             'first_name': first_name,
                             'last_name': last_name,
                             'hotel': hotel_name
                         })

    def is_room_empty(self, hotel_name, branch_name, room_number):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        elif not self.r.sismember('rooms', hotel_name + '_' + branch_name + '_' + room_number):
            print('This room does not belong to this branch')
        else:
            for i in self.r.smembers('rooms'):
                if self.r.hget('room_' + i, 'hotel') == hotel_name and \
                        self.r.hget('room_' + i, 'branch') == branch_name and \
                        self.r.hget('room_' + i, 'number') == room_number and \
                        self.r.hexists('room_' + i, 'guest_id'):
                    return False
            return True

    def add_guest_to_room(self,hotel_name, branch_name, room_number, guest_id):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        elif not self.r.sismember('rooms', hotel_name + '_' + branch_name + '_' + room_number):
            print('This room does not belong to this branch')
        elif not self.r.sismember('guests', hotel_name + '_' + guest_id):
            print('This guest does not belong to this hotel')
        else:
            if not self.is_room_empty(hotel_name,branch_name,room_number):
                print('This room is not empty')
            else:
                self.r.hmset('guest_' + hotel_name + '_' + guest_id,
                         {
                             'room_id': branch_name + '_' + room_number
                         })
                self.r.hmset('room_' + hotel_name + '_' + branch_name + '_' + room_number,
                         {
                             'guest_id': guest_id
                         })
                self.__add_to_hotel_booking_data(hotel_name, guest_id)

    def list_all_empty_rooms(self, hotel_name, branch_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        else:
            print('Empty rooms of ' + hotel_name + ' ' + branch_name + ':')
            for i in self.r.smembers('rooms'):
                if self.r.hget('room_' + i, 'hotel') == hotel_name and \
                        self.r.hget('room_' + i, 'branch') == branch_name and not\
                        self.r.hexists('room_' + i, 'guest_id'):
                    print(self.r.hget('room_' + i, 'number'))

    def list_all_occupied_rooms(self, hotel_name, branch_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        else:
            print('Occupied rooms of ' + hotel_name + ' ' + branch_name + ':')
            for i in self.r.smembers('rooms'):
                if self.r.hget('room_' + i, 'hotel') == hotel_name and \
                        self.r.hget('room_' + i, 'branch') == branch_name and \
                        self.r.hexists('room_' + i, 'guest_id'):
                    print(self.r.hget('room_' + i, 'number'))

    def list_all_guests(self, hotel_name, branch_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        else:
            print('Guests of ' + hotel_name + ' ' + branch_name + ':')
            for i in self.r.smembers('rooms'):
                if self.r.hget('room_' + i, 'hotel') == hotel_name and \
                        self.r.hget('room_' + i, 'branch') == branch_name and \
                        self.r.hexists('room_' + i, 'guest_id'):
                    print(self.r.hget('guest_' + hotel_name + '_' + self.r.hget('room_' + i, 'guest_id'),'first_name') + ' ' +
                          self.r.hget('guest_' + hotel_name + '_' + self.r.hget('room_' + i, 'guest_id'), 'last_name'))

    def list_all_guests_with_rooms(self, hotel_name, branch_name):
        if not self.r.sismember('hotels', hotel_name):
            print('This hotel does not exist')
        elif not self.r.sismember('branches', hotel_name + '_' + branch_name):
            print('This branch does not belong to this hotel')
        else:
            print('Guests of ' + hotel_name + ' ' + branch_name + ' with room numbers ' + ':')
            for i in self.r.smembers('rooms'):
                if self.r.hget('room_' + i, 'hotel') == hotel_name and \
                        self.r.hget('room_' + i, 'branch') == branch_name and \
                        self.r.hexists('room_' + i, 'guest_id'):
                    print(self.r.hget('guest_' + hotel_name + '_' + self.r.hget('room_' + i, 'guest_id'), 'first_name') + ' ' +
                          self.r.hget('guest_' + hotel_name + '_' + self.r.hget('room_' + i, 'guest_id'), 'last_name') + ':' +
                          self.r.hget('room_' + i, 'number'))

    def __add_to_hotel_booking_data(self, hotel_name, guest_id):
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        mapping={
                         hotel_name + '_' + guest_id: date_time
                     }
        self.r.lpush('guestBookingData', hotel_name + '_' + guest_id,date_time)
        self.r.zadd('guestLastBookingData',mapping)

    def show_hotel_booking_data(self):
        print('Last booking data of guests:')
        for i in self.r.zrange('guestLastBookingData', 0, -1, withscores=True, desc=True):
          print(i)
        print('All Booking data of guests:')
        for i in self.r.lrange('guestBookingData', 0, -1):
          print(i)
          print()