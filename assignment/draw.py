import json
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__)) 
    relative_path = os.path.join(current_dir, file_path)  
    with open(relative_path, 'r') as f:
        data = json.load(f)
    return data

def plot_data(data):
    plt.clf()  
    plt.close()  
    
    fig, ax = plt.subplots(figsize=(12, 8))

    custom_colors = [
        '#F20C0C','#F4563D','#F24B0C','#F4883D','#F2890C','#F4BA3D','#F2C80C',
        '#F4EC3D','#DDF20C','#CBF43D','#9EF20C','#99F43D','#60F20C','#66F43D',
        '#21F20C','#3DF445','#0CF236','#3DF477','#0CF275','#3DF4A9','#0CF2B3',
        '#3DF4DB','#0CF2F2','#3DDBF4','#0CB3F2','#3DA9F4','#0C75F2','#3D77F4',
        '#0C36F2','#3D45F4','#210CF2','#663DF4','#600CF2','#993DF4','#9E0CF2',
        '#CB3DF4','#DD0CF2','#F43DEC','#F20CC8','#F43DBA','#F20C89','#F43D88',
        '#F20C4B','#F43D56'
    ]

    for idx, (country, info) in enumerate(data.items()):
        color = custom_colors[idx] if idx < len(custom_colors) else custom_colors[-1]
        year_value_pairs = info["year_value_pairs"]
        years = [pair["year"] for pair in year_value_pairs]
        values = [pair["value"] for pair in year_value_pairs]
        
        filtered_years = [year for year, value in zip(years, values) if value is not None]
        filtered_values = [value for value in values if value is not None]
        
        if filtered_years and filtered_values:
            ax.plot(filtered_years, filtered_values, label=country, color=color)
            print(f"Plotting {country} with color {color}")  

    ax.set_xlabel('Year')
    plt.xlim(1985, 2021)
    ax.set_ylabel('Value')
    plt.ylim(100000, 8000000)
    
    ax.set_title('The Total of GHG in Party Data Over Years')
    
    if ax.lines:
        ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1))
        plt.subplots_adjust(top=0.96)
        plt.subplots_adjust(right=0.767)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data_file = 'dist/data.json'
    data = load_data(data_file)
    plot_data(data)