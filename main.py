from pyscript import document

CLUB_DATA = {
    "SocSci Club": {
        "Description": "A club for people who love history & philosophy.",
        "Meeting Time": "Wed 4:00 PM",
        "Location": "Room 607",
        "Advisor": "Mr. Santos",
        "Number of Members": 24,
        "Category": "Academic"
    },
    "Math Club": {
        "Description": "For students interested in Mathematics.",
        "Meeting Time": "Tues 5:00 PM",
        "Location": "Room 301",
        "Advisor": "Mr. Cruz",
        "Number of Members": 21,
        "Category": "Academic"
    },
    "Arts Club": {
        "Description": "For drawing and painting students.",
        "Meeting Time": "Wed 4:00 PM",
        "Location": "Arts Studio",
        "Advisor": "Ms. Dela Cruz",
        "Number of Members": 18,
        "Category": "Non-Academic"
    }
}

def show_club_info():

    select_element = document.getElementById("select_club_id")
    selected_club_name = select_element.value
    
    club_info = CLUB_DATA.get(selected_club_name, {})
    
    html_content = f"""
    <h4>{selected_club_name}</h4>
    <p><strong>Description:</strong> {club_info.get('Description', 'N/A')}</p>
    <p><strong>Meeting Time:</strong> {club_info.get('Meeting Time', 'N/A')}</p>
    <p><strong>Location:</strong> {club_info.get('Location', 'N/A')}</p>
    <p><strong>Advisor:</strong> {club_info.get('Advisor', 'N/A')}</p>
    <p><strong>Number of Members:</strong> {club_info.get('Number of Members', 'N/A')}</p>
    <p><strong>Category:</strong> {club_info.get('Category', 'N/A')}</p>
    """
    document.getElementById("output").innerHTML = html_content