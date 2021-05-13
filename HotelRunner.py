from HotelClass import HotelClass

rf=HotelClass()

rf.add_company('Hilton',1919)
rf.add_company('Marriott',1957)
rf.add_company('FourSeasons',1960)

rf.add_new_branch('Hilton','Rome')
rf.add_new_branch('Hilton','Baku')
rf.add_new_branch('Marriot','London')
rf.add_new_branch('FourSeasons','Madrid')

rf.list_all_branches('Hilton')

rf.add_new_rooms_to_branch('Hilton','Baku','101')
rf.add_new_rooms_to_branch('Hilton','Baku','102')
rf.add_new_rooms_to_branch('Hilton','Baku','103')
rf.add_new_rooms_to_branch('Marriott','London','201')
rf.add_new_rooms_to_branch('Marriott','London','202')
rf.add_new_rooms_to_branch('FourSeasons','Madrid','301')
rf.add_new_rooms_to_branch('FourSeasons','Madrid','302')

rf.list_branch_rooms('Hilton','Baku')
