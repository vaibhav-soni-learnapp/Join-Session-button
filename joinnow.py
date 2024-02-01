import streamlit as st


    

# Set the page title and icon
st.set_page_config(page_title="Admin Instructions", page_icon=":memo:")

# Instructional text and GIF in the sidebar
st.sidebar.title("Steps to Update Program")
st.sidebar.write("""
1. Go to the admin portal.
2. Select the programme.
3. Go to the cohort section.
4. Scroll to the right and click on "Update Programme".
5. Copy the Browser URL.
""")

# Assuming the GIF is named "update_program.gif" and is located in the same directory as your Streamlit app
# If your GIF is hosted online, replace the file path with the URL
gif_path = "update_program.gif"

# Display the GIF in the sidebar
st.sidebar.image(gif_path, caption="Follow these steps", use_column_width=True)

# Main page content (optional)
#st.title("Admin Portal Instructions")
st.write("Please follow the instructions in the sidebar to update the program.")



def convert_admin_to_user_url(admin_url, environment):

# Define base URLs for each environment
    user_base_urls = {
        'dev': "https://varsity-live.dev.varsitylive.in",
        'stage': "https://varsity-live.stage.varsitylive.in",
        'prod': "https://varsitylive.zerodha.com"
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
