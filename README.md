# Sample-Oriented Task-Driven Visualization App  

An interactive Dash web app inspired by the research paper *“Sample-Oriented Task-Driven Visualizations: Allowing Users to Make Better, More Confident Decisions.”*  

### Compare each bar to a fixed value that user chooses

An interactive data visualization app built with Dash.

<p align="center">
  <img src="assets/interactive_annotation.png" alt="App Screenshot" style="max-width: 60%; height: auto;">
</p>


This project demonstrates one of the interactive annotation ideas discussed in the paper — offering users a way to experiment with interactive annotations when it is difficult to make mathematical inferences from overlapping confidence intervals.

---

### 🔗 Live Demo  
👉 [View this demo app and try the idea in the paper yourself!](https://interactive-annotation-dash.onrender.com)

![Demo](assets/interactive_anno.gif)

---

### 🧠 Research Reference  
Paper: [Sample-Oriented Task-Driven Visualizations: Allowing Users to Make Better, More Confident Decisions](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf)  
Authors: [Nivan Ferreira, Danyel Fisher, Arnd Christian König]

---

### 🛠️ Tech Stack  
- CSS  
- Python 3  
- Plotly Dash  
- Pandas  
- Gunicorn

---

### 🚀 Local Development  
1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```  
2. Create and activate a virtual environment  
   - On macOS/Linux:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```  
   - On Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```  
3. Install the required dependencies  
   ```bash
   pip install -r requirements.txt
   ```  
4. Run the app locally  
   ```bash
   python app.py
   ```  
5. Open your browser and navigate to `http://127.0.0.1:8050` to view the app.

---

### 🤝 Collaboration & Contributions  

This app implements one of the innovative visualization ideas from the referenced research paper. I warmly invite collaborators interested in implementing other visualization concepts from the paper, such as dynamic bar-to-bar comparison or bar-to-range comparson, using Plotly Dash. Contributions, feature requests, and discussions are highly encouraged to foster an open and collaborative development environment. Feel free to open issues or submit pull requests to help expand this project.