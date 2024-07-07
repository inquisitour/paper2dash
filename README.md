# 🧠 paper2dash

<p align="center">
  <img src="./assets/logo.png" alt="Project Logo" width="400" height="200">
</p>

## 🌟 Introduction

Welcome to paper2dash! This interactive web application is designed to present key concepts and findings from cutting-edge research in the field of nonmonotonic reasoning and logic programming.

Built with Dash and Plotly, this dashboard offers an engaging and user-friendly interface to explore various aspects of equilibrium logic, including background information, encodings, complexity analysis, and more.

## 🚀 Features

- 📊 Interactive visualizations of complexity results with adaptive color schemes
- 🔍 Comprehensive search functionality across all content
- 🌓 Dark mode toggle for improved readability, with automatic chart adjustments
- 📱 Responsive design for desktop and mobile devices
- 📚 In-depth exploration of 11 key topics in equilibrium logic and ASP
- 🔗 Extensive bibliography with over 150 searchable references
- ♿ Improved accessibility with ARIA attributes for better screen reader support

## 🛠️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/inquisitour/paper2dash.git
   ```

2. Navigate to the project directory:
   ```
   cd paper2dash
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## 🖥️ Usage

1. Run the Dash app:
   ```
   python app.py
   ```

2. Open a web browser and go to `http://localhost:8050` to view the dashboard.

3. Navigate through the different sections using the sidebar menu.

4. Use the search functionality to find specific topics or references.

5. Toggle dark mode for a different visual experience. Charts will automatically adjust to maintain readability.

## 🗂️ Project Structure

```
paper2dash/
│
├── app.py                 # Main application file
├── layout.py              # Layout definition
├── callbacks.py           # Callback functions
├── styles.py              # Style definitions
│
├── components/            # Reusable components
│   ├── __init__.py
│   ├── sidebar.py
│   ├── header.py
│   └── content_area.py
│
├── assets/                # Static assets
│   ├── custom.css
│   └── logo.png
│
├── data/                  # Data files
│   └── paper_data.json
│
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── data_processing.py
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 📚 Content Sections

1. **Overview**: Introduction to equilibrium logic and its significance
2. **Background**: Foundational concepts in propositional logic and ASP
3. **Encodings**: Various encodings for equilibrium logic and ASP
4. **Complexity**: Analysis of computational complexity for key reasoning tasks
5. **Equivalence**: Exploration of different notions of equivalence in logic programs
6. **Circumscription**: Relationship between equilibrium logic and circumscription
7. **Strong Negation**: Integration of strong negation in equilibrium logic
8. **Related Works**: Connections to other research in nonmonotonic reasoning
9. **Concluding Remarks**: Summary of main contributions and future directions
10. **Appendix**: Additional proofs and technical details
11. **References**: Comprehensive bibliography with over 150 entries

## 🔍 Search Functionality

The dashboard includes a powerful search feature that allows users to find specific information across all content sections and the extensive bibliography. Simply enter your search terms in the search bar to get instant results.

## 🌙 Dark Mode

Toggle between light and dark modes for a comfortable viewing experience in any environment. The dark mode feature is especially useful for reducing eye strain during extended use. Charts and visualizations automatically adjust their color schemes to maintain readability in both modes.

## 📊 Interactive Visualizations

Explore complex concepts through interactive charts and graphs. The complexity analysis section features dynamic charts that can be toggled between bar and radar visualizations for a deeper understanding of computational complexity in equilibrium logic and ASP. Charts adapt to the current color mode for optimal viewing.

## ♿ Accessibility

The dashboard now includes improved accessibility features, such as ARIA attributes for better screen reader support. This ensures that the content is more accessible to users with disabilities.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the dashboard or add new features, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/awesome-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some awesome feature'`)
5. Push to the branch (`git push origin feature/awesome-feature`)
6. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- This dashboard is based on the paper "Characterising Equilibrium Logic and Nested Logic Programs: Reductions and Complexity"
- Authors : DAVID PEARCE, HANS TOMPITS, STEFAN WOLTRAN
- Dash and Plotly for providing the framework and visualization tools
- The open-source community for various libraries and resources used in this project

## 📞 Contact

For any questions or feedback, please open an issue on this repository or contact [Pratik Deshmukh] at [deshmukhpratik931@gmail.com].

---

Happy exploring the world of Equilibrium Logic and Answer Set Programming! 🚀🧠
