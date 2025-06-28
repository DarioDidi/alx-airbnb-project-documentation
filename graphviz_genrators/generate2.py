from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Airbnb Clone Backend Architecture', format='png')
dot.attr(rankdir='LR', size='10')
dot.attr('node', shape='box')

# Define main feature clusters
#dot.node('User', 'User Management')
dot.node('User', 'Users')
dot.node('Property', 'Property Listings\nManagement')
dot.node('Search', 'Search and Filtering')
dot.node('Booking', 'Booking Management')
dot.node('Payment', 'Payment Integration')
dot.node('Reviews', 'Reviews and Ratings')
dot.node('Notify', 'Notifications System')
dot.node('Admin', 'Admin Dashboard')

# Define sub-features and link them
# User Management
dot.node('Reg', 'User Registration')
dot.node('Auth', 'Login & Authentication')
dot.node('Profile', 'Profile Management')
dot.edges([('User', 'Reg'), ('User', 'Auth'), ('User', 'Profile'), ('User', 'Search')])

# Property Listings Management
dot.node('AddList', 'Add Listings')
dot.node('EditList', 'Edit/Delete Listings')
dot.edges([('Property', 'AddList'), ('Property', 'EditList')])

# Search and Filtering
dot.node('ByLocation', 'By Location')
dot.node('ByPrice', 'By Price')
dot.node('ByGuests', 'By Guests')
dot.node('ByAmenities', 'By Amenities')
dot.node('Pagination', 'Pagination')
dot.edges([('Search', 'ByLocation'), ('Search', 'ByPrice'), ('Search', 'ByGuests'), 
           ('Search', 'ByAmenities'), ('Search', 'Pagination')])

# Booking Management
dot.node('BookCreate', 'Booking Creation')
dot.node('BookCancel', 'Booking Cancellation')
dot.node('BookStatus', 'Booking Status')
dot.edges([('Booking', 'BookCreate'), ('Booking', 'BookCancel'), ('Booking', 'BookStatus')])

# Payment Integration
dot.node('SecurePay', 'Secure Payments')
dot.node('Payouts', 'Host Payouts')
dot.node('MultiCurrency', 'Multi-Currency Support')
dot.edges([('Payment', 'SecurePay'), ('Payment', 'Payouts'), ('Payment', 'MultiCurrency')])

# Reviews and Ratings
dot.node('GuestReviews', 'Guest Reviews')
dot.node('HostReplies', 'Host Replies')
dot.node('LinkBooking', 'Review-Booking Link')
dot.edges([('Reviews', 'GuestReviews'), ('Reviews', 'HostReplies'), ('Reviews', 'LinkBooking')])

# Notifications
dot.node('EmailNotif', 'Email Notifications')
dot.node('AppNotif', 'In-App Notifications')
dot.edges([('Notify', 'EmailNotif'), ('Notify', 'AppNotif')])

# Admin Dashboard
dot.node('ManageUsers', 'Manage Users')
dot.node('ManageListings', 'Manage Listings')
dot.node('ManageBookings', 'Manage Bookings')
dot.node('ManagePayments', 'Manage Payments')
dot.edges([('Admin', 'ManageUsers'), ('Admin', 'ManageListings'), ('Admin', 'ManageBookings'), ('Admin', 'ManagePayments')])

# Connect high-level systems
dot.edges([
    ('User', 'Property'), 
    ('User', 'Booking'), 
    ('User', 'Reviews'), 
    ('Booking', 'Payment'),
    ('Booking', 'Notify'),
    ('Payment', 'Admin'),
    ('User', 'Admin')
])

# Render the graph to a PNG file
dot.render('Airbnb_Backend_Graph', format='png', cleanup=True)
