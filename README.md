Backend
This section provides an overview of the backend setup of the Rentify project.

Technologies
FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
MongoDB: A NoSQL database for storing property data.
Setup
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/rentify-backend.git
cd rentify-backend
Create a virtual environment and activate it:

sh
Copy code
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
Install dependencies:

sh
Copy code
pip install -r requirements.txt
Set up environment variables:
Create a .env file with the following content:

env
Copy code
MONGO_URI=mongodb://localhost:27017/rentify
Run the FastAPI server:

sh
Copy code
uvicorn main:app --reload
The server will be running at http://localhost:8000.

Folder Structure
plaintext
Copy code
rentify-backend/
├── app/
│ ├── api/
│ │ ├── v1/
│ │ │ ├── endpoints/
│ │ │ │ ├── properties.py
│ │ │ │ └── ...
│ │ │ ├── **init**.py
│ │ │ └── ...
│ │ └── ...
│ ├── core/
│ │ ├── config.py
│ │ └── ...
│ ├── models/
│ │ ├── property.py
│ │ └── ...
│ ├── crud/
│ │ ├── crud_property.py
│ │ └── ...
│ ├── schemas/
│ │ ├── property.py
│ │ └── ...
│ ├── main.py
│ └── ...
├── .env
├── requirements.txt
└── ...
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please read the CONTRIBUTING file for guidelines on how to contribute.

Contact
For any inquiries, please contact iwinissacofficial@gmail.com.
