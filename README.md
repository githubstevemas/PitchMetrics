# PitchMetrics
<br>

Python project designed to scrape data from [Pitchfork](https://pitchfork.com/) and [Musicbrainz](https://musicbrainz.org) then perform data analysis on the collected information. The project utilizes the `BeautifulSoup` library for web scraping and `plotly` for grahpics to gather and analyze music reviews and other related data.

<br>

## Features

- Scrapes music reviews and other data from Pitchfork.com and Musicbrainz.org.
- Stores the scraped data in a PostgreSQL database.
- Prevents duplicate data insertion using `ON CONFLICT` handling in PostgreSQL.
- Displays graphical analyzes.
  
<br>

## Technologies Used

- [Python](https://www.python.org/) – Core programming language.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – For web scraping and parsing HTML content.
- [Requests](https://pypi.org/project/requests/) – For handling HTTP requests to retrieve web pages.
- [SQLAlchemy](https://www.sqlalchemy.org/) – For database interaction and ORM.
- [PostgreSQL](https://www.postgresql.org/) – As the database to store scraped data.
- [Plotly](https://plotly.com/) - To display dynamic charts.

<br>

## Setup Instructions

1. *Clone the repository*:
    ```bash
    git clone https://github.com/githubstevemas/Pitchfork-Scrap.git
    cd Pitchfork-Scrap
    ```

2. *activate the environement :*
    ```
    env/Scripts/activate
    ``` 

3. *Install dependencies*:
    ```bash
    pip install -r requirements.txt
    ```
    
4. *Set up the PostgreSQL database*:
   
    Create a `.env` file and add the following environment variables
      ```env
      DB_USERNAME=your_username
      DB_PASSWORD=your_password
      DB_NAME=pitchfork
      DB_HOST=localhost
      DB_PORT=5432
      ```
<br>

## Usage

1. *First you need to scrape datas with*:
    ```
    python main.py
    ```

2. *Run django server*:
    ```
    cd .\pitch_metrics\
    python manage.py runserver
    ```

3. *You can test the app localy in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000/).*


<br>

## Contact
Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
