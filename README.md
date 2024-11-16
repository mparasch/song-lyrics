# **Lyrics Finder Application**

A Python-based GUI application built with **Tkinter** that allows users to search for song lyrics by artist and song name. It integrates with APIs to fetch song information and lyrics.

---

## **Features**
- **Artist Search:** Allows users to search for songs by an artist.
- **Song Dropdown:** Dynamically populates a dropdown with songs by the searched artist.
- **Fetch Lyrics:** Retrieves lyrics for a selected song using an API.
- **User-Friendly Interface:** Designed with Tkinter for intuitive navigation.
- **Scrollable Lyrics Display:** View long lyrics with a built-in scrollbar.

---

## **Requirements**
Ensure the following are installed on your system:
- Python 3.8 or later
- Python libraries:
  - `tkinter` (comes pre-installed with Python on most systems)
  - `requests` (for API calls)

## **Setup and Installation**

Follow these steps to set up and run the application:

1. **Clone the repository**:
  ```bash
   git clone https://github.com/your-username/lyrics-finder-app.git
   cd lyrics-finder-app
  ```
2. **Install Dependencies**
  ```bash
  pip install requests
  ```
3. Configure the API key:
* Sign up at RapidAPI to obtain an API key for the Deezer API.
* Open the app.py file.
* Replace <INSERT deezer API KEY> in the get_songList function with your API key.

4. Run the application
  ```bash
   python app.py
  ```
