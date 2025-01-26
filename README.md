# **Simple Stock Price Chart Application**  
*A minimal and responsive web app for visualizing stock prices.*

---

## 📖 **Overview**  

SSPCA (Stock Price Chart Application) is an intuitive web application that enables users to visualize historical stock prices for publicly traded companies. Built using Python's Dash framework, the app delivers a user-friendly interface where users can input stock tickers, select desired timeframes, and analyze trends interactively.  

---

## 🚀 **Features**  

- 📈 **Interactive Stock Visualization**  
  - Real-time stock price data fetched using Yahoo Finance.  
  - Interactive line charts for better insights into stock performance.  

- ⏱️ **Customizable Timeline**  
  - Select timelines such as 1 month, 6 months, 1 year, or 5 years.  
  - Default time range set to 1 year for quick access.  

- 🖥️ **User-Friendly Interface**  
  - Simple, clean, and aesthetic UI for all types of users.  
  - Mobile-responsive design for seamless access across devices.  

- ✅ **Lightweight Application**  
  - Fast load times and responsive interactions.  
  - Built with minimal dependencies to ensure easy setup and usage.  

- 🔗 **Footer Branding**  
  - Displays attribution to the creator for personalized branding.  

---

## 🖼️ **Screenshots**  
### 🏠 Home Page  
![Home Page](https://github.com/user-attachments/assets/09b00c56-cff0-4550-a75c-9e271bb5f685)  
*An intuitive homepage where users can enter the stock ticker and select a timeline.*  

### 📊 Stock Price Visualization  
![Stock Visualization](https://github.com/user-attachments/assets/1bc87eb2-6ce5-48e5-911e-cbd04c53610c)  
*Visual representation of historical stock prices based on user input.*

---

## 🛠️ **Installation**  

Follow the steps below to set up and run the application on your local machine:  

### **Prerequisites**  
- Python 3.9 or higher  
- pip (Python package manager)  

### **Clone the Repository**  
```bash
git clone https://github.com/Divu_skp/stock-tracker.git  
cd stock-tracker  
```

### **Install Dependencies**
```bash
pip install -r requirements.txt 
```
### **Run the Application**
```bash
python app.py 
```
The app will run locally at http://127.0.0.1:8050.

## **🧑‍💻 Usage**
**1. Enter Stock Ticker:** Input the stock ticker (e.g., AAPL for Apple, GOOGL for Google).

**2. Select Timeline:** Choose from dropdown options (1 month, 6 months, 1 year, 5 years).

**3. Visualize Data:** View an interactive graph displaying the stock's historical closing prices.

## **📂 Project Structure**
```plaintext
.
├── app.py                # Main application file  
├── README.md             # Documentation  
├── requirements.txt      # Dependencies for the app  
├── assets/               # (Optional) Folder for custom styles/images
```
## **🛠️ Requirements File**
Ensure your requirements.txt file includes the following dependencies:
```plaintext
dash  
plotly  
yfinance 
```

## **💡 Future Enhancements**
- Add support for multiple tickers in a single graph.
- Include indicators like moving averages, RSI, or volume data.
- Enable export of stock data as CSV.
- Deploy the application on platforms like Heroku, Render, or AWS.
- Add user authentication for watchlist management.

## **🏗️ Built With**
- **Python:** For backend processing and API integration.
- **Dash:** For building the interactive and responsive web application.
- **Plotly:** For creating dynamic and visually appealing stock charts.
- **Yahoo Finance:** For retrieving real-time and historical stock data.

## **👨‍💻 Author**
Created with ❤️ by Dwived Krishna P.

Feel free to connect or contribute!

## **🌟 Show Your Support**
If you found this project useful, please consider giving it a ⭐ on GitHub!
