# Reading Materials API

This is the backend for the **Reading Materials App**, a full-stack project built as part of our Unit 4 Collaboration Project.

The API allows users to:
- Create, read, update, and delete reading materials (books, magazines, mangas)
- Create and view reviews associated with each reading material
- Fetch reading materials along with all related reviews nested inside the response

---

## Team Members

- [Christian Vieux](https://github.com/christianvieux)
- [Diana Wilson](https://github.com/DianaWilson1)
- [Zackary O'Connor](https://github.com/zackaryoconnor)
- [Alex Jungers](https://github.com/ajungers-ga)

---

## Frontend Repository

The frontend for this project is being developed separately and can be found at:

🔗 [Frontend Repository - Reading Materials App](https://github.com/zackaryoconnor/Front-End)

---

## Full CRUD Functionality

This API fully supports Create, Read, Update, and Delete (CRUD) operations for both ReadingMaterials and Reviews.  
Users can:
- Create new reading materials and reviews
- Retrieve lists or specific entries
- Update existing records
- Delete records if needed

All endpoints follow RESTful design principles for easy frontend integration.


## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL (for production database, SQLite used for development)
- Git / GitHub for version control


## Setting Up the Python Environment

To set up your local environment, follow these steps:

1. **Create and Activate a Virtual Environment:**

    - **On macOS/Linux:**
      ```bash
      python3 -m venv env
      source env/bin/activate
      ```

    - **On Windows:**
      ```bash
      python -m venv env
      .\env\Scripts\activate
      ```

2. **Install Dependencies:**
   Once the environment is activated, install the required packages:
   ```bash
   pip install -r requirements.txt

3. **Create and Configure `.env` File:**

   Create a `.env` file in the root of your project to store your environment-specific settings.

   **Example `.env` file:**
   ```
   # Database configuration
   DATABASE_ENGINE=django.db.backends.postgresql   # Only include this if you're using PostgreSQL. Omit this line for SQLite (SQLite is default).
   DATABASE_NAME=your_db_name                      # Only include if using PostgreSQL
   DATABASE_USER=your_db_user                      # Only include if using PostgreSQL
   DATABASE_PASSWORD=your_db_password              # Only include if using PostgreSQL
   DATABASE_HOST=localhost                         # Only include if using PostgreSQL
   DATABASE_PORT=5432                              # Only include if using PostgreSQL

   # Allowed Origins for CORS
   ALLOWED_ORIGINS=localhost, 54.173.248.136      # Only include if needed
   ```

### **IMPORTANT:**

- **If you’re using SQLite**, **do not include the `DATABASE_ENGINE` line** in the `.env` file. SQLite is the default.
  
- **If you’re using PostgreSQL (or another DB engine)**, **include the `DATABASE_ENGINE` line** and set it to `django.db.backends.postgresql` or another engine.
  
- **Only include database settings** (`DATABASE_NAME`, `DATABASE_USER`, etc.) if you're using PostgreSQL. For SQLite, you don’t need any database settings in the `.env` file.


## API Endpoints Overview

### Reading Materials
Method	Endpoint	Description
GET	/api/reading-materials/	List all reading materials
POST	/api/reading-materials/	Create a new reading material
GET	/api/reading-materials/<id>/	Retrieve a specific reading material with its reviews
PUT/PATCH	/api/reading-materials/<id>/	Update a reading material
DELETE	/api/reading-materials/<id>/	Delete a reading material

### Reviews
Method	Endpoint	Description
GET	/api/reviews/	List all reviews
POST	/api/reviews/	Create a new review (linked to a reading material)
GET	/api/reviews/<id>/	Retrieve a specific review
PUT/PATCH	/api/reviews/<id>/	Update a review
DELETE	/api/reviews/<id>/	Delete a review

## Special Features

Nested Reviews: When fetching a Reading Material by ID, all related Reviews are included automatically inside the response.

Clean project structure following Django REST API best practices.

Separation of concerns: Reading Materials and Reviews are handled by two separate Django apps.

