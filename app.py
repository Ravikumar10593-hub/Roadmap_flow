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
