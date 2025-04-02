
# None selected

# Skip to content
# Using Bucknell University Mail with screen readers

# Conversations

# Important
 
# 1–25 of 3,678
 

# Starred
 
# 1–10 of 400
 

# Unread
 
# 1–25 of 7,946
 
# Vighanesh Gaund via.
# Duy, start a conversation with your new connection, Vighanesh
# See Vighanesh's connections, experience, and more ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏
 
# 1:04 AM
# Z. Kevin Wu via Lin.
# Duy, start a conversation with your new connection, Z. Kevin
# See Z. Kevin's connections, experience, and more ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏
 
# 11:04 PM

# Everything else
 
# 1–25 of 12,692
 
# CSCI 311 Project
# Inbox

# Leo McMenimen
# Attachments
# Apr 1, 2025, 11:50 PM (2 hours ago)
# to Molly, me

# Hey guys,


# I spent some time making a GUI, readme, and completing my algorithm. If you have Python3 installed on your laptop you can run the GUI.py and it will run with the code I have so far. The only algorithm that will work so far will be edit because that is what I made. If you want to see what everything is looking like so far feel free to check it out. I attached all the files needed to run it to this email.



# I read in the files, however If needed I can mess around and make the GUI work with whatever you guys need


# Best,
# Leo McMenimen
#  6 Attachments
#   •  Scanned by Gmail

# Molly Yoder
# 12:23 AM (1 hour ago)
# to Leo, me

# Leo,

# Thanks for sending this over! I haven't written anything to read the file so I'm happy using your file handler to establish the sequences. I've finished writing my algorithm, but it's a little messy right now and I haven't actually tested it yet so if I can get to that before we meet tomorrow I will. I've also begun to write a bit about my algorithm in the latex file, but nothing too crazy at the moment.

# Thanks,
# Molly


# Duy Le <dl039@bucknell.edu>
# 12:57 AM (1 hour ago)
# to Molly

# cool, I writing my algoritm down now

# Le Duy


# Duy Le
# 1:36 AM (22 minutes ago)
# to Molly

# I will make a github for this so we can commit and push our code.

# --
# Kind regards,

# Duy Le
# Computer Engineering '27, Bucknell University

# 2723059910  |  dl039@bucknell.edu

# Create your own email signature
 
# __tpx__
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import file_handler  # Make sure this is correctly imported
# import algorithms    # Ensure the algorithms are correctly imported

# class DNASequenceAlignmentApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DNA Sequence Alignment")
        
#         # Labels and buttons
#         self.query_file_label = tk.Label(root, text="Select Database File:")
#         self.query_file_label.pack()

#         self.query_file_button = tk.Button(root, text="Browse", command=self.load_query_file)
#         self.query_file_button.pack()

#         self.database_file_label = tk.Label(root, text="Select Query File:")
#         self.database_file_label.pack()

#         self.database_file_button = tk.Button(root, text="Browse", command=self.load_database_file)
#         self.database_file_button.pack()

#         self.algorithm_label = tk.Label(root, text="Select Alignment Algorithm:")
#         self.algorithm_label.pack()

#         self.algorithm_menu = tk.StringVar()
#         self.algorithm_menu.set("Longest Common Substring")  # Default to "Longest Common Substring"
#         self.algorithm_dropdown = tk.OptionMenu(
#             root, self.algorithm_menu, 
#             "Longest Common Substring", "LCS", "Edit Distance"
#         )
#         self.algorithm_dropdown.pack()

#         self.run_button = tk.Button(root, text="Run Alignment", command=self.run_alignment)
#         self.run_button.pack()

#         self.result_label = tk.Label(root, text="Most Similar Sequence:")
#         self.result_label.pack()

#         self.result_text = tk.Text(root, height=4, width=50)
#         self.result_text.pack()

#     def load_query_file(self):
#         """Load the database file containing sequences."""
#         self.query_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#         if self.query_file:
#             self.query_file_label.config(text=f"Database File: {self.query_file}")

#     def load_database_file(self):
#         """Load the query file containing the query sequence."""
#         self.database_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#         if self.database_file:
#             self.database_file_label.config(text=f"Query File: {self.database_file}")

#     def run_alignment(self):
#         """Run the alignment algorithm based on user selection."""
#         try:
#             # Load sequences from files
#             database_sequences = file_handler.load_fasta(self.query_file)  # Load the database
#             query_sequence = file_handler.load_fasta(self.database_file)[0][1]  # Load the query sequence

#             # Get selected algorithm
#             algorithm = self.algorithm_menu.get()

#             # Select alignment algorithm
#             if algorithm == "Longest Common Substring":
#                 best_match = algorithms.longest_common_substring(query_sequence, database_sequences)
#             elif algorithm == "LCS":
#                 best_match = algorithms.lcs(query_sequence, database_sequences)
#             elif algorithm == "Edit Distance":
#                 best_match = algorithms.edit_distance(query_sequence, database_sequences)

#             # Display the result
#             self.result_text.delete(1.0, tk.END)  # Clear previous result
#             self.result_text.insert(tk.END, f"Header: {best_match[0]}\nSequence: {best_match[1]}")
        
#         except Exception as e:
#             # Show error if something goes wrong
#             messagebox.showerror("Error", f"An error occurred: {e}")

# # Main execution
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DNASequenceAlignmentApp(root)
#     root.mainloop()


