import os
import subprocess
import re

# Sort all .dat files in the current directory according to the model number
dat_files = sorted([f for f in os.listdir('.') if f.endswith('.dat')],
                   key=lambda x: int(''.join(filter(str.isdigit, x))))

# The file that stores the accuracy of all models
output_file = 'accuracies.txt'

# Regular expression to match the string in the format "Average Accuracy: X.XXXX"
accuracy_pattern = re.compile(r"Average Accuracy: ([0-9]+\.[0-9]+)")

# Prepare to write to the file
with open(output_file, 'w') as f:
    f.write("Model Accuracy Results:\n")  # Write the title
    for model in dat_files:
        print(f"Starting execution for model: {model}")  # Print the model starting execution
        # Build the command
        command = f"python3 test.py -model {model}"
        # Execute the command and capture the output
        try:
            process = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            output = process.stdout
            # Use regular expression to find "Average Accuracy: X.XXXX"
            match = accuracy_pattern.search(output)
            if match:
                accuracy = match.group(1)  # Extract the numerical part
                # Write the accuracy to the file
                f.write(f"Model: {model}, Accuracy: {accuracy}\n")
                print(f"Finished execution for model: {model}, Accuracy: {accuracy}")  # Print completion message
            else:
                print(f"Accuracy not found for model: {model}")
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.strip()
            print(f"Error executing {command}: {error_message}")  # Print error message
            # Write error message to file
            f.write(f"Model: {model}, Error: {error_message}\n")

print(f"All accuracies have been written to {output_file}")