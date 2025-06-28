from graphviz import Digraph

# Create diagram
uc = Digraph('Airbnb_Detailed_Use_Cases', format='png')
uc.attr(rankdir='TB', label='Airbnb Clone: Detailed Use Case Diagram', 
        labelloc='t', fontsize='16', splines='ortho')

# Styling
uc.attr('node', shape='ellipse', style='filled', 
        fillcolor='lightblue', fontname='Arial')
uc.attr('edge', fontname='Arial', fontsize='10', 
        arrowhead='vee', arrowsize='0.5')

# ===== ACTORS =====
uc.node('Guest', shape='box3d', fillcolor='#FFA07A')  # Light salmon
uc.node('Host', shape='box3d', fillcolor='#20B2AA')   # Light sea green
uc.node('PaymentSystem', 'Payment System', shape='cylinder', fillcolor='#D3D3D3')

# ===== USE CASES =====
# Authentication
uc.node('UC1', 'Register Account\n(Email/Password or OAuth)')
uc.node('UC2', 'Login\n(Email + Password)')
uc.node('UC3', 'Manage Profile\n(Update photo, bio, etc.)')

# Property
uc.node('UC4', 'Create Listing\n(Add property details)')
uc.node('UC5', 'Edit Listing\n(Update availability/price)')
uc.node('UC6', 'Search Listings\n(Filter by location/amenities)')

# Booking
uc.node('UC7', 'Book Property\n(Select dates + pay)')
uc.node('UC8', 'Cancel Booking\n(With refund policy)')
uc.node('UC9', 'Process Payment\n(Stripe/PayPal integration)')

# Reviews
uc.node('UC10', 'Leave Review\n(Rate property + comments)')
uc.node('UC11', 'Respond to Review\n(Host reply)')

# ===== EDGES (with action verbs) =====
# Guest actions
uc.edge('Guest', 'UC1', label='signs up using')
uc.edge('Guest', 'UC2', label='authenticates via')
uc.edge('Guest', 'UC3', label='updates')
uc.edge('Guest', 'UC6', label='searches for')
uc.edge('Guest', 'UC7', label='reserves by')
uc.edge('Guest', 'UC8', label='requests to')
uc.edge('Guest', 'UC10', label='submits')

# Host actions
uc.edge('Host', 'UC4', label='publishes new')
uc.edge('Host', 'UC5', label='modifies existing')
uc.edge('Host', 'UC11', label='writes')

# System flows
uc.edge('UC7', 'UC9', label='triggers')
uc.edge('UC8', 'UC9', label='reverses via', style='dashed')
uc.edge('UC9', 'PaymentSystem', label='connects to')

# Dependencies
uc.edge('UC10', 'UC7', label='requires completed', style='dotted')
uc.edge('UC11', 'UC10', label='responds to', style='dotted')

# ===== GROUPING =====
with uc.subgraph(name='cluster_auth') as auth:
    auth.attr(label='Authentication', style='rounded,filled', 
              fillcolor='#F0F8FF', color='gray')
    auth.node('UC1')
    auth.node('UC2') 
    auth.node('UC3')

with uc.subgraph(name='cluster_property') as prop:
    prop.attr(label='Property Management', style='rounded,filled', 
              fillcolor='#E6E6FA', color='gray')
    prop.node('UC4')
    prop.node('UC5') 
    prop.node('UC6')

with uc.subgraph(name='cluster_booking') as book:
    book.attr(label='Booking System', style='rounded,filled', 
              fillcolor='#F5FFFA', color='gray')
    book.node('UC7')
    book.node('UC8')
    book.node('UC9')
with uc.subgraph(name='cluster_reviews') as rev:
    rev.attr(label='Reviews', style='rounded,filled', 
             fillcolor='#FFF0F5', color='gray')
    rev.node('UC10')
    rev.node( 'UC11')
# ===== OUTPUT =====
uc.render('airbnb_detailed_use_cases', view=True, cleanup=True)