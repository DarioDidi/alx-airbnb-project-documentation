# Requirement Specifications 
## 1. User Authentication
Description: Secure user registration, login, and profile management.

API Endpoints
   
    Method	 Endpoint	        Description
    - POST	/api/auth/register	Register a new user (guest/host).
    - POST	/api/auth/login	    Log in a user (email + password).
    - POST	/api/auth/oauth	    Log in via OAuth (Google/Facebook).
    - GET	/api/auth/me	    Fetch current user profile.
    - PUT	/api/auth/me	    Update user profile.
 
   Input/Output Specifications
   - Register (POST /api/auth/register)
   - Request Body:
```
json
{
"name": "John Doe",
 "email": "john@example.com",
"password": "SecurePass123!",
"role": "guest" // or "host"
}
```

```
Response (Success - 201 Created):
json
{
  "token": "JWT_TOKEN",
  "user": {
    "id": "123",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "guest"
  }
}
```
Login (POST /api/auth/login)
Request Body:

```
json
{
  "email": "john@example.com",
  "password": "SecurePass123!"
}

Response (Success - 200 OK):
json
{
  "token": "JWT_TOKEN",
  "user": {
    "id": "123",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "guest"
  }
}
```
Validation Rules
Email: Must be valid format (user@domain.com).

Password: Minimum 8 chars, at least 1 uppercase, 1 number, 1 special char.

Role: Must be either guest or host.

Performance Criteria
Response Time: < 500ms for login/register.

Security:

Password hashed using bcrypt.

JWT expiry: 24 hours.

Rate limiting: 5 requests/min for /login to prevent brute force.

## 2. Property Listings Management
Description: Hosts can create, update, and delete property listings.

API Endpoints
```
Method	Endpoint	Description
POST	/api/listings	Create a new listing.
PUT	/api/listings/:id	Update a listing.
DELETE	/api/listings/:id	Delete a listing.
GET	/api/listings	Fetch all listings (with filters).
GET	/api/listings/:id	Fetch a single listing.
```
Input/Output Specifications
Create Listing (POST /api/listings)
Request Body:

```
json
{
  "title": "Beachfront Villa",
  "description": "Luxury villa with ocean view.",
  "location": "Miami, FL",
  "price": 250,
  "guests": 6,
  "amenities": ["wifi", "pool", "parking"],
  "availability": ["2024-07-01", "2024-07-30"]
}
```
Response (Success - 201 Created):
```
json
{
  "id": "listing_123",
  "title": "Beachfront Villa",
  "hostId": "user_123",
  "status": "active"
}
```
Validation Rules
Title: Min 10 chars, max 100 chars.

Price: Must be numeric > 0.

Availability Dates: Must be valid and not in the past.

Performance Criteria
Response Time: < 1s for listing retrieval (with pagination).

Scalability: Support 10,000+ listings with efficient filtering.

## 3. Booking System
Description: Guests can book properties, manage reservations, and cancel bookings.

API Endpoints:
```
Method	Endpoint	Description
POST	/api/bookings	Create a new booking.
GET	/api/bookings/:id	Fetch booking details.
DELETE	/api/bookings/:id	Cancel a booking.
```
Input/Output Specifications
Create Booking (POST /api/bookings)

Request Body:
```
json
{
  "listingId": "listing_123",
  "checkIn": "2024-07-10",
  "checkOut": "2024-07-15",
  "guests": 2,
  "paymentMethod": "stripe"
}
```
Response (Success - 201 Created):
```
json
{
  "id": "booking_456",
  "status": "confirmed",
  "totalPrice": 1250,
  "paymentStatus": "completed"
}
```
Validation Rules
Date Conflict: Prevent overlapping bookings.

Minimum Stay: At least 1 night.

Guests: Must not exceed listing capacity.

Performance Criteria
Concurrency: Handle 100+ concurrent bookings with atomic transactions.

Data Integrity: Ensure no double bookings via database locks.
