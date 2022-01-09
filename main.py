import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail

from dead_cells_wiki_scraper.dead_cells_provider import DeadCellsWikiProvider
from firestore_utils import FirestoreManager

logging_client = logging.Client()
logger = logging_client.logger("dcupdater")

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'dead-cells-staging',
})
db = firestore.client()

def check_for_updates(data):
    provider = DeadCellsWikiProvider()
    firestore_manager = FirestoreManager(db, provider)
    diffs = firestore_manager.get_diffs()
    needs_update = False
    for _, removals_and_additions in diffs.items():
        if len(removals_and_additions['removals']) > 0:
            needs_update = True
        if len(removals_and_additions['additions']) > 0:
            needs_update = True

    if needs_update:
        diffs_message = create_message(diffs)
        logging.log_text('Found diffs: %s', diffs)
        send_update_email(diffs_message)
        

def create_message(diffs):
    removals = '<h3>Removals</h3>'
    additions = '<h3>Additions</h3>'
    for diff_type, removals_and_additions in diffs.items():
        removals += '<h4>{}</h4>'.format(diff_type)
        additions += '<h4>{}</h4>'.format(diff_type)
        if len(removals_and_additions['removals']) > 0:
            for removal in removals_and_additions['removals']:
                removals += str(removal)
        if len(removals_and_additions['additions']) > 0:
            for addition in removals_and_additions['additions']:
                additions += str(addition)
    link = "<br><p>If these changes look correct, please follow this <a href=\"https://us-central1-dead-cells-268800.cloudfunctions.net/update_firestore\">link</a>"
    return removals + additions + link

def send_update_email(differences):
    message = Mail(
        to_emails="dead-cells-companion-admins@googlegroups.com",
        from_email="vanhine.adam@gmail.com",
        subject=f"Dead Cells Companion Data Update",
        html_content="""
        <h1>Differences</h1>
        {}
        """.format(differences)
    )
    sg = SendGridAPIClient()
    response = sg.send(message)
    print(response.status_code)

def update_firestore(request):
    provider = DeadCellsWikiProvider()
    firestore_manager = FirestoreManager(db, provider)
    firestore_manager.write_new_data_to_firestore()
