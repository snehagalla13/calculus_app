# 📚 UNC Calculus 1 Practice App

A Python-based interactive calculus practice application featuring randomly generated problems with instant feedback and helpful learning resources. Built with Streamlit.

![UNC Colors](https://img.shields.io/badge/UNC-Carolina%20Blue-7BAFD4)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)

## 🎯 Features

- **Randomly Generated Problems**: Practice different calculus concepts with new problems each time
- **Multiple Problem Types**:
  - Power Rule Derivatives
  - Sum Rule & Power Rule Combined
  - Chain Rule
  - Basic Limits
- **Beautiful LaTeX Rendering**: Mathematical equations displayed professionally
- **Instant Feedback**: Know immediately if your answer is correct
- **Learning Resources**: Get helpful links to Khan Academy and other tutorials when you need extra help
- **Score Tracking**: Monitor your progress with a running score counter

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/snehagalla13/calculus_app.git
   cd calculus_app
   ```

2. **Install required packages**
   ```bash
   pip install streamlit
   ```

## 💻 Usage

1. **Run the application**
   ```bash
   streamlit run calculus_app.py
   ```

2. **The app will automatically open in your default web browser** at `http://localhost:8501`

3. **Start practicing!**
   - Read the calculus problem displayed
   - Enter your answer in the text box
   - Use `^` for exponents (e.g., `6x^2` for 6x²)
   - Click "Check Answer" to see if you're correct
   - If incorrect, review the correct answer and click the resource links to learn more
   - Click "Next Problem" to continue practicing

## 📝 Answer Format Guidelines

- **Derivatives**: Write answers like `12x^3` or `6x^2 + 4x`
- **Limits**: Enter just the numeric value like `15`
- **Exponents**: Always use `^` symbol (e.g., `x^2` not `x2`)
- **No spaces** are required but acceptable

## 🎓 Problem Types Explained

### Power Rule
Find derivatives of polynomial terms like f(x) = 5x³

**Rule**: d/dx(xⁿ) = n·xⁿ⁻¹

### Sum Rule
Find derivatives of sums of polynomial terms like g(x) = 3x⁴ + 2x²

**Rule**: Take the derivative of each term separately

### Chain Rule
Find derivatives of composite functions like h(x) = (3x)⁴

**Rule**: Derivative of outer function × derivative of inner function

### Basic Limits
Evaluate limits by substitution like lim(x→2) (3x + 5)

**Rule**: Substitute the value directly for continuous functions

## 🛠️ Technical Details

### Built With
- **Python** - Core programming language
- **Streamlit** - Web application framework
- **LaTeX** - Mathematical equation rendering

### Project Structure
```
calculus_app/
├── calculus_app.py    # Main application file
└── README.md          # Documentation
```

## ⚠️ Known Issues

Currently tracking the following issues:

- **Issue #1**: Strict Validation 
  - *Description*: A few answers are marked as wrong even though they are right due to formatting issues
  - *Status*: In progress / Under investigation

If you encounter any bugs or issues not listed here, please [open an issue](https://github.com/snehagalla13/calculus_app/issues) on GitHub.

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

Created by Sneha Galla

## 🙏 Acknowledgments

- Khan Academy for excellent calculus resources
- Paul's Online Math Notes for comprehensive tutorials

## 📧 Contact

Questions or suggestions? Feel free to open an issue or reach out!

---
