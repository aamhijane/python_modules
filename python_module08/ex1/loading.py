import sys
import importlib


def check_dependencies() -> bool:
    """Check if all required packages are installed."""
    required = {
        "pandas": ["pandas", "Data manipulation ready"],
        "requests": ["requests", "Network access ready"],
        "matplotlib": ["matplotlib", "Visualization ready"],
        "numpy": ["numpy", None],
    }

    all_ok = True

    print("Checking dependencies:")
    for module, package in required.items():
        try:
            mod = importlib.import_module(module)
            version = getattr(mod, "__version__", "unknown")
            name, description = package
            if description:
                print(f"[OK] {name} ({version}) - {description}")
            else:
                print(f"[OK] {name} ({version})")
        except ImportError:
            print(f"  [MISSING] {package[0]} - not installed!")
            all_ok = False

    return all_ok


def show_install_instructions() -> None:
    """Show how to install missing dependencies."""
    print("\nTo install missing dependencies, run:")
    print("  pip install -r requirements.txt")
    print("  OR")
    print("  poetry install")
    sys.exit(1)


def generate_matrix_data():
    """Generate 1000 rows of fake Matrix agent data."""
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    data = {
        "agent_id":     range(1000),
        "threat_level": np.random.randint(1, 100, 1000),
        "is_dangerous": np.random.choice([True, False], 1000),
        "agent_name":   ["Agent_" + str(i) for i in range(1000)],
    }
    return pd.DataFrame(data)


def analyze_data(df) -> dict:
    """Analyze the Matrix data and return basic statistics."""
    return {
        "total_agents":     len(df),
        "avg_threat":       round(df["threat_level"].mean(), 2),
        "high_threat_count": len(df[df["threat_level"] > 75]),
        "dangerous_count":  int(df["is_dangerous"].sum()),
    }


def generate_visualization(df) -> None:
    """Generate and save a visualization of the Matrix data."""
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Matrix Data Analysis", fontsize=16)

    # Chart 1 - Bar chart: threat level distribution
    axes[0].hist(df["threat_level"], bins=20,
                 color="green", edgecolor="black")
    axes[0].set_title("Threat Level Distribution")
    axes[0].set_xlabel("Threat Level")
    axes[0].set_ylabel("Count")

    # Chart 2 - Pie chart: dangerous vs safe agents
    dangerous = int(df["is_dangerous"].sum())
    safe = len(df) - dangerous
    axes[1].pie(
        [dangerous, safe],
        labels=["Dangerous", "Safe"],
        colors=["red", "green"],
        autopct="%1.1f%%"
    )
    axes[1].set_title("Dangerous vs Safe Agents")

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Main entry point for the loading program."""
    try:
        print("LOADING STATUS: Loading programs...\n")

        # check dependencies
        if not check_dependencies():
            show_install_instructions()

        # generate data & chart
        df = generate_matrix_data()
        print("\nAnalyzing Matrix data...")
        print(f"Processing {len(df)} data points...")
        print("Generating visualization...")

        # generate visualization & save it
        print("\nAnalysis complete!")
        generate_visualization(df)

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
