import csv

def write_to_csv(all_security_incidents):
    """
    Writes security incident data to a CSV file named 'security_incidents.csv'.
    This function takes a list of security incidents and writes their details to a CSV file.
    Each incident can have multiple notes, and each note is written as a separate row in the CSV.
    If an incident has no notes, a single row is written for the incident with empty note fields.
    Args:
        all_security_incidents (list): A list of dictionaries, where each dictionary represents a security incident.
            Each incident dictionary may contain the following keys:
                - 'request': A dictionary containing incident details such as 'id', 'subject', 'description', 'created_time', 'status', 'priority', 'group', and 'technician'.
                - 'all_notes': A list of dictionaries, where each dictionary represents a note associated with the incident.
    """

    with open('exports/security_incidents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Incident ID", "Subject", "Description", "Created Time", "Status", "Priority", "Group", "Technician", "Note ID", "Note Description"])
        for incident in all_security_incidents:
            if incident is not None:
                incident_request = incident.get('request', {})
                status_name = incident_request.get('status', {}).get('name', '') if incident_request.get('status') else ''
                priority_name = incident_request.get('priority', {}).get('name', '') if incident_request.get('priority') else ''
                group_name = incident_request.get('group', {}).get('name', '') if incident_request.get('group') else ''
                technician_email = incident_request.get('technician', {}).get('email_id', '') if incident_request.get('technician') else ''
                
                if incident.get('all_notes'):
                    for note in incident['all_notes']:
                        writer.writerow([
                            incident_request.get('id', ''),
                            incident_request.get('subject', ''),
                            incident_request.get('description', ''),
                            incident_request.get('created_time', ''),
                            status_name,
                            priority_name,
                            group_name,
                            technician_email,
                            note.get('request_note', {}).get('id', ''),
                            note.get('request_note', {}).get('description', '')
                        ])
                else:
                    writer.writerow([
                        incident_request.get('id', ''),
                        incident_request.get('subject', ''),
                        incident_request.get('description', ''),
                        incident_request.get('created_time', ''),
                        status_name,
                        priority_name,
                        group_name,
                        technician_email,
                        "",
                        ""
                    ])