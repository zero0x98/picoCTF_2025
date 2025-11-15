from pwn import remote
import binascii

# Conversion functions
def binary_to_ascii(binary_input):
    try:
        binary_cleaned = ''.join(binary_input.split(' '))
        n = int(binary_cleaned, 2)
        return binascii.unhexlify('%x' % n).decode('utf-8')
    except:
        return None

def octal_to_ascii(octal_input):
    try:
        octal_values = octal_input.split(' ')[1:]
        return ''.join(chr(int(octal_char, 8)) for octal_char in octal_values)
    except:
        return None

def hex_to_ascii(hex_input):
    try:
        return bytes.fromhex(hex_input).decode('utf-8')
    except:
        return None

def decode_message(encoded_message):
    decoders = [
        ("binary", binary_to_ascii),
        ("octal", octal_to_ascii),
        ("hexadecimal", hex_to_ascii),
    ]
    valid_result = None

    for name, decoder in decoders:
        result = decoder(encoded_message)
        if result and result.isprintable():
            valid_result = (name, result)
            break  # Exit once a valid decoding is found

    if valid_result:
        print(f"Detected {valid_result[0]} input")
        return valid_result[1]
    
    else:
        print("Error: Failed to decode the message")
        exit(0)

# Automate the process
def connect_to_server(host, port):
    print(f"Connecting to {host}:{port}...")
    conn = remote(host, port)
    attempt = 0
    while True:
        try:
            # Receive the server's message
            message = conn.recvline().decode('utf-8').strip()

            # Look for the specific line that starts with "Please give the " or "Please give me the " - necessary for the 2nd and 3rd convertion challenge
            if "Please give the " in message or "Please give me the " in message:
                print("\nAttempt", attempt,"")
                print(f"Server: {message}")
                encoded_message = ""
                if "Please give the " in message:
                    encoded_message = message.split("Please give the ")[1].split(" as a word.")[0]
                    print(f"Encoded message to decode: {encoded_message}")
                elif "Please give me the " in message: 
                    encoded_message = message.split("Please give me the ")[1].split(" as a word.")[0]
                    print(f"Encoded message to decode: {encoded_message}")
                # Determine the base of the input
                response = decode_message(encoded_message)
                if response:
                    print(f"Sending response: {response}")
                    conn.sendline(response.encode('utf-8'))
                else:
                    print("No valid decoding found. Exiting.")
                    break
            elif "Flag:" in message:
                print("\nChallenge Solved!!!")
                print(f"{message}\n")
                break
            else:
                continue
        except EOFError:
            print("\nBye bye - server closed")
            break
        attempt+=1

    conn.close()
    print("Connection closed.")

# Main function
def main():
    host = "jupiter.challenges.picoctf.org"
    port = 29956
    connect_to_server(host, port)

if __name__ == "__main__":
    main()
