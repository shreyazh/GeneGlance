import streamlit as st
from Bio.Seq import Seq

# Title
st.title("DNA Sequence Analysis Tool")

# Sidebar Navigation
page = st.sidebar.radio(
    "Select an Analysis Tool:",
    ("Reverse Complement", "GC Content Calculator", "Mutation Finder", "Motif Finder")
)

# Input DNA Sequence
st.sidebar.header("Input DNA Sequence")
sequence_input = st.sidebar.text_area("Paste your DNA sequence here (A, T, G, C only):")

if sequence_input:
    # Clean the input
    sequence_input = sequence_input.upper().replace(" ", "").replace("\n", "")
    valid_characters = set("ATGC")
    if not set(sequence_input).issubset(valid_characters):
        st.error("Invalid DNA sequence. Please enter only A, T, G, or C.")
    else:
        st.success("Valid DNA sequence provided!")
        dna_seq = Seq(sequence_input)

        # Reverse Complement Page
        if page == "Reverse Complement":
            st.subheader("Reverse Complement")
            st.text(str(dna_seq.reverse_complement()))

        # GC Content Calculator Page
        elif page == "GC Content Calculator":
            st.subheader("GC Content Calculator")
            gc_content = 100 * (dna_seq.count("G") + dna_seq.count("C")) / len(dna_seq)
            st.text(f"GC Content: {gc_content:.2f}%")

        # Mutation Finder Page
        elif page == "Mutation Finder":
            st.subheader("Mutation Finder")
            st.text("Enter a mutated sequence to compare:")
            mutated_sequence = st.text_input("Mutated DNA Sequence:")
            if mutated_sequence:
                if len(mutated_sequence) != len(sequence_input):
                    st.error("Mutated sequence length must match the original sequence.")
                else:
                    differences = [
                        (i + 1, original, mutated)
                        for i, (original, mutated) in enumerate(zip(sequence_input, mutated_sequence))
                        if original != mutated
                    ]
                    if differences:
                        st.write("Mutations found at the following positions:")
                        for diff in differences:
                            st.text(f"Position {diff[0]}: Original = {diff[1]}, Mutated = {diff[2]}")
                    else:
                        st.text("No mutations detected.")

        # Motif Finder Page
        elif page == "Motif Finder":
            st.subheader("Motif Finder")
            motif = st.text_input("Enter a motif to search for:")
            if motif:
                motif = motif.upper()
                positions = [i + 1 for i in range(len(sequence_input) - len(motif) + 1) if sequence_input[i:i + len(motif)] == motif]
                if positions:
                    st.write(f"Motif '{motif}' found at positions: {positions}")
                else:
                    st.text(f"Motif '{motif}' not found in the sequence.")
