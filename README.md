# Carnot Efficiency Calculator

An interactive web application demonstrating the Second Law of Thermodynamics through the Carnot cycle, for my PHYC-202 physics project!

## Project Overview

This Streamlit web app helps visualize and understand:
- **Carnot Efficiency**: The theoretical maximum efficiency of any heat engine
- **Formula**: η = 1 - (T_cold / T_hot)
- **Real-World Applications**: Comparison of ideal vs actual engine efficiencies

## Installation

```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment

### Deploy to Streamlit Community Cloud (Free)

This app is ready to be deployed on [Streamlit Community Cloud](https://share.streamlit.io/), which provides free hosting for public Streamlit apps.

#### Prerequisites
- A GitHub account
- Your project pushed to a public GitHub repository

#### Deployment Steps

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Carnot Efficiency Calculator"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Sign up for Streamlit Community Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with your GitHub account
   - Authorize Streamlit to access your repositories

3. **Deploy your app:**
   - Click "New app" in the Streamlit Community Cloud dashboard
   - Select your repository from the dropdown
   - Choose the branch (usually `main` or `master`)
   - Set the main file path to `app.py`
   - Click "Deploy"

4. **Your app will be live!**
   - Streamlit Community Cloud will automatically build and deploy your app
   - You'll get a URL like: `https://YOUR_APP_NAME.streamlit.app`
   - The app will automatically redeploy whenever you push changes to your GitHub repository

#### Updating Your Deployed App

Simply push changes to your GitHub repository, and Streamlit Community Cloud will automatically redeploy:
```bash
git add .
git commit -m "Update app"
git push
```

The deployment typically takes 1-2 minutes to complete.

## Features

### Core Functionality
- ✅ Interactive temperature sliders (Kelvin/Celsius)
- ✅ Real-time efficiency calculation with live metrics
- ✅ Color-coded efficiency interpretation (Excellent/Good/Moderate/Low ranges)
- ✅ Real-world engine comparisons with visual progress bars
- ✅ CSV export functionality

### Enhanced Visualizations
- ✅ **P-V Diagram**: Interactive visualization with process annotations
  - Shows all four Carnot cycle processes with labels
  - Highlights heat absorption and rejection
  - Educational arrows explaining each step
- ✅ **Energy Flow Diagram**: Sankey diagram showing energy conversion
  - Visual representation of useful work vs waste heat
  - Adjustable energy input with helpful tooltips
- ✅ **Creator's Note**: Comprehensive explanation of the Second Law

### Real-World Context
- ✅ Detailed comparison tables for car engines, power plants, and diesel engines
- ✅ Shows Carnot limit vs actual efficiency percentages
- ✅ Displays how close real engines are to theoretical maximum

## Physics Concept

The Carnot efficiency demonstrates why 100% efficient engines are physically impossible. 
Even an ideal engine must reject waste heat to the cold reservoir, limited by the Second Law of Thermodynamics.

## Summary

This app provides an intuitive, interactive way to explore the fundamental limits of heat engine efficiency, making complex thermodynamic concepts accessible through real-time calculations and beautiful visualizations.

---

**Assignment**: Physics 202 - Creative Application Project