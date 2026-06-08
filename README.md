# GUI Calendar Application 📅

A simple and interactive desktop Calendar Application built using **Python**, **Tkinter**, and **tkcalendar**. This project provides a graphical calendar interface that allows users to view and select dates through an easy-to-use GUI.

## 🚀 Features

* Interactive calendar interface
* Date selection functionality
* User-friendly graphical interface
* Lightweight desktop application
* Built using Python GUI libraries
* Simple and easy to customize

## 🛠️ Technologies Used

* Python 3.x
* Tkinter
* tkcalendar

## 📂 Project Structure

```bash
GUI-Calendar/
│
├── GUI_Calendar.py
├── README.md
```

## 📸 Application Preview

<img width="600" alt="Calendar App Screenshot" src="https://via.placeholder.com/600x350?text=GUI+Calendar+Application">

*Replace the above image with your project screenshot.*

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/GUI-Calendar.git
cd GUI-Calendar
```

### 2. Install Dependencies

```bash
pip install tkcalendar
```

### 3. Run the Application

```bash
python GUI_Calendar.py
```

## 💻 Sample Code

```python
from tkinter import *
from tkcalendar import *

root = Tk()

root.title("2026 Calendar")
root.geometry("600x400")

cal = Calendar(root, year=2026, month=6, day=4)
cal.pack(pady=60)

root.mainloop()
```

## 🎯 Learning Outcomes

* Python GUI Development
* Tkinter Widgets and Layout Management
* Third-Party Library Integration
* Event-Driven Programming
* Desktop Application Development

## 🔮 Future Enhancements

* Add event scheduling functionality
* Save selected dates to a database
* Add reminders and notifications
* Dark mode support
* Multiple calendar views

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Om Mayekar**

* GitHub: https://github.com/Om-Mayekar
* LinkedIn: https://linkedin.com/in/ommayekar
