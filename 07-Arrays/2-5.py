# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   sum = 0
   for row in cinema_seats:
      sum += len(row)
   return sum

def seats_available(seats):
   a = 0
   for row in cinema_seats:
      for seat in row:
         if seat == 'A':
            a += 1
   return a

def seats_booked(seats):
   b = 0
   for row in cinema_seats:
      for seat in row:
         if seat == 'B':
            b += 1
   return b

def seat_status(seats, row, place):
   status = 'Available'
   if seats[row - 1][place - 1] == 'B':
      status = 'Booked'
   return status

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))