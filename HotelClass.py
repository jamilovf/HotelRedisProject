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
        print('Branches of ' + hotel_name + ':')
        for i in self.r.smembers('branches'):
            if self.r.hget('branch_' + i, 'hotel') == hotel_name:
                print(self.r.hget('branch_' + i, 'title'))

    def add_new_rooms_to_branch(self, hotel_name, branch_name, room_number):
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
        print('Rooms of ' + hotel_name + ' ' + branch_name + ':')
        for i in self.r.smembers('rooms'):
            if self.r.hget('room_' + i, 'hotel') == hotel_name and self.r.hget('room_' + i, 'branch') == branch_name :
                print(self.r.hget('room_' + i, 'number'))