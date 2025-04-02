import tkinter as tk
from tkinter import filedialog, messagebox
import file_handler  # Make sure this is correctly imported
import algorithms    # Ensure the algorithms are correctly imported

class DNASequenceAlignmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Sequence Alignment")
        
        # Labels and buttons
        self.query_file_label = tk.Label(root, text="Select Database File:")
        self.query_file_label.pack()

        self.query_file_button = tk.Button(root, text="Browse", command=self.load_query_file)
        self.query_file_button.pack()

        self.database_file_label = tk.Label(root, text="Select Query File:")
        self.database_file_label.pack()

        self.database_file_button = tk.Button(root, text="Browse", command=self.load_database_file)
        self.database_file_button.pack()

        self.algorithm_label = tk.Label(root, text="Select Alignment Algorithm:")
        self.algorithm_label.pack()

        self.algorithm_menu = tk.StringVar()
        self.algorithm_menu.set("Longest Common Substring")  # Default to "Longest Common Substring"
        self.algorithm_dropdown = tk.OptionMenu(
            root, self.algorithm_menu, 
            "Longest Common Substring", "LCS", "Edit Distance"
        )
        self.algorithm_dropdown.pack()

        self.run_button = tk.Button(root, text="Run Alignment", command=self.run_alignment)
        self.run_button.pack()

        self.result_label = tk.Label(root, text="Most Similar Sequence:")
        self.result_label.pack()

        self.result_text = tk.Text(root, height=4, width=50)
        self.result_text.pack()

    def load_query_file(self):
        """Load the database file containing sequences."""
        self.query_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.query_file:
            self.query_file_label.config(text=f"Database File: {self.query_file}")

    def load_database_file(self):
        """Load the query file containing the query sequence."""
        self.database_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.database_file:
            self.database_file_label.config(text=f"Query File: {self.database_file}")

    def run_alignment(self):
        """Run the alignment algorithm based on user selection."""
        try:
            # Load sequences from files
            database_sequences = file_handler.load_fasta(self.query_file)  # Load the database
            query_sequence = file_handler.load_fasta(self.database_file)[0][1]  # Load the query sequence

            # Get selected algorithm
            algorithm = self.algorithm_menu.get()

            # Select alignment algorithm
            if algorithm == "Longest Common Substring":
                best_match = algorithms.longest_common_substring(query_sequence, database_sequences)
            elif algorithm == "LCS":
                best_match = algorithms.lcs(query_sequence, database_sequences)
            elif algorithm == "Edit Distance":
                best_match = algorithms.edit_distance(query_sequence, database_sequences)

            # Display the result
            self.result_text.delete(1.0, tk.END)  # Clear previous result
            self.result_text.insert(tk.END, f"Header: {best_match[0]}\nSequence: {best_match[1]}")
        
        except Exception as e:
            # Show error if something goes wrong
            messagebox.showerror("Error", f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = DNASequenceAlignmentApp(root)
    root.mainloop()


