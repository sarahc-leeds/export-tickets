import requests
import csv
import json
from app.utils import handle_request_errors
from auth import get_access_token
from csv_export import write_to_csv

request_url = 'https://sdpondemand.manageengine.eu/api/v3/requests'

def get_all_incidents(token):
    headers = {
        "Authorization": "Bearer " + token['access_token'],
        "Accept": "application/vnd.manageengine.sdp.v3+json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    all_requests = []
    page = 1
    row_count = 200

    while True:
        list_info = {
            "list_info": {
                "row_count": row_count,
                "page": page,
                "sort_field": "created_time",
                "sort_order": "desc"
            }
        }
        params = {"input_data": json.dumps(list_info)}
        try:
            resp = requests.get(request_url, headers=headers, params=params, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            requests_list = data.get('requests', [])
            if not requests_list:
                break
            all_requests.extend(requests_list)
            page += 1
        except Exception as e:
            handle_request_errors(e, request_url)
            break

    return all_requests

def filter_for_security_incidents(token):
    incidents = get_all_incidents(token)
    security_incidents = []
    for incident in incidents:
        if incident['group']['name'] == 'Incident':
            security_incidents.append(incident['id'])

    return security_incidents


def get_security_incident_details(token, incident_id):
    headers = {
        "Authorization": "Bearer " + token['access_token'],
        "Accept": "application/vnd.manageengine.sdp.v3+json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    incident_url = request_url + '/' + str(incident_id)
    try:
        resp = requests.get(incident_url, headers=headers)
        resp.raise_for_status()
        incident_details = resp.json()
    except Exception as e:
        handle_request_errors(e, incident_url)

    return incident_details


def get_security_incident_notes(token, incident_id, note_id):
    headers = {
        "Authorization": "Bearer " + token['access_token'],
        "Accept": "application/vnd.manageengine.sdp.v3+json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    notes_url = request_url + '/' + str(incident_id) + '/notes/' + str(note_id)
    print(notes_url)
    try:
        resp = requests.get(notes_url, headers=headers)
        resp.raise_for_status()
        note = resp.json()
    except Exception as e:
        handle_request_errors(e, notes_url)

    print(f'The note is {note}')

    return note


def get_all_requests_and_notes(token):
    security_incidents = filter_for_security_incidents(token)
    requests_and_notes = []
    for incident_id in security_incidents:
        incident = get_security_incident_details(token, incident_id)
        notes = []
        if incident['request']['has_notes']:
            # Make request to /api/v3/requests/{incident_id}/notes/ to get Ids of all notes
            notes_response = requests.get(request_url + '/' + str(incident_id) + '/notes/', headers={"Authorization": "Bearer " + token['access_token']}).json()
            notes_list = notes_response.get('notes', [])
            notes_ids = [note['id'] for note in notes_list]
            print(f"Note IDs: {notes_ids}")
            for note_id in notes_ids:
                note = get_security_incident_notes(token, incident_id, note_id)
                notes.append(note)
        incident['all_notes'] = notes
        requests_and_notes.append(incident)

    return requests_and_notes


def main():
    token = get_access_token()
    all_security_incidents = get_all_requests_and_notes(token)

    # output all the security incidents and their notes into a json file
    with open('exports/security_incidents.json', 'w') as f:
        json.dump(all_security_incidents, f, indent=4)

    write_to_csv(all_security_incidents)


if __name__ == "__main__":  
    main()