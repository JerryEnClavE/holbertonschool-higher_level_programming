import os


def generate_invitations(template, attendees):
    if type(template) is not str:
        print("Error: template not a string")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if type(attendees) is not list:
        print("Error: attendees not a list")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        title = attendee.get("event_title", "N/A")
        date = attendee.get("event_date", "N/A")
        location = attendee.get("event_location", "N/A")

        invitation = template.replace('{name}', name)
        invitation = invitation.replace('{event_title}', title)
        invitation = invitation.replace('{event_date}', date)
        invitation = invitation.replace('{event_location}', location)

        filename = f"output_{index}.txt"

        if os.path.exists(filename):
            print(f"Error: {filename} already exists.")

        try:
            with open(filename, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(e)
