from HotelClass import HotelClass

rf=HotelClass()

rf.add_company('Hilton',1919)
rf.add_company('Marriott',1957)
rf.add_company('FourSeasons',1960)

rf.add_new_branch('Hilton','Rome')
rf.add_new_branch('Hilton','Baku')
rf.add_new_branch('Marriott','London')
rf.add_new_branch('FourSeasons','Madrid')

rf.list_all_branches('Hilton')
rf.list_all_branches('Marriott')
rf.list_all_branches('FourSeasons')

rf.add_new_room_to_branch('Hilton','Baku','101')
rf.add_new_room_to_branch('Hilton','Baku','102')
rf.add_new_room_to_branch('Hilton','Baku','103')
rf.add_new_room_to_branch('Hilton','Rome','104')
rf.add_new_room_to_branch('Hilton','Rome','105')
rf.add_new_room_to_branch('Marriott','London','201')
rf.add_new_room_to_branch('Marriott','London','202')
rf.add_new_room_to_branch('FourSeasons','Madrid','301')
rf.add_new_room_to_branch('FourSeasons','Madrid','302')

rf.list_branch_rooms('Hilton','Baku')
rf.list_branch_rooms('Hilton','Rome')
rf.list_branch_rooms('Marriott','London')
rf.list_branch_rooms('FourSeasons','Madrid')

rf.add_new_guest('H100','John','Doe','Hilton')
rf.add_new_guest('H101','Kate','Wilson','Hilton')
rf.add_new_guest('H102','Anna','Jolie','Hilton')
rf.add_new_guest('M100','Martin','Green','Marriott')
rf.add_new_guest('F100','Rose','Smith','FourSeasons')

rf.add_guest_to_room('Hilton','Baku','101','H100')
rf.add_guest_to_room('Hilton','Baku','102','H101')
rf.add_guest_to_room('Hilton','Rome','104','H102')
rf.add_guest_to_room('Marriott','London','201','M100')
rf.add_guest_to_room('FourSeasons','Madrid','301','F100')

rf.list_all_empty_rooms('Hilton','Baku')
rf.list_all_empty_rooms('Hilton','Rome')
rf.list_all_empty_rooms('Marriott','London')
rf.list_all_empty_rooms('FourSeasons','Madrid')

rf.list_all_occupied_rooms('Hilton','Baku')
rf.list_all_occupied_rooms('Hilton','Rome')
rf.list_all_occupied_rooms('Marriott','London')
rf.list_all_occupied_rooms('FourSeasons','Madrid')

rf.list_all_guests('Hilton','Baku')
rf.list_all_guests('Hilton','Rome')
rf.list_all_guests('Marriott','London')
rf.list_all_guests('FourSeasons','Madrid')

rf.list_all_guests_with_rooms('Hilton','Baku')
rf.list_all_guests_with_rooms('Hilton','Rome')
rf.list_all_guests_with_rooms('Marriott','London')
rf.list_all_guests_with_rooms('FourSeasons','Madrid')

rf.show_hotel_booking_data()