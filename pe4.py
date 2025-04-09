# Pair Exercise 4 with Jade Sleiman and Mark Villamayor
# This program demonstrates sequential and concurrent downloading of Wikipedia content

# Import required libraries
import wikipedia
import time
import concurrent.futures

# Section A: Sequentially download wikipedia content
def sequential_download():
    # A.1. Use the wikipedia.search method to return a list of topics related to 'generative artificial intelligence'
    print("Starting sequential download...")
    topics = wikipedia.search('generative artificial intelligence')
    
    # Record start time for performance measurement
    start_time = time.perf_counter()
    
    # A.2. Iterate over the topics returned in #1 above using a for loop
    for topic in topics:
        try:
            # Assign the page contents to a variable named page using the wikipedia.page method
            # Using auto_suggest=False to get exact matches
            page = wikipedia.page(topic, auto_suggest=False)
            
            # Assign the page title to a variable
            title = page.title
            
            # Retrieve the references for that page
            references = page.references
            
            # Create a filename based on the page title
            filename = f"{title}.txt"
            
            # Write the references to a .txt file with each reference on its own line
            with open(filename, 'w', encoding='utf-8') as file:
                # Join the references with newlines to ensure each is on its own line
                file.write('\n'.join(references))
                
            print(f"Sequential: Saved references for '{title}'")
        except Exception as e:
            print(f"Error processing topic '{topic}': {e}")
    
    # A.3. Print to the console the amount of time it took the above code to execute
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Sequential download completed in {execution_time:.4f} seconds")
    return execution_time

# Section B: Concurrently download wikipedia content
# B.2. Create a function that retrieves and saves Wikipedia content
def wiki_dl_and_save(topic):
    try:
        # Retrieve the wikipedia page for the topic
        page = wikipedia.page(topic, auto_suggest=False)
        
        # Get the title and the references for the topic
        title = page.title
        references = page.references
        
        # Create a .txt file where the name of the file is the title of the topic
        filename = f"{title}_concurrent.txt"
        
        # Write the references to the file with each reference on its own line
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(references))
            
        print(f"Concurrent: Saved references for '{title}'")
        return title
    except Exception as e:
        print(f"Error processing topic '{topic}': {e}")
        return None

def concurrent_download():
    # B.1. Use the wikipedia.search method to return a list of topics
    print("\nStarting concurrent download...")
    topics = wikipedia.search('generative artificial intelligence')
    
    # Record start time for performance measurement
    start_time = time.perf_counter()
    
    # B.3. Use ThreadPoolExecutor to execute concurrently the function defined in step 2
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Use the map method to apply the function to each topic in the list
        # This will execute the function concurrently for all topics
        results = list(executor.map(wiki_dl_and_save, topics))
    
    # B.4. Print to the console the amount of time it took the code to execute
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Concurrent download completed in {execution_time:.4f} seconds")
    return execution_time

# Main execution
if __name__ == "__main__":
    # Run sequential download
    seq_time = sequential_download()
    
    # Run concurrent download
    conc_time = concurrent_download()
    
    # Compare the performance
    speedup = seq_time / conc_time if conc_time > 0 else 0
    print(f"\nPerformance comparison:")
    print(f"Sequential execution: {seq_time:.4f} seconds")
    print(f"Concurrent execution: {conc_time:.4f} seconds")
    print(f"Speedup factor: {speedup:.2f}x")
