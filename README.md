# 🌐 Fully Dynamic Graph Summarization
> A powerful, user-friendly tool for summarizing massive dynamic graphs without starting from scratch on every update.

## 🚀 What is This?

Imagine trying to store and analyze Facebook's friend network or Twitter's follow graph—billions of nodes and edges that change every second. Traditional approaches either can't handle the scale or need to rebuild everything when a single edge changes. **That's where we come in.**

This tool provides **fully dynamic graph summarization**, meaning you can:
- Compress massive graphs into compact, meaningful summaries
- Handle edge additions and deletions in near-constant time
- Preserve essential structural properties while dramatically reducing size
- Visualize and interact with your graphs through an intuitive interface

## ✨ Key Features

- **🔄 Dynamic Updates**: Efficiently handles edge insertions and deletions without recomputing the entire summary
- **🧠 Hybrid Intelligence**: Combines lightweight numerical techniques with neural networks for optimal performance
- **📊 Interactive Visualization**: User-friendly interface to explore, update, and analyze large-scale graphs
- **⚡ High Performance**: Processes updates in near-constant time, making it suitable for real-world streaming graphs
- **💾 Space Efficient**: Dramatically reduces storage requirements while maintaining graph properties
- **🎯 No Setup Hassle**: Pre-configured environment eliminates dependency headaches

## 🎯 Use Cases

This tool is perfect for:

- **Social Network Analysis**: Compress billion-scale friendship or follower networks
- **Citation Networks**: Analyze academic paper relationships efficiently
- **Biological Networks**: Study protein interactions and metabolic pathways
- **Infrastructure Monitoring**: Track evolving network topologies
- **Knowledge Graphs**: Maintain compact representations of interconnected data

## 🏗️ How It Works

Our approach extends the PoliGraSS methodology with a three-step iterative process:

### 1️⃣ Group Partitioning
Uses **min-hashing** to group structurally similar nodes based on their neighborhoods.

### 2️⃣ Supernode Selection
Deploys a **shallow neural network** to intelligently merge nodes while preserving graph properties.

### 3️⃣ Edge Encoding
Efficiently updates superedges and maintains correction edges for perfect reconstruction.

### Dynamic Updates
When edges are added or removed, the algorithm updates only the affected parts of the summary—**no full recomputation needed!**

## Installation
## Installation

```bash
# Clone the repository
git clone https://github.com/AyushTyagi2/Fully_Dynamic_Graph_Summarization.git
cd Fully_Dynamic_Graph_Summarization
git clone https://github.com/AyushTyagi2/Fully_Dynamic_Graph_Summarization.git
cd Fully_Dynamic_Graph_Summarization

# Install dependencies
pip install -r requirements.txt
```
## Execution

```bash
#Execute the backend
uvicorn backend.api:app --reload

# Execute the Frontend(on the other terminal)
npm run dev
```

## Quick Start
## Quick Start

### Basic Usage

```python
import networkx as nx
from graph_summarizer import DynamicGraphSummarizer

# Load your graph
G = nx.read_edgelist("your_graph.txt")

# Initialize summarizer
summarizer = DynamicGraphSummarizer(
    counts=100,           # Max iterations
    group_size=50,        # Max group size
    hidden_size=64,       # Neural network hidden dimensions
    lr=0.01,             # Learning rate
    dropout=0.1,         # Dropout rate
    weight_decay=0.0001  # Weight decay
)

# Create initial summary
summary, corrections = summarizer.summarize(G)

# Dynamic updates
summarizer.add_edge(u, v)      # Add edge
summarizer.remove_edge(u, v)   # Remove edge

# Export results
summary.save("summary_graph.nx")
corrections.save("correction_edges.nx")
```

### Using the Interactive Tool

1. **Upload Your Dataset**: Load your graph in NetworkX format
2. **Configure Parameters**: Set hyperparameters for your specific use case
3. **Visualize**: Watch the summarization process in real-time
4. **Update Dynamically**: Add/remove edges and see instant updates
5. **Export**: Download your summary and correction edges

### 📋 File Naming Requirements

When uploading raw graph datasets, your files **must** contain specific keywords in their filenames for proper recognition:

- **Graph files**: Must contain `_graph` in the filename (e.g., `my_graph`, `data_graph`, `network_graph.pkl`)
- **Feature files**: Must contain `_feat` in the filename (e.g., `node_feat`, `features_feat`, `node_features_feat.pkl`)

**Example valid filenames:**
- `astro-ph_graph` (graph pickle file)
- `astro-ph_feat` (feature pickle file)

Both files are required for the summarization process to work. The upload handler will automatically rename them to `{dataset_id}_graph` and `{dataset_id}_feat` for processing.

## 🎛️ Hyperparameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `counts` | Maximum iterations for summarization | 20 |
| `group_size` | Maximum size of each node group | 2000 |
| `hidden_size1` | Neural network first hidden layer dimensions | 32 |
| `hidden_size2` | Neural network second hidden layer dimensions | 16 |
| `lr` | Learning rate | 0.0005 |
| `dropout` | Dropout rate for regularization | 0.0 |
| `weight_decay` | Weight decay for optimizer | 0.0 |
| `bad_counter` | Early stopping tolerance (iterations with no improvement) | 1 |

## 📧 Contact

For questions, suggestions, or collaborations:

- **Ayush Tyagi**: 2023csb1108@iitrpr.ac.in
- **Nitin Kumar**: 2023csb1141@iitrpr.ac.in
- **Harsh Rai**: 2023csb1345@iitrpr.ac.in
- **Parth Kulkarni**: 2023csb1142@iitrpr.ac.in
- **Dr. Manish Kumar**: manishk@iitrpr.ac.in
---

**⭐ If you find this tool useful, please star the repository!**
