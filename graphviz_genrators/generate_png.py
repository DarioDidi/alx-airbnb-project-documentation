from PIL import Image, ImageDraw, ImageFont
import textwrap

# Define the backend features in a structured format
backend_features = """
Airbnb Clone - Backend Functionalities Overview

1. User Management
- User Registration:
  • Guests or Hosts sign-up
  • Secure authentication (JWT)
- Login & Authentication:
  • Email/password login
  • OAuth (Google, Facebook)
- Profile Management:
  • Update photo, contact info, preferences

2. Property Listings Management
- Add Listings:
  • Title, description, location, price, amenities, availability
- Edit/Delete Listings

3. Search and Filtering
- Search by:
  • Location, price, guests, amenities
- Support pagination

4. Booking Management
- Booking Creation:
  • Date validation to prevent double bookings
- Booking Cancellation:
  • Based on cancellation policy
- Booking Status:
  • Pending, confirmed, canceled, completed

5. Payment Integration
- Secure payments (Stripe, PayPal)
- Guest payments & host payouts
- Multi-currency support

6. Reviews and Ratings
- Guest reviews & ratings
- Host responses
- Review-booking linkage for authenticity

7. Notifications System
- Email & in-app alerts for:
  • Booking, cancellation, payment updates

8. Admin Dashboard
- Manage users, listings, bookings, payments
"""

# Image settings
width, height = 1200, 1800
background_color = "white"
text_color = "black"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust if necessary
font_size = 24

# Create the image canvas
image = Image.new("RGB", (width, height), color=background_color)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, font_size)

# Word wrap the text and draw it on the image
margin = 50
offset = 50
for line in backend_features.strip().split('\n'):
    wrapped_text = textwrap.wrap(line, width=90)
    for wrapped_line in wrapped_text:
        draw.text((margin, offset), wrapped_line, font=font, fill=text_color)
        #offset += font.getsize(wrapped_line)[1] + 10
        offset += font.getbbox(wrapped_line)[1] + 10

# Save the image
image.save("Airbnb_Backend_Features.png")
