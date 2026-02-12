import streamlit as st
import random
import matplotlib.pyplot as plt

st.title("🪙 Monte Carlo Coin Toss Simulator")

trials = st.slider("Number of Trials", 100, 100000, 5000)
coins_per_trial = st.slider("Coins per Trial", 1, 20, 1)
bias = st.slider("Probability of Heads (Bias)", 0.0, 1.0, 0.5)

if st.button("Run Simulation"):
    head_counts = 0
    tail_counts = 0

    for _ in range(trials):
        for _ in range(coins_per_trial):
            if random.random() < bias:
                head_counts += 1
            else:
                tail_counts += 1

    total_flips = trials * coins_per_trial

    prob_heads = head_counts / total_flips
    prob_tails = tail_counts / total_flips

    pct_heads = prob_heads * 100
    pct_tails = prob_tails * 100

    st.write("### Results")
    st.write(f"Heads Probability: {prob_heads:.4f} ({pct_heads:.2f}%)")
    st.write(f"Tails Probability: {prob_tails:.4f} ({pct_tails:.2f}%)")

    fig, ax = plt.subplots()
    ax.bar(["Heads", "Tails"], [pct_heads, pct_tails])
    ax.set_ylabel("Percentage (%)")
    ax.set_title("Coin Toss Distribution")
    st.pyplot(fig)
