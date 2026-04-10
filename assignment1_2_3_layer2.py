import tkinter as tk

# Execution Key
EXECUTION_KEY = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

# Global variable for Assignment 2
stored_value = ""

# ---------------- Assignment 1 ----------------
def assignment1():
    output.set(
        "Assignment 1: Exploring Layer 2 – Testnet\n\n"
        "Contract Deployed on Layer 2 (Polygon Mumbai)\n\n"
        f"Execution Key:\n{EXECUTION_KEY}\n\n"
        "Gas Fee: LOW\n"
        "Transaction Speed: FAST\n"
        "Status: Success ✅"
    )

# ---------------- Assignment 2 ----------------
def set_value():
    global stored_value
    stored_value = entry.get()
    output.set(
        "Assignment 2: Layer 2 Interaction\n\n"
        f"Value '{stored_value}' stored successfully!\n"
        "Gas Fee: LOW\n"
        "Transaction Time: FAST\n"
        "Status: Stored ✅"
    )

def get_value():
    output.set(
        "Assignment 2: Layer 2 Interaction\n\n"
        f"Stored Value: {stored_value}\n"
        "Retrieved Successfully ✅"
    )

# ---------------- Assignment 3 ----------------
def assignment3():
    output.set(
        "Assignment 3: Layer 2 Scaling\n\n"
        "Layer 1 (Ethereum Mainnet):\n"
        "Gas Fee: HIGH ❌\n"
        "Transaction Speed: SLOW ❌\n\n"
        "Layer 2 (Arbitrum Sepolia / Polygon Mumbai):\n"
        "Gas Fee: LOW ✅\n"
        "Transaction Speed: FAST ✅\n\n"
        "Conclusion:\nLayer 2 provides better scalability and efficiency."
    )

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Layer 2 Blockchain Assignments")
root.geometry("600x500")

# Title
tk.Label(root, text="Layer 2 Blockchain Simulation", font=("Arial", 16, "bold")).pack(pady=10)

# Assignment 1 Button
tk.Button(root, text="Run Assignment 1 (Deploy)", command=assignment1, bg="green", fg="white").pack(pady=5)

# Assignment 2 Section
tk.Label(root, text="Assignment 2 (Set/Get Value)").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Set Value", command=set_value, bg="blue", fg="white").pack(pady=3)
tk.Button(root, text="Get Value", command=get_value, bg="purple", fg="white").pack(pady=3)

# Assignment 3 Button
tk.Button(root, text="Run Assignment 3 (Comparison)", command=assignment3, bg="orange", fg="white").pack(pady=10)

# Output Area
output = tk.StringVar()
tk.Label(root, textvariable=output, wraplength=550, justify="left").pack(pady=20)

# Run App
root.mainloop()