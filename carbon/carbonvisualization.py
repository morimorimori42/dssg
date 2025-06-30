"""
bar chart creation for results
"""
import matplotlib.pyplot as plt


def create_co2_visualization(final_emissions, target):
    # Extract disassembly directions and emissions from the final_emissions data
    d_dirs = [emission.d_dir for emission in final_emissions]
    total_emissions = [emission.result.total for emission in final_emissions]

    # Create the bar plot with a specific hatch pattern (e.g., dots)
    plt.figure(figsize=(8, 6))
    bars = plt.bar(d_dirs, total_emissions, color='white', edgecolor='black', hatch='...')

    plt.xlabel('Disassembly Direction')
    plt.ylabel('Total Emissions (kgCO2e)')
    plt.title(f'Total Emissions for Target Component {target}')
    plt.xticks(d_dirs)

    # Add grid lines
    plt.grid(axis='y', alpha=0.5, linestyle='--')

    # Add text labels to the bars
    for bar, val in zip(bars, total_emissions):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_y() + bar.get_height(),
                 f'{val:.2f}',
                 ha='center', va='bottom', fontsize=10)

    # Save the plot as a PDF
    plt.savefig(f"co2_visualization_target_{target}.pdf")
    plt.close()



