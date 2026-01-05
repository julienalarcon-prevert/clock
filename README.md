Voici le README mis à jour en anglais, sans la mention de l'association 2'Danse.

Voici toutes les informations que vous m'avez demandé d'enregistrer. Si vous souhaitez modifier vos paramètres, vous pouvez le faire sur la page [informations enregistrées](https://gemini.google.com/saved-info).

---

# 🕒 Python Clock Project

This Python project is an interactive time-management application. It displays time in a `hh:mm:ss` format, allowing users to synchronize with the system clock, manually set a starting time, and configure an alarm.

## 📋 Features

* **System Clock Mode**: Automatically fetches and starts the clock from your computer's current time.
* **Manual Setting**: Allows users to input a custom start time using a tuple `(hours, minutes, seconds)`.
* **Alarm System**: A dedicated function to set a "wake-up" time. The program triggers a message when the clock matches the alarm tuple.
* **Dynamic Updates**: Real-time updates every second with precise logic for time carry-overs (60s  1min, 60min  1h).
* **Tuple-Based Logic**: All time data is stored and manipulated as immutable tuples to ensure data integrity.

## 🛠️ How It Works

The program follows a modular structure controlled by a **Main Menu**:

1. **Initialize**: The user chooses between System Time or Manual Entry.
2. **The Loop**: The program enters a `while True` loop.
* **Display**: Formats the tuple into a readable string (e.g., `16:30:00`).
* **Check**: Compares the current time tuple to the alarm tuple.
* **Wait**: Pauses for 1 second using `time.sleep(1)`.
* **Calculate**: Deconstructs the tuple, increments the second, manages carries, and reconstructs a new tuple.



