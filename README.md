# Train Delay Notifier

## Overview

The **Train Delay Notifier** is a Python application designed to track real-time delays and notify users about train schedule changes. This project aims to provide commuters with timely 
information, ensuring they can plan their travels efficiently and avoid missing trains. This project applies to Southern California's [Metrolink Trains](https://metrolinktrains.com/) only. 

## Features

- **Real-time train delay tracking: Fetches data about train schedules and delays from an external API.
- **Notifications**: Alerts users of upcoming train delays via SMS.
- **User preferences**: Customizable settings to receive notifications based on train lines, stations and specific times. 
    - Initially, settings will need to be inputted via terminal or manually.

## Tech Stack

- **Python**: For the main application logic. 
- **Flask**: For buiding a simple web app to show train status.
- **Requests**: For making HTTP requests to fetch real-time data.
- **API**: Integrates with Metrolink API (or build a mock API for local testing)

## Getting Started 

### Prerequisites

- Python 3.6 or higher
- Virtual environment (optional but recommended)
- A train delay API key (if applicable)
 
