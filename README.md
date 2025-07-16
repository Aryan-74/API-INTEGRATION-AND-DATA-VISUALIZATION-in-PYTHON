# API-INTEGRATION-AND-DATA-VISUALIZATION-in-PYTHON

this is the first project of my first summer internship in python programming

COMPANY: CODTECH IT SOLUTIONS

NAME: Aryan Jain

INTERN ID: CT04DG1236

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

DESCRIPTION: 

**Overview:**

Task 1 of the CODTECH Python internship focuses on the integration of a public API with a Python script and the visualization of the collected data using popular data visualization libraries like **Matplotlib** or **Seaborn**. This task is designed to help students understand how to fetch real-time data from an external web service, process it programmatically, and then visualize it in a clean, readable format. It emphasizes essential skills in API handling, data parsing, and plotting — all of which are foundational in both data science and modern software development.

**Objective:**

The primary goal of this task is to develop a Python script that retrieves weather-related data from a **public API** (for example, the OpenWeatherMap API), processes the response, and then visualizes the information such as temperature trends, humidity levels, or atmospheric conditions over time. The script should not only retrieve and display data but should do so in a manner that is visually intuitive and insightful to the end user.

**Approach:**

To complete this task, the first step was identifying a reliable and freely available API. The **OpenWeatherMap API** was selected because it offers a wide range of weather information including temperature, wind, humidity, pressure, and forecasts for specific cities.

After registering and acquiring a free API key from OpenWeatherMap, the Python `requests` library was used to send an HTTP GET request to the API endpoint. This returned a JSON object that contained forecast data for the chosen city.

The JSON data had to be carefully parsed to extract relevant information such as datetime and temperature. Each forecasted data point included a timestamp and various atmospheric measurements. This data was stored in Python lists for further processing.

To visualize the data, libraries such as **Matplotlib** and **Seaborn** were employed. These libraries are powerful tools in the Python ecosystem that allow for detailed and customizable plotting. The temperature data was plotted against time, generating a line chart that displayed how the temperature fluctuates over a 5-day period in a particular city. The `seaborn.lineplot()` function was used to ensure smooth lines and consistent styling.

Several customizations were added to the plot to enhance readability. These included rotating x-axis labels for better date-time readability, adjusting figure size for clearer visualization, limiting the number of x-axis ticks to avoid crowding, and adding gridlines and labels for clarity.

In addition to the visualization, the script includes error handling to catch and report API errors such as invalid API keys or unsupported city names. This ensures the program doesn't crash if the API returns an unexpected response.

**Learning Outcomes:**

Through this task, several important skills were developed:

* Understanding the basics of **REST APIs**
* Using the **requests** library to interact with external services
* Handling and parsing **JSON** data in Python
* Visualizing time-series data using **Matplotlib** and **Seaborn**
* Writing clean and readable code with appropriate comments and structure
* Implementing basic error handling to deal with API errors


**Conclusion:**

Task 1 effectively combines real-world programming with data visualization, giving students a glimpse into how modern applications use APIs to fetch live data and turn it into actionable insights. Completing this task lays a strong foundation for further projects in data analysis, machine learning, and full-stack development. It also enhances practical skills that are valuable in industry scenarios such as dashboard creation, reporting tools, and live data monitoring systems.

DATA VISUALIZATION: <img width="1400" height="600" alt="weather_visualizer_Delhi" src="https://github.com/user-attachments/assets/d76bd066-4329-4b39-b4ab-2ecb9c21c81f" />

