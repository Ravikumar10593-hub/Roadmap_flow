## **Data Science Roadmap🛣️ | Knowledge Graph🤯**

- Github link : https://github.com/Ravikumar10593-hub/Roadmap_flow

- App Link : https://roadmapflow-datascience.streamlit.app/

Table of Content:

1. Project details
2. Project Setup
3. Future improvement

 ![image](https://github.com/Ravikumar10593-hub/Roadmap_flow/assets/65507584/c0770f38-335b-47f2-b7da-50347bdab6c6)

### Project details
- Create a Knowledge graph which depicts the Roadmap for “Data Science Tools”.
- Divide the main nodes into categories like “Collection”, “Cleaning”, “EDA”, “Model Building” & “Model Deployment”.
- Each category will have connections to some well-known tools used within that category.
- Every time you click a node, it will give you the list of resources to learn the tool (Now we will have very limited resources for testing).

![image](https://github.com/Ravikumar10593-hub/Roadmap_flow/assets/65507584/bf61e235-03f7-4e31-8270-539b82d0a38f)

### Project Setup
**Setting up a virtual environment:**
Recently I have been using UV to create the virtual environment and install the dependencies, if you not aware about it then please give it a read(It is created in Rust and can save your lot of time).

![image](https://github.com/Ravikumar10593-hub/Roadmap_flow/assets/65507584/3482121b-2f52-4b8d-86ef-cd41b758ab0e)

```
## If you are using pip: 
pip install uv
```
Once the UV is installed, create a virtual env.

```
## To create a virtual environment:

uv venv  # Create a virtual environment at .venv.

## To activate the virtual environment:

# On macOS and Linux.
source .venv/bin/activate

# On Windows.
.\.venv\Scripts\activate.ps1
```
![image](https://github.com/Ravikumar10593-hub/Roadmap_flow/assets/65507584/666c99c3-22e4-47bd-8500-1bc827124a27)

**Install the dependencies:**
```
uv pip install streamlit
uv pip install streamlit-agraph

## Install from a requirements.txt file (OPTIONAL).
uv pip install -r requirements.txt  
```

**Create a app.py:**

```
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(layout="wide")

st.title("Data Science Tools Hierarchical Graph")

# Split the page into two columns
col1, col2 = st.columns([3, 1])

# Define the nodes
nodes = [
    Node(id="Data Science Tools", label="Data Science Tools", color="#4B0082"),
    Node(id="Collection", label="Collection", color="#4B0082"),
    Node(id="Cleaning", label="Cleaning", color="#4B0082"),
    Node(id="EDA", label="EDA", color="#4B0082"),
    Node(id="Model Building", label="Model Building", color="#4B0082"),
    Node(id="Model Deployment", label="Model Deployment", color="#4B0082"),
    Node(id="Scrapy", label="Scrapy", color="#FF5733"),
    Node(id="Beautiful Soup", label="Beautiful Soup", color="#FF5733"),
    Node(id="Selenium", label="Selenium", color="#FF5733"),
    Node(id="APIs", label="APIs (like Twitter API, Google Maps API)", color="#FF5733"),
    Node(id="SQL", label="SQL", color="#FF5733"),
    Node(id="Pandas", label="Pandas", color="#33FF57"),
    Node(id="NumPy", label="NumPy", color="#33FF57"),
    Node(id="OpenRefine", label="OpenRefine", color="#33FF57"),
    Node(id="DataWrangler", label="DataWrangler", color="#33FF57"),
    Node(id="Matplotlib", label="Matplotlib", color="#33FF57"),
    Node(id="Seaborn", label="Seaborn", color="#33FF57"),
    Node(id="Plotly", label="Plotly", color="#33FF57"),
    Node(id="Scikit-learn", label="Scikit-learn", color="#3357FF"),
    Node(id="TensorFlow", label="TensorFlow", color="#3357FF"),
    Node(id="Keras", label="Keras", color="#3357FF"),
    Node(id="PyTorch", label="PyTorch", color="#3357FF"),
    Node(id="XGBoost", label="XGBoost", color="#3357FF"),
    Node(id="Flask", label="Flask", color="#FF33A6"),
    Node(id="Django", label="Django", color="#FF33A6"),
    Node(id="FastAPI", label="FastAPI", color="#FF33A6"),
    Node(id="Docker", label="Docker", color="#FF33A6"),
    Node(id="Kubernetes", label="Kubernetes", color="#FF33A6")
]

# Define the edges
edges = [
    Edge(source="Data Science Tools", target="Collection"),
    Edge(source="Data Science Tools", target="Cleaning"),
    Edge(source="Data Science Tools", target="EDA"),
    Edge(source="Data Science Tools", target="Model Building"),
    Edge(source="Data Science Tools", target="Model Deployment"),
    Edge(source="Collection", target="Scrapy"),
    Edge(source="Collection", target="Beautiful Soup"),
    Edge(source="Collection", target="Selenium"),
    Edge(source="Collection", target="APIs"),
    Edge(source="Collection", target="SQL"),
    Edge(source="Cleaning", target="Pandas"),
    Edge(source="Cleaning", target="NumPy"),
    Edge(source="Cleaning", target="OpenRefine"),
    Edge(source="Cleaning", target="DataWrangler"),
    Edge(source="EDA", target="Pandas"),
    Edge(source="EDA", target="NumPy"),
    Edge(source="EDA", target="Matplotlib"),
    Edge(source="EDA", target="Seaborn"),
    Edge(source="EDA", target="Plotly"),
    Edge(source="Model Building", target="Scikit-learn"),
    Edge(source="Model Building", target="TensorFlow"),
    Edge(source="Model Building", target="Keras"),
    Edge(source="Model Building", target="PyTorch"),
    Edge(source="Model Building", target="XGBoost"),
    Edge(source="Model Deployment", target="Flask"),
    Edge(source="Model Deployment", target="Django"),
    Edge(source="Model Deployment", target="FastAPI"),
    Edge(source="Model Deployment", target="Docker"),
    Edge(source="Model Deployment", target="Kubernetes")
]

# Configure the graph
config = Config(
    width=900,
    height=900,
    directed=True,
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",
    collapsible=False,
    node={'labelProperty': 'label'},
    link={'labelProperty': 'label', 'renderLabel': False},
    hierarchical=True,
    layout={
        "hierarchical": {
            "enabled": True,
            "levelSeparation": 150,
            "nodeSpacing": 100,
            "treeSpacing": 200,
            "direction": "UD",  # UD for top to bottom
            "sortMethod": "directed"
        }
    },
    zoom=1.2  # Adjust as needed
)

# Define resources for each node
resources = {
    "Scrapy": {"Links": ["https://scrapy.org/"]},
    "Beautiful Soup": {"Links": ["https://www.crummy.com/software/BeautifulSoup/"]},
    "Selenium": {"Links": ["https://www.selenium.dev/"]},
    "APIs": {"Links": ["https://www.programmableweb.com/"]},
    "SQL": {"Links": ["https://www.mysql.com/"]},
    "Pandas": {"Links": ["https://pandas.pydata.org/"]},
    "NumPy": {"Links": ["https://numpy.org/"]},
    "OpenRefine": {"Links": ["https://openrefine.org/"]},
    "DataWrangler": {"Links": ["https://www.trifacta.com/products/wrangler/"]},
    "Matplotlib": {"Links": ["https://matplotlib.org/"]},
    "Seaborn": {"Links": ["https://seaborn.pydata.org/"]},
    "Plotly": {"Links": ["https://plotly.com/"]},
    "Scikit-learn": {"Links": ["https://scikit-learn.org/"]},
    "TensorFlow": {"Links": ["https://www.tensorflow.org/"]},
    "Keras": {"Links": ["https://keras.io/"]},
    "PyTorch": {"Links": ["https://pytorch.org/"]},
    "XGBoost": {"Links": ["https://xgboost.readthedocs.io/"]},
    "Flask": {"Links": ["https://flask.palletsprojects.com/"]},
    "Django": {"Links": ["https://www.djangoproject.com/"]},
    "FastAPI": {"Links": ["https://fastapi.tiangolo.com/"]},
    "Docker": {"Links": ["https://www.docker.com/"]},
    "Kubernetes": {"Links": ["https://kubernetes.io/"]},
    # Add more resources for other nodes if needed
}

# Display the graph
st.sidebar.title("Resources")
clicked_node = agraph(nodes=nodes, edges=edges, config=config)

if clicked_node:
    node_resources = resources.get(clicked_node, {"Links": []})
    
    st.sidebar.subheader("Links")
    for link in node_resources["Links"]:
        st.sidebar.markdown(f"[{link}]({link})")
else:
    st.sidebar.write("Click on a node to see the resources.")
```
Streamlit Configuration:

- The page is set to a wide layout.
- The title of the page is “Data Science Tools Hierarchical Graph”.
  
Layout:

- The page is divided into two columns with a ratio of 3:1.
Node Definitions:

- Nodes are defined to represent various categories and tools within data science.
- Categories include “Collection”, “Cleaning”, “EDA”, “Model Building”, and “Model Deployment”.
- Tools such as “Scrapy”, “Pandas”, “Scikit-learn”, and “Docker” are included under their respective categories.
- Each node has an ID, label, and color.
Edge Definitions:

- Edges are created to connect the “Data Science Tools” node to the various category nodes.
- Each category node is connected to its respective tools.
Graph Configuration:

- The graph is set to be directed and has node highlight behavior enabled.
- The hierarchical layout is enabled, with nodes arranged from top to bottom.
- Graph dimensions and zoom are set.
Resource Links:

- A dictionary named resources is defined to map tools to their respective resource links.
- Each tool has a list of related links.
Graph Display and Interaction:

- The graph is displayed using agraph with the specified nodes, edges, and configuration.
- A sidebar is created to display resources for a clicked node.
- If a node is clicked, relevant resource links are shown in the sidebar.
- If no node is clicked, a default message is displayed in the sidebar.
![image](https://github.com/Ravikumar10593-hub/Roadmap_flow/assets/65507584/46c98653-bcba-459e-b7bd-4bc934abdba6)

### Future improvement
- Change the rounded nodes with the respective images.
- Add more quality resources(Both PDF and links).

### More about me:
I am a Data Science enthusiast🌺, Learning and exploring how Math, Business, and Technology can help us to make better decisions in the field of data science.

Want to read more: https://medium.com/@ravikumar10593/

YouTube Link (100k+ views): https://www.youtube.com/raviscontent

Find my all handles: https://linktr.ee/ravikumar10593

### How to Set this up in your local
- `git clone <Copy the URL from the dropdown>` or Download the zip
- If you have uv the `uv pip install -r requirements.txt` else `pip install -r requirements.txt`
- `streamlit run app.py`

