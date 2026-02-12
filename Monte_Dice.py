import streamlit as st
import random
import matplotlib.pyplot as plt

st.title("🎲 Monte Carlo Dice Simulator")

trials = st.slider("Number of trials", 100,100000,5000)
dice_count = st.slider("Number of dice", 1,10,2)

if st.button("Run Simulator"):
    results = {}
    
    for _ in range(trials):
        total = sum(random.randint(1,6) for _ in range(dice_count))
        results[total]=results.get(total,0) +1
            
    sums = sorted(results.keys())
    probs = [results[s]/trials for s in sums]
    
    percentages = [p * 100 for p in probs]
    
    st.write("### Probability Distribution")
    fig,ax = plt.subplots()
    ax.bar(sums,probs)
    st.pyplot(fig)
    for s, p, pct in zip(sums, probs, percentages): st.write(f"Sum {s}: Probability = {p:.4f}, Percentage = {pct:.2f}%")