from graphviz import Digraph

# Create a new directed graph
uc_diagram = Digraph('AirbnbUseCaseDiagram', format='png')
uc_diagram.attr(rankdir='TB', label='Airbnb Clone Use Case Diagram', labelloc='t', fontsize='16')

# Define nodes and edges styling
uc_diagram.attr('node', shape='ellipse', style='filled', color='lightblue', fontname='Arial')
uc_diagram.attr('edge', fontname='Arial', arrowhead='vee')

# Add Actors (with different shapes/colors)
uc_diagram.node('Guest', shape='box3d', fillcolor='orange')
uc_diagram.node('Host', shape='box3d', fillcolor='orange')
uc_diagram.node('PaymentGateway', 'Payment Gateway', shape='box', fillcolor='lightgrey')

# Add Use Cases
use_cases = [
    'Register Account',
    'Login',
    'Manage Profile',
    'Search Listings',
    'Book Property',
    'Cancel Booking',
    'Process Payment',
    'Add Listing',
    'Edit Listing'
]
for uc in use_cases:
    uc_diagram.node(uc)

# Guest Interactions
uc_diagram.edge('Guest', 'Register Account')
uc_diagram.edge('Guest', 'Login')
uc_diagram.edge('Guest', 'Manage Profile')
uc_diagram.edge('Guest', 'Search Listings')
uc_diagram.edge('Guest', 'Book Property')
uc_diagram.edge('Guest', 'Cancel Booking')

# Host Interactions
uc_diagram.edge('Host', 'Add Listing')
uc_diagram.edge('Host', 'Edit Listing')
uc_diagram.edge('Host', 'Manage Profile')

# System/External Interactions
uc_diagram.edge('Book Property', 'Process Payment', label='<<include>>')
uc_diagram.edge('Process Payment', 'Payment Gateway')
uc_diagram.edge('Cancel Booking', 'Process Payment', label='<<extend>>')

# Group Use Cases into Subgraphs (Packages)
with uc_diagram.subgraph(name='cluster_auth') as auth:
    auth.attr(label='Authentication', style='rounded', color='lightgray')
    auth.node('Register Account')
    auth.node('Login')
    auth.node('Manage Profile')

with uc_diagram.subgraph(name='cluster_property') as prop:
    prop.attr(label='Property Management', style='rounded', color='lightgray')
    prop.node('Add Listing')
    prop.node('Edit Listing')
    prop.node('Search Listings')

with uc_diagram.subgraph(name='cluster_booking') as booking:
    booking.attr(label='Booking System', style='rounded', color='lightgray')
    booking.node('Book Property')
    booking.node('Cancel Booking')
    booking.node('Process Payment')

# Render and save the diagram
uc_diagram.render('airbnb_use_case_diagram', view=True)