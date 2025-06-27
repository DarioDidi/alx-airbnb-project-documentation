# User Stories
### 1. User Registration:
   As a new user,
   I want to register an account (as a guest or host),
   so that I can book properties or list my own.

   Acceptance Criteria:

   Email, password, and role selection are required.
   
   Password must meet security standards (8+ chars, special characters).
   
   Confirmation email is sent upon registration.

### 2. Property Listing Creation:
   As a host,
   I want to add a new property listing with details (title, price, amenities),
   so that guests can discover and book my property  
    Acceptance Criteria:
     Mandatory fields: Title, location, price, availability dates.\
    Option to upload photos and specify amenities (Wi-Fi, pool, etc.).\
    Listing appears in search results after submission.

### 3. Property Search & Booking:
   As a guest,
   I want to search for properties by location, price, and amenities,
   so that I can find and book a suitable rental.
   
   Acceptance Criteria:
   
   Filters for location, price range, and amenities work accurately.
   
   Calendar shows real-time availability to prevent double bookings.
   
   Booking requires payment confirmation.

### 4. Payment Processing
   As a guest,
   I want to securely pay for my booking via Stripe/PayPal,
   so that my reservation is confirmed instantly.
   
   Acceptance Criteria:
   
   Supports credit/debit cards and digital wallets.
   
   Payment success triggers a confirmation email.
   
   Host receives payout after checkout (minus platform fees).

### 5. Reviews and Ratings
  As a guest,
   I want to be able to post reviews on my bookings,
  and that my review is reflected instantly.


