# Hotel Self Check-In (Flask)

A simple, modern Flask web app for hotel self check-in, featuring a stylish landing page and check-in form.

## Features
- Landing page inspired by [this design](https://img.freepik.com/free-vector/flat-landing-page-template-hotel-accommodation_23-2150312508.jpg)
- Self check-in form (name and reservation code)
- Flash messages for feedback
- Responsive, mobile-friendly UI (Bootstrap)
- Ready for deployment and testing

## Setup
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add the landing image**
   - Download the image from [here](https://img.freepik.com/free-vector/flat-landing-page-template-hotel-accommodation_23-2150312508.jpg)
   - Save it as `static/hotel_landing.jpg`

## Run the App
```bash
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Run Tests
```bash
pytest
```

## Project Structure
```
HotelCheckIn/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── style.css
│   └── hotel_landing.jpg  # <- Download and add manually
├── templates/
│   ├── landing.html
│   └── checkin.html
└── tests/
    └── test_app.py
``` 