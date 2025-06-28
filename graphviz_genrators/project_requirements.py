from graphviz import Digraph, Graph

#overarching graph
#overarch = Digraph(comment='Overstructure', format='png')
overarch = Graph(name='Overstructure')

# Create a new directed graph
#dot = Digraph(comment='Airbnb Clone Backend Architecture', format='png')
dot = Graph(name='Airbnb Clone Backend Architecture')

#overarch.attr('node', shape='box')
dot.attr(rankdir='LR', size='10')
dot.attr('node', shape='box')

# Define main feature clusters







dot.node('Admin', '''8. Admin Dashboard
- Manage users, listings, bookings, payments''')

dot.node('Notify', '''
7. Notifications System
- Email & in-app alerts for:
  • Booking, cancellation, payment updates''')

dot.node('Reviews', '''6. Reviews and Ratings
- Guest reviews & ratings
- Host responses
- Review-booking linkage for authenticity''')

dot.node('Payment', '''5. Payment Integration
- Secure payments (Stripe, PayPal)
- Guest payments & host payouts
- Multi-currency support''')

dot.node('Booking', '''4. Booking Management
- Booking Creation:
  • Date validation to prevent double bookings
- Booking Cancellation:
  • Based on cancellation policy
- Booking Status:
  • Pending, confirmed, canceled, completed''')

dot.node('Search', '''3. Search and Filtering
- Search by:
  • Location, price, guests, amenities
- Support pagination''')

dot.node('Property', '''2. Property Listings Management
- Add Listings:
  • Title, description, location, price, amenities, availability
- Edit/Delete Listings
''')

dot.node('User', '''1. User Management
         - User Registration:
            • Guests or Hosts sign-up
            • Secure authentication (JWT)
        - Login & Authentication:
            • Email/password login
            • OAuth (Google, Facebook)
        - Profile Management:
            • Update photo, contact info, preferences
         ''')

"""dot.node('Database', '''1. Database Management

    Use a relational database such as PostgreSQL or MySQL.
    Required tables:
        Users (guests and hosts)
        Properties
        Bookings
        Reviews
        Payments''')

dot.node('API', )"""
#overarch.subgraph(dot)
# Render the graph to a PNG file
#overarch.render('Airbnb_Backend_requirements', format='png', cleanup=True)
dot.render('Airbnb_Backend_requirements', format='png', cleanup=True)
