import graphviz

# Create a new ERD diagram
erd = graphviz.Digraph('ERD', filename='ERD_Diagram', format='png')
erd.attr('node', shape='box')

erd.node('Title', 'ALX Airbnb Database')
# User Entity
erd.node('User', '''User
------------------------
user_id (PK, UUID, Indexed)
first_name (VARCHAR, NOT NULL)
last_name (VARCHAR, NOT NULL)
email (VARCHAR, UNIQUE, NOT NULL)
password_hash (VARCHAR, NOT NULL)
phone_number (VARCHAR, NULL)
role (ENUM, NOT NULL)
created_at (TIMESTAMP, DEFAULT)''')

# Property Entity
erd.node('Property', '''Property
------------------------
property_id (PK, UUID, Indexed)
host_id (FK -> User.user_id)
name (VARCHAR, NOT NULL)
description (TEXT, NOT NULL)
location (VARCHAR, NOT NULL)
pricepernight (DECIMAL, NOT NULL)
created_at (TIMESTAMP, DEFAULT)
updated_at (TIMESTAMP, ON UPDATE)''')

# Booking Entity
erd.node('Booking', '''Booking
------------------------
booking_id (PK, UUID, Indexed)
property_id (FK -> Property.property_id)
user_id (FK -> User.user_id)
start_date (DATE, NOT NULL)
end_date (DATE, NOT NULL)
total_price (DECIMAL, NOT NULL)
status (ENUM, NOT NULL)
created_at (TIMESTAMP, DEFAULT)''')

# Payment Entity
erd.node('Payment', '''Payment
------------------------
payment_id (PK, UUID, Indexed)
booking_id (FK -> Booking.booking_id)
amount (DECIMAL, NOT NULL)
payment_date (TIMESTAMP, DEFAULT)
payment_method (ENUM, NOT NULL)''')

# Review Entity
erd.node('Review', '''Review
------------------------
review_id (PK, UUID, Indexed)
property_id (FK -> Property.property_id)
user_id (FK -> User.user_id)
rating (INTEGER, 1-5, NOT NULL)
comment (TEXT, NOT NULL)
created_at (TIMESTAMP, DEFAULT)''')

# Message Entity
erd.node('Message', '''Message
------------------------
message_id (PK, UUID, Indexed)
sender_id (FK -> User.user_id)
recipient_id (FK -> User.user_id)
message_body (TEXT, NOT NULL)
sent_at (TIMESTAMP, DEFAULT)''')

# Relationships
erd.edge('Property', 'User', label='host_id')
erd.edge('Booking', 'Property', label='property_id')
erd.edge('Booking', 'User', label='user_id')
erd.edge('Payment', 'Booking', label='booking_id')
erd.edge('Review', 'Property', label='property_id')
erd.edge('Review', 'User', label='user_id')
erd.edge('Message', 'User', label='sender_id')
erd.edge('Message', 'User', label='recipient_id')

erd.render(view=True)