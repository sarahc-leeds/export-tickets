# ManageEngine API Script

This script interacts with the ManageEngine ServiceDesk Plus API to retrieve and process security incident data. It fetches all incidents, filters them for security incidents, retrieves detailed information and notes for each incident, and then exports the data to a JSON file and a CSV file.

## Features

- Fetch all incidents from ManageEngine ServiceDesk Plus API.
- Filter incidents to retrieve only security-related incidents.
- Retrieve detailed information and notes for each security incident.
- Export the security incidents and their notes to a JSON file.
- Export the security incidents and their notes to a CSV file.

## Prerequisites

- Python 3.x
- ManageEngine ServiceDesk Plus account with API access.

## Setup

1. Clone the repository

2. Install the required dependencies using pip:

   ```sh
   pip install requests
   ```

3. Update the `.example.env` file with your own values

4. Ensure you have the following files in the same directory as `main.py`:
   - `utils.py` (containing the `handle_request_errors` function)
   - `auth.py` (containing the `get_access_token` function)
   - `csv_export.py` (containing the `write_to_csv` function)

## Configuration

- Update the `request_url` variable in `main.py` to match your ManageEngine ServiceDesk Plus API endpoint if different.

## Usage

1. Run the script:

   ```sh
   python main.py
   ```

2. The script will generate two output files:
   - `security_incidents.json`: Contains all security incidents and their notes in JSON format.
   - `security_incidents.csv`: Contains all security incidents and their notes in CSV format.

## Functions

- `get_all_incidents(token)`: Fetches all incidents from the API.
- `filter_for_security_incidents(token)`: Filters incidents to retrieve only security-related incidents.
- `get_security_incident_details(token, incident_id)`: Retrieves detailed information for a specific security incident.
- `get_security_incident_notes(token, incident_id, note_id)`: Retrieves notes for a specific security incident.
- `get_all_requests_and_notes(token)`: Retrieves all security incidents and their notes.
- `main()`: Main function to execute the script.

## Notes

- Ensure your API token is valid and has the necessary permissions to access the ManageEngine ServiceDesk Plus API (Scope should be `SDPOnDemand.requests.ALL`)
- Handle API rate limits and errors appropriately as per your requirements.

## License

This project is licensed under the MIT License.
