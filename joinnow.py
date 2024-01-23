import streamlit as st
def convert_admin_to_user_url(admin_url):
    # Mapping of admin URLs to user URLs
    url_mapping = {
        'dev': ("https://varsity-live-admin.dev.varsitylive.in", "https://varsity-live.dev.varsitylive.in"),
        'stage': ("https://varsity-live-admin.stage.varsitylive.in", "https://varsity-live.stage.varsitylive.in"),
        'prod': ("https://backoffice.varsitylive.in", "https://varsitylive.in")
    }

    # Detecting environment and setting base URL
    environment = 'prod'  # Default to production
    for env, urls in url_mapping.items():
        if urls[0] in admin_url:
            environment = env
            break
    user_base_url = url_mapping[environment][1]

    # Extracting IDs
    parts = admin_url.split('/')
    programmeId = parts[-3]
    cohortId = parts[-1]

    # Constructing new user URL
    new_url = f"{user_base_url}/practice?programmeId={programmeId}&cohortId={cohortId}"
    return new_url

# Example Usage
admin_url = "https://varsity-live-admin.dev.varsitylive.in/programmes/7ec32d73-5730-4566-9a73-06a2a008408c/cohorts/41d52a38-3f6c-44fd-9085-e391ed5b42f1"
user_url = convert_admin_to_user_url(admin_url)
print(user_url)
