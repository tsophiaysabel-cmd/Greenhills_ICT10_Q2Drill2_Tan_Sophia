from pyscript import display, document

from pyscript import display
from js import document

def get_name(e):
    # Clear previous output
    document.getElementById('div1').innerHTML = ''

    club_members = ['abdul jabbar darimbang', 'daphne mariano', 'juan miguel piansay']

    # Get values, lowercase them, and strip extra whitespace
    last_name = document.getElementById("lname").value.lower().strip()
    first_name = document.getElementById("fname").value.lower().strip()

    # Added a space ' ' between first and last name
    full_name = first_name + ' ' + last_name

    # Check if name is in the list
    if full_name in club_members:
        message = f"Congratulations {full_name}! You are now part of the Science club."
    else:
        message = f"Sorry, {full_name}, your name is not on the list."

    # Display the result in div1
    display(message, target='div1')