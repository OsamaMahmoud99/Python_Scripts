import subprocess

try:
    from intelhex import IntelHex

except ImportError:
    subprocess.check_call(["pip", "install", "IntelHex"])



counter = 0

def search_pattern_in_hex_file(file_path, pattern):
    flag = 0
    global counter
    ih = IntelHex(file_path)
    #ih.loadhex(file_path)
    #pydict = ih.todict() 
    #print(hex(pydict[0])[2:])
 
    
    # Convert the pattern string to bytes
    pattern_bytes = bytes.fromhex(pattern)
   
    
    # Iterate over all addresses in the hex file
    for addr in ih.addresses():
       # Read the bytes at the current address
       #print(addr)
       #input("TEST")
       data = ih.tobinarray(start=addr, size=len(pattern_bytes))
       #print(data)
       i = 0
       flag = 0
        
        # Compare the read bytes with the pattern
       for i in range(len(pattern_bytes)):
        if data[i] != pattern_bytes[i]:
            flag = 1
            
           
       if flag == 0:
           print(f"Pattern found at address {addr}")
           counter = counter + 1;
           print(data)
           return True
    
   
   
    print("Pattern not found in the file")
    return False
   

counter_file_path = "counter.txt"  # Path to the file to save the counter value

def save_counter(counter_value):
    with open(counter_file_path, "w") as file:
        file.write(str(counter_value))
        
        
# Example usage
file_path = "SRAM.hex"
pattern_to_search = 'AA1715BB1715BB1715BB1715BB1715AA'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = 'C772BF8DBCE9D51274F6867C34234DC6'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = 'AA810BB810BB810BB810BB810BB810AA'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = '666666B586CE68F7D440F63D6CFE240678C8CF24F94C358C875CAA1D3F75A39A'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = '1000000000000000000000000000000000000000000000000000000000000001'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
print(counter);

# Example usage
file_path = "ITCM.hex"
pattern_to_search = 'AA1715BB1715BB1715BB1715BB1715AA'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = 'C772BF8DBCE9D51274F6867C34234DC6'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = 'AA810BB810BB810BB810BB810BB810AA'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = '666666B586CE68F7D440F63D6CFE240678C8CF24F94C358C875CAA1D3F75A39A'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
pattern_to_search = '1000000000000000000000000000000000000000000000000000000000000001'  # Example pattern to search
search_pattern_in_hex_file(file_path, pattern_to_search)
print(counter);

# Save the updated counter value
save_counter(counter)
print("Updated counter value saved.")