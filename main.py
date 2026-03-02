# Updated main.py

# Import necessary libraries
import sys
try:
    # Arabic text processing
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    
    def process_text(text):
        try:
            reshaped_text = reshape(text)
            bidi_text = get_display(reshaped_text)
            return bidi_text
        except Exception as e:
            print(f"Error processing text: {str(e)}")
            return text

    # Main function
    def main():
        input_text = 'مرحبا بالعالم'
        print(process_text(input_text))

    if __name__ == '__main__':
        main()

except MemoryError:
    print("Memory limit exceeded, please increase memory allocation.")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
    sys.exit(1)