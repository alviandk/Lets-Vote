
## Let's Vote Backend Application

Let's Vote is an API built with Django and Django REST framework, backed by a PostgreSQL database, designed to manage voting processes with ease.

### Prerequisites

1.  Python 3.8 or higher
2.  pip
3.  virtualenv (recommended)
4.  PostgreSQL

### Setting Up the Project

1.  **Clone the Repository**
        
    ```
    git clone https://github.com/yourusername/lets-vote.git
    cd lets-vote
    ``` 
    
2.  **Create a Virtual Environment (Recommended)**
    
    
    ```
    virtualenv venv
    source venv/bin/activate  
    # On Windows use `venv\Scripts\activate` 
    ``` 
    
3.  **Install Dependencies**
    
    `pip install -r requirements.txt` 
    
4.  **Setup PostgreSQL**
    
    -   Ensure PostgreSQL is running.
        
    -   Create a database for the project:
        
        `createdb lets_vote_db` 
        
    -   Create a .env File:
        
        In the root of your Django project, create a `.env` file with the following content:

        ```
        DEBUG=True
        SECRET_KEY=your-secret-key
        DB_NAME=your-database-name
        DB_USER=your-database-user
        DB_PASSWORD=your-database-password
        DB_HOST=your-database-host
        DB_PORT=your-database-port
        ```
        
5.  **Run Migrations**
        
    `python manage.py migrate` 
    
6.  **Start the Development Server**
    
    
    `python manage.py runserver` 
    

The server will start, and you can access the API at `http://127.0.0.1:8000/`.

### API Endpoints

-   List all votes: `GET /api/votes/`
-   Retrieve a vote: `GET /api/votes/<vote_id>/`
-   Create a vote: `POST /api/votes/`
-   Update a vote: `PUT /api/votes/<vote_id>/`
-   Delete a vote: `DELETE /api/votes/<vote_id>/`

... [continue with other endpoints as necessary]

### Testing

Run tests by executing:

`python manage.py test` 
