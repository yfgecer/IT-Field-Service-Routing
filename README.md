 # TechFix Solution Company 

 ## 1. Real-World Problem Context
In big cities like Istanbul, traffic congestion is a major problem for service operations. **TechFix Solutions** is an IT field support company, and its main headquarters is located in Fatih. When a branch office has a hardware or network problem, the company needs to send technical teams to that district as quickly as possible.

## 2. Problem Definition
The main problem in this project is finding the fastest routes from the Fatih headquarters to six different branch locations in Istanbul (Kagithane, Besiktas, Uskudar, Kadikoy, Umraniye, and Atasehir). Since physical distance does not always mean shorter travel time in a busy city, our goal is to minimize the total travel time (in minutes) for the technical teams. Additionally, we need to analyze how these optimal routes change dynamically when an unexpected event, like a major traffic accident, blocks a main road.

## 3. Network Model
I specifically chose **The Shortest Route Problem** for this project. 

I chose this model because our main goal is very clear: finding the minimum travel time from one single starting point (Fatih headquarters) to specific destination points (our branches).

## 4. Nodes, Edges, and Data Details
To build our network model, I prepared a dataset (`network_data.csv`). As required, here is the detailed explanation of the data, columns, and my assumptions:

**1. Meaning of Each Column:**
* **Source:** This column represents the starting point (district) of a road segment.
* **Target:** This column represents the ending point (district) of that road segment.
* **Weight:** This column shows the cost of traveling in terms of **minutes** between the Source and the Target.

**2. Nodes and Edges:**
* **Nodes:** They represent our 7 district locations (Fatih, Kagithane, Besiktas, Uskudar, Kadikoy, Umraniye, Atasehir).
* **Edges:** They represent the main roads, bridges, and tunnels connecting these districts.

**3. Assumptions Behind the Data:**
* **Traffic Conditions:** I assumed that the travel times in the dataset reflect "average busy daytime traffic." They are not empty night-time roads.
* **Direct Connections:** I assumed that direct edges only exist between logical neighbor districts. For example, there is no direct edge from Fatih to Umraniye; the team must pass through Uskudar or Kadikoy first.
* **Two-Way Symmetrical Roads:** I assumed that the travel time is the same for both directions (e.g., going from Fatih to Besiktas takes the same time as going from Besiktas to Fatih).

## 5. Selected Algorithm: The Shortest Route Solution Method (Dijkstra)

For this problem, I selected **Dijkstra's Algorithm**, which follows the standard shortest route solution method we learned. 

**Why this algorithm?**
Because my project is a "Single-Source Shortest Path" problem. I have one starting origin (Fatih headquarters) and I need to find the minimum travel time to all other branch nodes. Since all our edge weights are positive numbers (travel minutes), this method is the most appropriate choice.

**Steps of the shortest route solution method applied to our project:**
In summary, the algorithm solves our routing problem by following these exact steps:
1. Select the node with the shortest direct route from the origin (Fatih).
2. Establish a *permanent set* with the origin node and the node that was selected in step 1.
3. Determine all nodes directly connected to the permanent set nodes.
4. Select the node with the shortest route (branch) from the group of nodes directly connected to the permanent set nodes.
5. Repeat steps 3 and 4 until all nodes (all target districts in Istanbul) have joined the permanent set.

## 6. Python Implementation
To solve the problem mathematically and visually, I implemented the project in Python. I used three main Python libraries to build this routing system:

* **Pandas:** I used Pandas to read our road network data (source, target, and time weights) from the `network_data.csv` file. This makes the project dynamic; if a new road is built in Istanbul or travel times change, we just update the CSV file without changing the core Python code.
* **NetworkX:** This is the core library for our network model. I used it to convert the CSV data into a mathematical Graph. Then, I used its built-in `single_source_dijkstra` function to calculate the shortest paths. This function automatically applies the 5 steps of the shortest route solution method we discussed.
* **Matplotlib:** I used this library to create visual maps of our network. It allows us to draw the nodes, show the connections, and highlight the fastest routes in different colors. It is especially useful to visualize how the routes dynamically change during our accident scenario.

## 7. Results
The algorithm was tested in two different stages to prove its accuracy and flexibility. 

**1. Base Network Results (Normal Traffic):**
Under normal daytime traffic conditions, the algorithm calculated the optimal shortest paths from the Fatih headquarters to all 6 branch locations. Here is the complete list of the fastest routes:
* **To Kagithane:** 35 minutes (Route: Fatih -> Kagithane)
* **To Uskudar:** 40 minutes (Route: Fatih -> Uskudar)
* **To Kadikoy:** 45 minutes (Route: Fatih -> Kadikoy)
* **To Besiktas:** 45 minutes (Route: Fatih -> Besiktas)
* **To Atasehir:** 70 minutes (Route: Fatih -> Kadikoy -> Atasehir)
* **To Umraniye:** 70 minutes (Route: Fatih -> Uskudar -> Umraniye)

**2. Scenario Results (Major Accident Rerouting):**
In this scenario, the direct roads from Fatih to Kadikoy and Uskudar were heavily blocked. Travel times increased to **120 minutes** and **100 minutes**, respectively.

When I re-ran the algorithm with the new data, the system realized that the old routes were now too slow. It automatically ignored the blocked roads and created new alternative routes. Instead of waiting in traffic, the algorithm rerouted the Asian-side teams through **Besiktas**. Here are the recalculated shortest paths:
* **From Fatih**

* **To Kagithane:** 35 minutes (Unchanged)
* **To Besiktas:** 45 minutes (Unchanged)
* **To Uskudar:** 65 minutes (New Route: Fatih -> Besiktas -> Uskudar)
* **To Kadikoy:** 75 minutes (New Route: Fatih -> Besiktas -> Kadikoy)
* **To Umraniye:** 95 minutes (New Route: Fatih -> Besiktas -> Uskudar -> Umraniye)
* **To Atasehir:** 105 minutes (New Route: Fatih -> Besiktas -> Kadikoy -> Atasehir)

## 8. Managerial Interpretation
If I were the Operations Manager at this company, I would use this model for three main business goals:

**1. Cost and Resource Efficiency:** 
By always using the absolute shortest routes, the company minimizes unnecessary travel time. This directly reduces daily fuel costs. Also, because teams spend less time in traffic, they can solve more IT problems in a single day.

**2. Crisis Management and Agility:** 
Istanbul's traffic is unpredictable. Our accident scenario proves that the company can survive unexpected crises. When a main tunnel is blocked, managers do not need to panic or guess alternative roads. They can simply update the travel times in the system, and the algorithm instantly provides a "Plan B" (like rerouting the teams through Besiktas). This makes the company's operations highly agile.

**3. Better Customer Satisfaction:** 
With this system, managers can give accurate estimated arrival times (ETA) to the branches. If an accident increases the travel time to Atasehir from 70 minutes to 105 minutes, the manager can see this immediately and inform the branch proactively. 

**4. System Scalability:** 
Currently, this project uses a small network of 7 districts as a "Proof of Concept" (PoC). In a small map, a human can easily guess the shortest route by looking at it. However, real-world logistics are much more complex. Istanbul has 39 districts and hundreds of neighborhoods. When the network grows to 500 nodes and thousands of edges, human calculation becomes impossible. Because we used Dijkstra's Algorithm, this system is highly **scalable**. It will calculate the optimal routes instantly even if we expand the dataset to cover hundreds of new branches across Turkey.

## 9. How to Run the Code

To run this project on your local machine, please follow the steps below. Make sure your terminal is opened in the root directory of the project.

**1. Install Required Libraries:**
Instead of installing packages one by one, you can install all dependencies at once using the provided requirements file. Run this command in your terminal:
`pip install -r requirements.txt`

**2. Run the Main Solution:**
The core routing algorithm is written in a separate Python script. To quickly calculate the shortest paths and see the text-based results in your terminal, run the solution file located in the `src` folder:
`python src/solution.py`

**3. Visual Analysis and Scenarios:**
For a detailed step-by-step breakdown, visual network maps, and testing the dynamic accident scenario, you can use the Jupyter Notebook located in the `notebooks` folder. 
Start Jupyter by typing:
`jupyter notebook`
Then, navigate to the `notebooks/analysis.ipynb` file in your browser and run the cells.
*Alternative way to open the notebook:* 
If you are using **Visual Studio Code (VS Code)**, you do not need to use the terminal. You can simply install the "Jupyter" extension in VS Code, click on `analysis.ipynb`, and run the cells directly inside your editor.

## 10. References
**1. Academic Resources:**
* **Taylor, B. W. (2016).** *Introduction to Management Science* 
* **Course Lecture Slides:**

**2. Data & Mapping Resources:**
* **Google Maps:** Used for estimating real-time and average travel times (in minutes) between Istanbul districts.
* **Google My Maps:** Used for planning the coordinates and geographical connections of the network nodes.
* **Istanbulharitasi360.com:** Referenced for verifying the logical neighbor connections and district layouts of the Istanbul city map.

