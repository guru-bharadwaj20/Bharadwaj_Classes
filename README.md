# First_GUI
This is a Python-based GUI application built with `Tkinter` for managing user authentication, input forms, course details, and payments for the fictional "Bharadwaj Classes". The application simulates an educational management system that provides a user-friendly interface for login, registration, course selection, and payment processing.

## Features

- **User Authentication**: A login screen with username and password fields. The default credentials are:
  - Username: `admin`
  - Password: `password`
  
- **Registration Form**: After successful login, users can submit their details such as Name, Age, University, Gender, and Nationality.

- **Course Selection**: Users can choose from a list of courses (Java, C, C++, Python). Upon selection, detailed course information is displayed including instructor, duration, description, and price.

- **Payment Window**: After course selection, the user is presented with a QR code for making a payment.

## How It Works

1. **Login Page**: Users must enter a valid username and password to access the system. Invalid login attempts will trigger error messages.
2. **Registration Form**: Once logged in, users enter their personal details (Name, Age, University, Gender, Nationality).
3. **Course Selection**: After submitting their details, users can select a course and view detailed information about it.
4. **Payment Window**: After selecting a course, users are shown a QR code for making the payment and a "Done!" button to finish the process.
