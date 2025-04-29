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

