🖼️ Product Catalog Image API 🚀

A REST API backend for product catalog image scraping and resizing. Streamline your image management with ease!

📝 **How to Run:**
1. Activate your virtual environment.
2. Install requirements: `pip install -r requirements.txt`
3. Migrate your database: `python manage.py makemigrations` & `python manage.py migrate`
4. Launch the server: `python manage.py runserver`

## Running with Docker and Docker Compose 🐳

We can easily run the "dj_backend" project using Docker and Docker Compose for quick setup. Follow these steps:

1. **Build the Docker Image:**

   ```bash
   docker build -t dj_backend .
   ```
1. **Using Docker Compose:**

   ```bash
   docker-compose up --build -d # To run
   docker-compose stop  # To stop
   ```

🕵️ **How to Scrape Images:**
To scrape images, simply run our custom management command: `python manage.py scrape`

🌐 **API Endpoints:**
- Retrieve specific image info: `/api/v1/catalog/images/retrieve/{ID}/`
- Get all scraped images from the original source URL name: `/api/v1/catalog/images/retrieve-by-source-url/{SOURCE_URL_NAME}/`
- Fetch images of specific sizes by adding query parameters, e.g., `/api/v1/catalog/images/retrieve/755b31ce-643b-427a-9f5b-0870a5fe9f43/?size=small`

For inquiries or assistance, contact us at imamhossainroni95@gmail.com. Start optimizing your image workflows today! 📸✨
