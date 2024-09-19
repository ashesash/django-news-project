# Thunder News - A Django News Blog

A news blog built with Django featuring a carousel for displaying the latest news stories. This project demonstrates Django's class-based views and static files handling, alongside Glide.js for an image carousel.

The deployed app can be accessed here:
[Thunder News](https://thunder-news.fly.dev/)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Customization](#customization)
- [Technologies Used](#technologies-used)

## Features

- Display news articles with title, author, and publication date.
- A carousel on the homepage that automatically rotates the latest stories.
- Mobile responsive design using Glide.js for a smooth user experience.
- Django admin interface for managing news stories.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python (3.12 or later)
- Django (4.x or later)
- Glide.js (via CDN or local files)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/django-news-blog.git
    cd django-news-blog
    ```

2. Set up a virtual environment and activate it:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Navigate to `http://127.0.0.1:8000/` in your web browser to view the news blog.

## Usage

### Adding News Stories

1. Access the Django admin at `http://127.0.0.1:8000/admin/`.
2. Add news stories via the `NewsStory` model.
3. The homepage will automatically display the latest 4 stories in a carousel and all other stories below it.

### Glide.js Carousel

The latest 4 stories are displayed in a carousel on the homepage, using the Glide.js library. The carousel autoplays by default and pauses when hovered.

## Customization

### Changing the Number of Stories in the Carousel

By default, the homepage displays the latest 4 stories in the carousel. To change this:

1. Open `views.py` in the `news/` directory.
2. Update the line in `IndexView.get_context_data`:

    ```python
    context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
    ```

   Change `4` to the desired number of stories.

### Customizing Glide.js

You can modify the settings for the Glide carousel by editing `carousel.js` in the `base.html` file.

Example:

```javascript
new Glide('.glide', {
    type: 'carousel',
    autoplay: 5000,          // Autoplay interval in milliseconds (5 seconds)
    perView: 1,              // Number of slides to display at once
    gap: 20,                 // Space between slides
    hoverpause: true         // Pause autoplay on hover
}).mount();
```

## Technologies Used

- **Django**: A Python web framework used to build the news blog.
- **Glide.js**: A responsive and modern carousel library for displaying the latest news stories.
- **HTML/CSS/JavaScript**: Frontend development.
- **SQLite**: Default Django database for development.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


