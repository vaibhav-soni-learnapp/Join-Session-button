import streamlit as st

def convert_admin_to_user_url(admin_url, environment):
    # Define base URLs for each environment
    user_base_urls = {
        'dev': "https://varsity-live.dev.varsitylive.in",
        'stage': "https://varsity-live.stage.varsitylive.in",
        'prod': "https://varsitylive.in"
    }

    # Extracting IDs
    parts = admin_url.split('/')
    programmeId = parts[-3]
    cohortId = parts[-1]

    # Constructing new user URL
    user_base_url = user_base_urls.get(environment, user_base_urls['prod'])  # Default to 'prod'
    new_url = f"{user_base_url}/practice?programmeId={programmeId}&cohortId={cohortId}"
    return new_url

# Streamlit UI
def main():
    st.title("Join Session - Varsity Live")

    # User input for URL
    admin_url = st.text_input("Enter the Admin URL:", "")

    # Dropdown for environment selection
    environment = st.selectbox("Select Environment:", ('dev', 'stage', 'prod'))

    # Button to convert URL
    if st.button("Join Session"):
        if admin_url:
            user_url = convert_admin_to_user_url(admin_url, environment)
            st.success(f"Join Session: {user_url}")
        else:
            st.error("Please enter a valid Admin URL.")

if __name__ == "__main__":
    main()
