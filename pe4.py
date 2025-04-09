#Pair Exercise 4 with Mark Villamayorr 

import wikipedia
import time
import concurrent.futures
import os

def clean_filename(title):
    """Create a valid filename from a Wikipedia page title"""
    # Replace any characters that might cause issues in filenames
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_chars:
        title = title.replace(char, '_')
    return title

def write_references_to_file(title, references):
    """Write references to a text file named after the page title"""
    filename = clean_filename(title) + ".txt"
    with open(filename, 'w', encoding='utf-8') as file:
        for ref in references:
            file.write(ref + '\n')

def wiki_dl_and_save(topic):
    """Download Wikipedia page for a topic and save its references to a file"""
    try:
        # Get the Wikipedia page with auto_suggest=False
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = page.references
        
        # Write references to a file
        write_references_to_file(title, references)
        
        return f"Saved references for '{title}'"
    except Exception as e:
        return f"Error processing '{topic}': {str(e)}"

# Section A: Sequential download
def sequential_download():
    print("Starting sequential download...")
    start_time = time.perf_counter()
    
    # 1. Search for topics related to 'generative artificial intelligence'
    topics = wikipedia.search('generative artificial intelligence')
    
    # 2. Iterate over topics and save references
    for topic in topics:
        try:
            page = wikipedia.page(topic, auto_suggest=False)
            title = page.title
            references = page.references
            
            write_references_to_file(title, references)
            
            print(f"Saved references for '{title}'")
        except Exception as e:
            print(f"Error processing '{topic}': {str(e)}")
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    # 3. Print execution time
    print(f"Sequential download completed in {elapsed_time:.2f} seconds")
    return elapsed_time

# Section B: Concurrent download
def concurrent_download():
    print("\nStarting concurrent download...")
    start_time = time.perf_counter()
    
    # 1. Search for topics related to 'generative artificial intelligence'
    topics = wikipedia.search('generative artificial intelligence')
    
    # 3. Use ThreadPoolExecutor to execute the function concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(wiki_dl_and_save, topics))
    
    # Print results
    for result in results:
        print(result)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    # 4. Print execution time
    print(f"Concurrent download completed in {elapsed_time:.2f} seconds")
    return elapsed_time

if __name__ == "__main__":
    # Create a directory for output files if it doesn't exist
    os.makedirs("wikipedia_references", exist_ok=True)
    os.chdir("wikipedia_references")
    
    # Run both methods and compare times
    seq_time = sequential_download()
    conc_time = concurrent_download()
    
    # Compare the performance
    speedup = seq_time / conc_time if conc_time > 0 else 0
    print(f"\nPerformance comparison:")
    print(f"Sequential: {seq_time:.2f} seconds")
    print(f"Concurrent: {conc_time:.2f} seconds")
    print(f"Speedup: {speedup:.2f}x")
